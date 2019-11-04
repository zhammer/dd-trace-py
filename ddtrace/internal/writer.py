# stdlib
import itertools
import math
import random
import time

from .. import api
from .. import _worker
from ..internal.logger import get_logger
from ..settings import config
from ..vendor import monotonic
from ddtrace.vendor.six.moves.queue import Queue, Full, Empty

log = get_logger(__name__)


MAX_TRACES = 1000

DEFAULT_TIMEOUT = 5
LOG_ERR_INTERVAL = 60


class AgentWriter(_worker.PeriodicWorkerThread):

    QUEUE_PROCESSING_INTERVAL = 1

    def __init__(self, hostname='localhost', port=8126, uds_path=None, https=False,
                 shutdown_timeout=DEFAULT_TIMEOUT,
                 filters=None, priority_sampler=None,
                 dogstatsd=None):
        super(AgentWriter, self).__init__(interval=self.QUEUE_PROCESSING_INTERVAL,
                                          exit_timeout=shutdown_timeout,
                                          name=self.__class__.__name__)
        self._trace_queue = Q(maxsize=MAX_TRACES)
        self._filters = filters
        self._priority_sampler = priority_sampler
        self._last_error_ts = 0
        self._last_thread_time = 0
        self.dogstatsd = dogstatsd
        self.api = api.API(hostname, port, uds_path=uds_path, https=https,
                           priority_sampling=priority_sampler is not None)
        self.start()

    def recreate(self):
        """ Create a new instance of :class:`AgentWriter` using the same settings from this instance

        :rtype: :class:`AgentWriter`
        :returns: A new :class:`AgentWriter` instance
        """
        return self.__class__(
            hostname=self.api.hostname,
            port=self.api.port,
            uds_path=self.api.uds_path,
            https=self.api.https,
            shutdown_timeout=self.exit_timeout,
            filters=self._filters,
            priority_sampler=self._priority_sampler,
            dogstatsd=self.dogstatsd,
        )

    @property
    def _send_stats(self):
        """Determine if we're sending stats or not."""
        return config.health_metrics_enabled and self.dogstatsd

    def write(self, spans=None, services=None):
        if spans:
            self._trace_queue.put(spans)

    def run(self):
        # Always send the heartbeat metric
        if self.dogstatsd:
            # Report liveliness for this tracer
            self.dogstatsd.gauge('datadog.tracer.heartbeat', 1)
            # Increment a counter for number of writers we have
            # DEV: This is as accurate as we can get since we might have
            #  multiple writers per-process, using a gauge would basically
            #  have them all collapsed into "1" since we don't have a
            #  per-writer unique tag to add here (and shouldn't)
            self.dogstatsd.increment('datadog.tracer.writers')

        try:
            traces = self._trace_queue.get(block=False)
            self.flush_queue(traces)
        except Empty:
            pass

        if not self._send_stats:
            return

        # Statistics about the queue max length
        self.dogstatsd.gauge('datadog.tracer.queue.max_length', self._trace_queue.maxsize)

        # Statistics about the rate at which spans are inserted in the queue
        (
            dropped, accepted, accepted_sum,
            accepted_min, accepted_max, accepted_avg,
        ) = self._trace_queue.reset_stats()
        self.dogstatsd.histogram('datadog.tracer.queue.dropped.traces', dropped)
        self.dogstatsd.increment('datadog.tracer.queue.dropped.traces.sum', dropped)
        self.dogstatsd.histogram('datadog.tracer.queue.enqueued.traces', accepted)
        self.dogstatsd.increment('datadog.tracer.queue.enqueued.traces.sum', accepted)
        self.dogstatsd.gauge('datadog.tracer.queue.enqueued.spans.sum', accepted_sum)
        self.dogstatsd.gauge('datadog.tracer.queue.enqueued.spans.min', accepted_min)
        self.dogstatsd.gauge('datadog.tracer.queue.enqueued.spans.max', accepted_max)
        self.dogstatsd.gauge('datadog.tracer.queue.enqueued.spans.avg', accepted_avg)

        # Statistics about the writer thread
        if hasattr(time, 'thread_time_ns'):
            current_thread_time = time.thread_time()
            diff = current_thread_time - self._last_thread_time
            self._last_thread_time = current_thread_time
            self.dogstatsd.histogram('datadog.tracer.writer.cpu_time', diff)

    def flush_queue(self, traces):
        if self._send_stats:
            traces_flush_length = len(traces)
            traces_flush_spans = sum(map(len, traces))

        # Before sending the traces, make them go through the
        # filters
        try:
            traces = self._apply_filters(traces)
        except Exception as err:
            log.error('error while filtering traces: {0}'.format(err))
            return

        if self._send_stats:
            traces_filtered = len(traces) - traces_flush_length

        # If we have data, let's try to send it.
        traces_responses = self.api.send_traces(traces)
        payload_stats = []
        for response, payload in traces_responses:
            payload_stats.append(payload.stats)
            if isinstance(response, Exception) or response.status >= 400:
                self._log_error_status(response)
            elif self._priority_sampler:
                result_traces_json = response.get_json()
                if result_traces_json and 'rate_by_service' in result_traces_json:
                    self._priority_sampler.set_sample_rate_by_service(result_traces_json['rate_by_service'])

        # Dump statistics
        # NOTE: Do not use the buffering of dogstatsd as it's not thread-safe
        # https://github.com/DataDog/datadogpy/issues/439
        if self._send_stats:
            # Statistics about this flush
            self.dogstatsd.increment('datadog.tracer.flushes')
            self.dogstatsd.histogram('datadog.tracer.flush.traces', traces_flush_length)
            self.dogstatsd.increment('datadog.tracer.flush.traces.sum', traces_flush_length)
            self.dogstatsd.histogram('datadog.tracer.flush.spans', traces_flush_spans)
            self.dogstatsd.increment('datadog.tracer.flush.spans.sum', traces_flush_spans)

            # Statistics about the filtering
            self._flush_stats('traces.filtered', traces_filtered)

            # Statistics about API
            self._flush_stats('api.requests', len(traces_responses))

            # Exceptions raised during API calls
            # DEV: No successful HTTP call was made
            errors = list(e for (e, p) in traces_responses if isinstance(e, Exception))
            for error_type, grouped_errors in itertools.groupby(sorted((type(error).__name__ for error in errors))):
                self._flush_stats('api.errors', len(list(grouped_errors)), tags=['error:%s' % (error_type, )])

            # HTTP API call response stats
            # DEV: Even `status:500` is marked as a response here and not an "api.errors"
            responses = list(r for (r, p) in traces_responses if not isinstance(r, Exception))
            for status, grouped_statuses in itertools.groupby(sorted((r.status for r in responses))):
                self._flush_stats('api.responses', len(list(grouped_statuses)), tags=['status:%s' % (status, )])

            # Statistics about payloads
            self._flush_stats('payloads', len(payload_stats))
            for size, total_traces, total_spans in payload_stats:
                self._flush_stats('payload.size', size)
                self._flush_stats('payload.traces', total_traces)
                self._flush_stats('payload.spans', total_spans)

    run_periodic = run
    on_shutdown = run

    def _flush_stats(self, name, value, tags=None):
        self.dogstatsd.histogram('datadog.tracer.flush.%s' % (name, ), value, tags=tags)
        self.dogstatsd.increment('datadog.tracer.%s' % (name, ), value, tags=tags)

    def _log_error_status(self, response):
        log_level = log.debug
        now = monotonic.monotonic()
        if now > self._last_error_ts + LOG_ERR_INTERVAL:
            log_level = log.error
            self._last_error_ts = now
        prefix = 'Failed to send traces to Datadog Agent at %s: '
        if isinstance(response, api.Response):
            log_level(
                prefix + 'HTTP error status %s, reason %s, message %s',
                self.api,
                response.status,
                response.reason,
                response.msg,
            )
        else:
            log_level(
                prefix + '%s',
                self.api,
                response,
            )

    def _apply_filters(self, traces):
        """
        Here we make each trace go through the filters configured in the
        tracer. There is no need for a lock since the traces are owned by the
        AgentWriter at that point.
        """
        if self._filters is not None:
            filtered_traces = []
            for trace in traces:
                for filtr in self._filters:
                    trace = filtr.process_trace(trace)
                    if trace is None:
                        break
                if trace is not None:
                    filtered_traces.append(trace)
            return filtered_traces
        return traces


class Q(Queue):
    """
    Q is a threadsafe queue that let's you pop everything at once and
    will randomly overwrite elements when it's over the max size.

    This queue also exposes some statistics about its length, the number of items dropped, etc.
    """

    def __init__(self, maxsize=0):
        # Cannot use super() here because Queue in Python2 is old style class
        Queue.__init__(self, maxsize)
        # Number of item dropped (queue full)
        self.dropped = 0
        # Number of items accepted
        self.accepted = 0
        # Cumulative length of accepted items
        self.accepted_sum = 0
        # Min length of accepted items
        self.accepted_min = 0
        # Max length of accepted items
        self.accepted_max = 0
        # Avg length of accepted items
        self.accepted_avg = 0

    def put(self, item):
        try:
            # Cannot use super() here because Queue in Python2 is old style class
            Queue.put(self, item, block=False)
        except Full:
            # If the queue is full, replace a random item. We need to make sure
            # the queue is not emptied was emptied in the meantime, so we lock
            # check qsize value.
            with self.mutex:
                qsize = self._qsize()
                if qsize != 0:
                    idx = random.randrange(0, qsize)
                    self.queue[idx] = item
                    log.warning('Writer queue is full has more than %d traces, some traces will be lost', self.maxsize)
                    self.dropped += 1
                    self._update_stats(item)
                    return
            # The queue has been emptied, simply retry putting item
            return self.put(item)
        else:
            with self.mutex:
                self._update_stats(item)

    def _update_stats(self, item):
        # self.mutex needs to be locked to make sure we don't lose data when resetting
        self.accepted += 1
        if hasattr(item, '__len__'):
            item_length = len(item)
        else:
            item_length = 1

        self.accepted_sum += item_length
        self.accepted_min = min(self.accepted_min, item_length) if self.accepted_min > 0 else item_length
        self.accepted_max = max(self.accepted_max, item_length) if self.accepted_max > 0 else item_length
        self.accepted_avg = math.ceil(self.accepted_sum / float(self.accepted))

    def reset_stats(self):
        """Reset the stats to 0.

        :return: The current value of dropped, accepted and accepted_lengths.
        """
        with self.mutex:
            dropped, accepted, accepted_sum, accepted_min, accepted_max, accepted_avg = (
                self.dropped, self.accepted, self.accepted_sum,
                self.accepted_min, self.accepted_max, self.accepted_avg,
            )
            (
                self.dropped, self.accepted, self.accepted_sum,
                self.accepted_min, self.accepted_max, self.accepted_avg,
            ) = 0, 0, 0, 0, 0, 0
        return dropped, accepted, accepted_sum, accepted_min, accepted_max, accepted_avg

    def _get(self):
        things = self.queue
        self._init(self.maxsize)
        return things
