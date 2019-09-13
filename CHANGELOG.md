
<details><summary>[v0.29.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.29.0) - 2019-09-05T17:25:17Z</summary>
## Upgrading to 0.29.0

This release introduces a new contextvars-based context manager in Python 3.7 and adds support for Tornado 5 and 6 with Python 3.7. In addition, the release includes several updates for our Django integration.

## Changes

### Core

[internal] Add generic rate limiter (#1029)
[internal] Add support for contextvars to tracer in py37 (#990)
[internal] Vendor monotonic package (#1026)
[dev] Update span test utils (#1028)
[dev] Allow extra args to scripts/run-tox-scenario (#1027)
[dev] Remove unused circle env vars for release (#1016)

### Integrations

[tornado] minor documentation fix (#1038)
[tornado] document overriding on_finish and log_exception (#1037)
[tornado] Add support for Tornado 5 and 6 with Python 3.7 (#1034)
[pymongo] Add support for PyMongo 3.9 (#1023)
[django] enable distributed tracing by default (#1031)
[django] Create test for empty middleware (#1022 -- thanks @ryanwilsonperkin)
[django] Patch DBs in django app config (#1019 -- thanks @JBKahn)
[django] Setup pytest-django (#995)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.28.0...v0.29.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/45?closed=1).
</details>
            
<details><summary>[v0.28.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.28.0) - 2019-08-16T16:45:24Z</summary>
## Upgrading to 0.28.0

This release introduces container tagging and adds support for gRPC server.

## Changes

### Integrations

* [grpc] Add support for GRPC server (#960)
* [django] Only set sample rate if rate is set (#1009)
* [django] Update how we get the http.url (#1010)
* [django] Improve Django docs (#1002 -- thanks @adamchainz)
* [pylibmc] Fix client when tracer is disabled (#1004)

### Core

* [core] Parse and send container id with payloads to the agent (#1007)
* [internal] Change log from exception to debug (#1013)
* documentation bugfix (#1017)
* Add back release:wheel (#1015)
* [tests] Adding in helpful default packages (#1008)
* [dev] Map .git into ddtest for setuptools_scm (#1006)
* Use setuptools_scm to handle version numbers (#999)
* Use Python 3 for test_build job (#994)
* writer: fix deprecated log.warn use (#993 -- thanks @deterralba)
* Upload wheels on release (#989)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.27.1...v0.28.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/44?closed=1).
</details>
            
<details><summary>[v0.27.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.27.1) - 2019-07-25T12:32:35Z</summary>
# Upgrading to 0.27.1

This patch release includes performance fix which is highly recommended for anyone currently using 0.27.0.

# Changes

* 0.27 Performance Fix #1000 

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.27.0...v0.27.1)
</details>
            
<details><summary>[v0.27.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.27.0) - 2019-07-12T18:45:44Z</summary>
## Upgrading to 0.27.0

This release introduces improvements to the trace writer. In addition, the release fixes some issues with integrations.

## Changes

### Core

* api: implement __str__ (#980)
* API: add Unix Domain Socket connection support (#975)
* [core] Remove references to runtime-id (#971)
* sampler: rewrite RateByServiceSampler without using Lock (#959)
* Handle HTTP timeout in API writer (#955)
* payload: raise PayloadFull on full payload (#941)

### Integrations

* [pymongo] Support newer msg requests (#985)
* pymongo: Add missing 2013 opcode (#961)
* Refs #983 - Make AIOTracedCursor an async generator  (#984 -- thanks @ewjoachim)
* Fix a typo in AIOTracedCursor docstring (#982 -- thanks @ewjoachim)
* [sqlalchemy] Only set sample rate if configured (#978)

### Documentation

* LICENSE: Fix copyright holder notice (#977 -- thanks @underyx)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.26.0...v0.27.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/43?closed=1).
</details>
            
<details><summary>[v0.26.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.26.0) - 2019-06-05T18:49:55Z</summary>
## Upgrading to 0.26.0

This release introduces several core improvements and continues addressing pain points in our tooling and testing. 

## Changes

### Core

* Add a PeriodicWorker base class for periodic tasks (#934)
* Fix runtime workers not flushing to Dogstatsd (#939)
* api: simplify _put codepath (#956)
* make psutil requirement more accurate (#949 -- thanks @chrono)
* writer: log a message when a trace is dropped (#942)
* span: use system random source to generate span id (#940)
* [core] Add config to set hostname tag on trace root span (#938)

### Integrations

* Support keyword 'target' parameter when wrapping GRPC channels (#946 -- thanks @asnr)
* Record HTTP status code correctly when using abort() with Bottle (#943 -- thanks @equake)
* boto: add support for Python 3.5+ (#930)

### Documentation

* fix documentation for current_root_span (#950 -- thanks @chrono)

### Tooling

* Run flake8 with Python 3 (#957)
* tox: fix ignore path for integrations (#954)
* Remove mention of -dev branch in CircleCI (#931)

### Testing

* [tests] Add benchmarks (#952)
* [tests] increase deviation for sampler by service test (#948)
* [tests] Fix thread synchronization (#947)
* [tests] fix brittle deviation test for tracer (#945)
* [tests] fix threading synchronization to opentracer test (#944
* [pyramid] Fix dotted name for autopatched config test (#932)
* tests: always skip sdist, use develop mode (#928)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.25.0...v0.26.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/42?closed=1).
</details>
            
<details><summary>[v0.25.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.25.0) - 2019-05-07T16:22:39Z</summary>
## Upgrading to 0.25.0

This release includes several core improvements and addresses pain points in our testing/CI. The release also adds a new integration for Algolia Search.

## Changes

### Improvements

- Type cast port number to avoid surprise unicode type (#892 -- thanks @tancnle)
- Add support for Python 3.7 (#864)
- [writer] Enhance Q implementation with a wait based one (#862)
- [core] Add Span 'manual.keep' and 'manual.drop' tag support (#849)
- [core] Vendor msgpack dependency (#848)
- Fix http.url tag inconsitency (#899)
- aiohttp: do not set query string in http.url tag (#923)
- tornado: do not include query string in the http.url tag (#922)
- bottle: fix query string embedded in URL (#921)
- django: remove query string from http.url tag (#920)

### Integrations

- Implement algolia search (#894)

### Tooling

- [dev/tooling] Enforce single quote strings (#884)
- [tests] Leverage tox environment listing to simplify CircleCI tox target list (#882)

### Testing

- tests/tornado: enhance `test_concurrent_requests` (#915)
- doc: disable fixed sidebar (#906)
- [opentracer] Refactor time usage (#902)
- [opentracer] Fix flaky test based on sleep (#901)
- [internal] Add and use RuntimeWorker.join() to remove race condition in testing (#887)
</details>
            
<details><summary>[v0.24.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.24.0) - 2019-04-15T17:57:49Z</summary>
## Upgrading to 0.24.0

This release introduces a new feature (disabled by default), supports new versions of integrations and improves our testing and tooling. 

## Changes

### Improvements

- [core] Enable requests integration by default (#879)
- [core] Fix logging with unset DATADOG_PATCH_MODULES (#872)
- [core] Use DEBUG log level for RateSampler initialization (#861 -- thanks @bmurphey)
- [core] Guard against when there is no current call context (#852)
- [core] Collect run-time metrics (#819)

### Integrations

- [mysql] Remove mysql-connector 2.1 support (#866)
- [aiobotocore] Add support for versions up to 0.10.0 (#865)

### Tooling

- [dev/tooling] Update flake8 to 3.7 branch (#856)
- [dev/tooling] Add script to build wheels (#853)
- [ci] Use tox.ini checksum to update cache (#850)

### Testing

- [tests] Use a macro to persist result to workspace in CircleCI (#880)
- [tests] add psycopg2 2.8 support (#878)
- [aiohttp] Fix race condition in testing (#877)
- [docs] Remove confusing testing instructions from README (#874)
- [tests] Add support for aiohttp up to 3.5 (#873)
- Remove useless __future__ imports (#871)
- [testing] Remove nose usage (#870)
- [tests] Add support for pytest4 (#869)
- [tests] Add testing for Celery 4.3 (#868)
- [tests] Enable integration tests in docker-compose environment (#863)
- [tests] Do not test celery 4.2 with Kombu 4.4 (#858)
- [tests] Fix ddtrace sitecustomize negative test (#857)
- [tests] Use spotify cassandra image for tests (#855)
- [tests] Fix requests gevent tests (#854)
</details>
            
<details><summary>[v0.23.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.23.0) - 2019-03-19T18:53:31Z</summary>
## Upgrading to 0.23.0

With this release we are introducing a new configuration system across integrations to generate APM events for [Trace Search & Analytics](https://docs.datadoghq.com/tracing/visualization/search/). The other core changes are the beginnings of a new approach to address issues with tracer loads and improve debugging.

## Changes

### Improvements

* Trace search client configuration (#828)
* [core] fix wrapt wrappers sources (#836)
* [core] Add Payload class helper (#834)
* [internal] Add rate limited logger (#822)

### Bugs

* Fix for broken celery tests (#839 -- thanks @JackWink)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.22.0...v0.23.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/39?closed=1).
</details>
            
<details><summary>[v0.22.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.22.0) - 2019-03-01T19:00:53Z</summary>
## Upgrading to 0.22.0

This release contains a few improvements for not marking a Celery task as an error if it is an expected and allowed exception, for propagating synthetics origin header, and to vendor our `six` and `wrapt` dependencies.

## Changes
### Improvements
- [celery] Don't mark expected failures as errors (#820 -- thanks @sciyoshi)
- [core] Propagate x-datadog-origin (#821)
- [core] vendor wrapt and six dependencies (#755)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.21.1...v0.22.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/36?closed=1).

</details>
            
<details><summary>[v0.21.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.21.1) - 2019-02-21T21:57:40Z</summary>
## Upgrading to 0.21.1

This is a bug fix release that requires no changes to your code.

Included in this release is a fix for some database cursors where we would force `Cursor.execute` and `Cursor.executemany` to return a cursor instead of the originally intended output. This caused an issue specifically with MySQL libraries which tried to return the row count and we were returning a cursor instead.

## Changes
### Bugs
* [core] Patch logging earlier for ddtrace-run (#832)
* [dbapi2] Fix dbapi2 execute/executemany return value (#830 )
* [core] Use case-insensitive comparison of header names during extract (#826 -- thanks @defanator)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.21.0...v0.21.1) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/38?closed=1).

</details>
            
<details><summary>[v0.21.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.21.0) - 2019-02-19T17:20:31Z</summary>
## Upgrading to 0.21.0

With this release we are moving distributed tracing settings to be enabled by default. This change means that you no longer need to explicitly enable distributed tracing for any integration.

## Changes
### Improvements
- Enable distributed tracing by default (#818)
  - aiohttp
  - bottle
  - flask
  - molten
  - pylons
  - pyramid
  - requests
  - tornado
- [testing] Ensure consistent use of override_config and override_env (#815)
- [core] Break up ddtrace.settings into sub-modules (#814)
- [tests] Simplify elasticsearch CI test commands (#813)
- [core] Remove sending of service info (#811)
- [core] Add import hook module (#769)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.20.4...v0.21) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/35?closed=1).
</details>
            
<details><summary>[v0.20.4](https://github.com/DataDog/dd-trace-py/releases/tag/v0.20.4) - 2019-02-08T17:35:51Z</summary>
## Upgrading to 0.20.4

This is a bug fix release, no code changes are required.

In this release we have fixed a bug that caused some configuration values to not get updated when set.

## Changes
### Bug fixes
* [bug] Integration config keys not being updated (#816)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.20.3...v0.20.4) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/37?closed=1).

</details>
            
<details><summary>[v0.20.3](https://github.com/DataDog/dd-trace-py/releases/tag/v0.20.3) - 2019-02-04T20:07:58Z</summary>
## Upgrading to 0.20.3

This is a bug fix release that requires no changes.

This release includes a fix for context propagation with `futures`. Under the right conditions we could incorrectly share a trace context between multiple `futures` threads which result in multiple traces being joined together in one.

## Changes
### Bug fixes
* [core] Allow futures to skip creating new context if one doesn't exist (#806)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.20.2...v0.20.3) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/37?closed=1).
</details>
            
<details><summary>[v0.20.2](https://github.com/DataDog/dd-trace-py/releases/tag/v0.20.2) - 2019-01-29T21:47:49Z</summary>
## Upgrading to 0.20.2

No changes are needed to upgrade to `0.20.2`.

This big fix release includes changes to ensure we properly read the HTTP response body from the trace agent before we close the HTTP connection.

## Changes
### Bug fixes

- [core] Call HTTPResponse.read() before HTTPConnection.close() (#800)

### Improvements
- [tests] limit grpcio version to >=1.8.0,<1.18.0 (#802)
- [tools] Add confirmation to 'rake pypi:release' task (#791 )

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.20.1...v0.20.2) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/36?closed=1).
</details>
            
<details><summary>[v0.20.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.20.1) - 2019-01-17T14:13:18Z</summary>
## Upgrading to 0.20.1

No changes are needed to upgrade

## Changes
### Bug fixes
[celery] Ensure `celery.run` span is closed when task is retried (#787)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.20.0...v0.20.1) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/36?closed=1).
</details>
            
<details><summary>[v0.20.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.20.0) - 2019-01-09T19:10:40Z</summary>
# Upgrading to 0.20.0

We have added support for logs injection to the tracer. If you are already using `ddtrace-run`, the integration can be enabled with setting the environment variable `DD_LOGS_INJECTION=true`. The default behavior once logs injection is enabled is to have trace information inserted into all log entries. If you prefer more customization, you can manually instrument and configure a log formatter with the tracer information.

# Changes

## New Integrations

* [mako] Add Mako integration (#779 -- thanks @wklken)

## Enhancements

* [core] Tracer and logs integration (#777)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.19.0...v0.20.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/34?closed=1).
</details>
            
<details><summary>[v0.19.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.19.0) - 2018-12-28T19:16:44Z</summary>
## Upgrading to 0.19.0

With `0.19.0` we have decided to disable the tracing of `dbapi2` `fetchone()`/`fetchmany()`/`fetchall()` methods by default.

This change effects all integrations which rely on the `dbapi2` API, including `psycopg2`, `mysql`, `mysqldb`, `pymysql`, and `sqlite3`.

We have introduced this change to reduce the noise added to traces from having these methods (mostly `fetchone()`) traced by default.

With `fetchone()` enabled the traces received can get very large for large result sets, the resulting traces either become difficult to read or become too large causing issues when flushing to the trace agent, potentially causing traces to be dropped.

To re-enable the tracing of these methods you can either configure via the environment variable `DD_DBAPI2_TRACE_FETCH_METHODS=true` or manually via:

```python
from ddtrace import config
config.dbapi2.trace_fetch_methods = True
```

## Changes
### Bugs
[dbapi2] disable fetchone/fetchmany/fetchall tracing by default (#780)
[opentracing] Fixing context provider imports for scope manager (#771 -- thanks @Maximilien-R)

### Enhancements
[tests] test python setup.py sdist and twine check on build (#782)
[core] Add API to configure Trace Search (#781)
[core] Enable priority sampling by default (#774)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.18.0...v0.19.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/32?closed=1).
</details>
            
<details><summary>[v0.18.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.18.0) - 2018-12-12T21:12:57Z</summary>
## New Integrations

* [molten] Add molten support (#685)

## Bug Fixes

* [aws] Blacklist arguments stored as tags (#761)
* [psycopg2] Fix composable query tracing (#736)

## Improvements

* [aiohttp] Add HTTP method to the root span resource (#652 -- thanks @k4nar)
* [aws]Flatten span tag names (#768)
* [opentracer] Set global tags (#764)
* [core] add six and replace custom compat functions (#751)
* [config] make IntegrationConfig an AttrDict (#742)
* [tests] remove unused monkey.py test file (#760)
* [tests] fix linting in test files (#752)
* [psycopg2] fix linting issues (#749)
* [tests] have most tests use pytest test runner (#748)
* [tests] Provide default implementation of patch test methods (#747)
* [tests] run flake8 on all test files (#745)
* [tests] Add patch mixin and base test case (#721)
* [tests] Add Subprocess TestCase (#720)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.17.1...v0.18.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/30?closed=1).
</details>
            
<details><summary>[v0.17.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.17.1) - 2018-12-05T21:51:11Z</summary>
This release includes the removal of service sending, this should resolve many of the 400s that are being returned from the Agent resulting in an unfriendly `ERROR` message and giving the impression that the tracer is failing. (#757)

## Improvements
- [core] Make writing services a no-op (#735)
- [tests] upgrade flake8 to 3.5.0 (#743)
- remove flake8 ignores and fix issues (#744)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.17.0...v0.17.1) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/31?closed=1).
</details>
            
<details><summary>[v0.17.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.17.0) - 2018-11-28T17:37:20Z</summary>
## New features
- [redis] add support for redis 3.0.0 (#716)
- [core] Allow DD_AGENT_HOST and DD_TRACE_AGENT_PORT env variables (#708)
- [core] Add global tracer tags (#702)
- [core] Trace http headers (#647)

## Improvements
- [docs] add Flask configuration documentation (#734)
- Add long_description to setup.py (#728)
- [tests] pin version of redis-py-cluster for 'tox -e wait' (#725)
- [requests] Add another split_by_domain test (#713)
- [docs] Add kombu references (#711)
- [ci] Use small circleci resource class for all jobs (#710)
- [requests] patch Session.send instead of Session.request (#707)
- [ci] reorganize CircleCI workflows (#705)
- [elasticsearch] add support for elasticsearch{1,2,5} packages (#701)
- [tests] add base test case classes and rewrite tracer tests (#689)
- [dbapi] Trace db fetch and session methods (#664)

## Bugfixes
- [elasticsearch] add alias for default _perform_request (#737)
- [tests] Pin pytest to 3.x.x and redis to 2.10.x for rediscluster (#727)
- [django] Use a set instead of list for cache_backends to avoid duplicates (#726 -- thanks @wenbochang)
- [tests] fix broken redis check (#722)
- [docs] Fix broken flask link (#712)
- [mongodb] Fix pymongo query metadata (#706)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.16.0...v0.17.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/29?closed=1).
</details>
            
<details><summary>[v0.16.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.16.0) - 2018-11-13T16:18:47Z</summary>
## New Integrations
* [jinja2] Add jinja2 integration (#649 -- thanks @mgu)
* [kombu] add Kombu integration (#515 -- thanks @tebriel)
* [grpc] Add grpc client support. (#641)
* [gevent] Support gevent 1.3 (#663)
* [flask] rewrite Flask integration (#667)

## Bug Fixes
* [mysqldb] Fix mysqldb monkey patch (#623 -- thanks @benjamin-lim)
* [requests] exclude basic auth from service name (#646 -- thanks @snopoke)

## Improvements
* [core] Add IntegrationConfig helper class (#684)
* [core] add support for integration span hooks (#679)
* [httplib, requests] Sanitize urls in span metadata (#688)
* [tests] ensure we are running tests.contrib.test_utils (#678)
* [celery] [bottle] Add span type information for celery and bottle. (#636)
* [ci] Reorganize autopatch test calls (#670)
* [core] initial support for partial flushes (#668)
* [django] Remove query from django db span's tag sql.query (#659)
* [tests] Make CI faster by disabling dist and install in autopatching tests (#654)
* [core] Trace http headers (#647)
* [django] Infer span resource name when internal error handler is used (#645)
* [elasticsearch] Make constant organization consistent with other integrations (#628)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.15.0...v0.16.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/28?closed=1).

</details>
            
<details><summary>[v0.15.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.15.0) - 2018-10-16T19:01:55Z</summary>
**New integrations**

- Add [rediscluster](https://pypi.org/project/redis-py-cluster/) integration (#533, #637)
- Add [Vertica](https://github.com/vertica/vertica-python) Integration (#634)

**Bug fixes**

- [django] Fix minimum Django version for user.is_authenticated property (#626 -- thanks @browniebroke)

**Improvements**

- [celery] Add retry reason metadata to spans (#630)
- [core] Update config to allow configuration before patching (#650)
- [core] Add Tracer API to retrieve the root Span (#625)
- [core] Fixed `HTTPConnection` leaking (#542 -- thanks @mackeyja92)
- [django] Allow Django cache to be seen as a different service. (#629)
- [gevent] Patch modules on first import (#632)
- [gevent] Add support for gevent.pool.Pool and gevent.pool.Group (#600)
- [redis] Removed unused tag (#627)
- [requests] Patch modules on first import (#632)
- [tests] Add Span.span_type tests (#633)
- [tests] Update the integrations libraries versions to the latest possible. (#607)
- [tests] CircleCI run tests in the new alpine-based test runner (#638)
- [tests] Add test cases for API._put (#640)
- [tests] Skip flaky TestWorkers.test_worker_multiple_traces test case (#643)
- [tests] Remove tests for not supported gevent 1.3 (#644)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.14.1...v0.15.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/25?closed=1).
</details>
            
<details><summary>[v0.14.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.14.1) - 2018-09-25T16:05:12Z</summary>
**Bug fixes**
- [opentracer] Activate span context on extract (#606, #608)
- [opentracer] Fix "does not provide the extra opentracing" (#611, #616)

**Improvements**
- [docs] Clarify debug mode (#610)
- [docs] Fix docstring for `Tracer.set_tags` (#612 -- thanks @goodspark)
- [docs] Add priority sampling to ddtrace-run usage (#621)
- [circleci] Imrpve python docs deployment strategy (#615)
- [tests] Refactor tox.ini file (#609)
- [tests] Improve performance of tests execution (#605)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.14.0...v0.14.1) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/27?closed=1).
</details>
            
<details><summary>[v0.14.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.14.0) - 2018-09-11T18:28:55Z</summary>
**OpenTracing**

In this release we are happy to introduce the beta for the long-awaited OpenTracing compatible API layer for `ddtrace`!

Support for `opentracing>=2.0.0` is provided in this release. Namely, the following are supported:

- `start_span`/`start_active_span`
- `inject` and `extract` functionality
- `baggage`, through `set_baggage_item` and `get_baggage_item`
- compatible tags from the [OpenTracing specification](https://github.com/opentracing/specification/blob/b193756f1fe646b79ef4f901bed92c0e72845440/semantic_conventions.md#standard-span-tags-and-log-fields)
- scope manager support
- seamless integration with the Datadog tracer when using `ddtrace-run`

For setup information and usage see [our docs for the Datadog OpenTracing tracer](http://pypi.datadoghq.com/trace/docs/installation_quickstart.html#opentracing).


**CI Improvements**

Also included in this release are some optimizations to our CI which should get things running a bit quicker.

Thanks @labbati!



Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.13.1...v0.14.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/20?closed=1).
</details>
            
<details><summary>[v0.13.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.13.1) - 2018-09-04T15:48:39Z</summary>
**Bug fixes**

* [core] remove the root logger configuration within the library (#556)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.13.0...v0.13.1) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/24?closed=1).
</details>
            
<details><summary>[v0.13.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.13.0) - 2018-08-23T12:53:23Z</summary>
**New integrations**
- [`pymemcache`](https://github.com/pinterest/pymemcache) integration (#511)

**Celery integration**

Due to some limitations with our Celery integration, we changed our instrumentation to a [signals based approach](http://docs.celeryproject.org/en/latest/userguide/signals.html). We also started using import hooks to instrument Celery, so that enabling the instrumentation doesn't trigger a `celery` import.

- Signals implementation: #530
- Moving to import hooks: #534
- Resolved issues: #357, #493, #495, #495, #510, #370

**Breaking changes**
Using the signal based approach increase the stability of our instrumentation, but it limits what is currently traced. This is a list of changes that are considered breaking changes in the behavior and not in the API, so no changes are needed in your code unless you want a different behavior:
- By default all tasks will be traced if they use the Celery signals API, so tasks invoked with methods like `apply()`,  `apply_async()` and `delay()` will be traced but tasks invoked with `run()` will **not** be traced. 
- `patch_task()` is deprecated; if it's used, all tasks will be instrumented

**Bug fixes**
- [core] check if bootstrap dir is in path before removal (#516 -- thanks @beezz!)
- [core] have hostname default to `DATADOG_TRACE_AGENT_HOSTNAME` environment variable if available (#509, #524 -- thanks @hfern!)
- [core] add WSGI-style http headers support to HTTP propagator (#456, #522)
- [core] Enable buffering on `getresponse` (#464, #527)
- [core] configure the root logger (#536)
- [aiopg] set the `app_type` during initialization (#492, #507)
- [boto] default to `None` if no region (#525, #526)
- [flask] avoid double instrumentation when `TraceMiddleware` is used (#538)
- [pymongo] fix multiple host kwargs (#535)
- [tornado] make settings object accessible during configuration (#499, #498 -- thanks @kave!)

**Improvements**
- [core/helpers] add a shortcut to retrieve Trace correlation identifiers (#488)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.12.1...v0.13.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/21?closed=1).
</details>
            
<details><summary>[v0.12.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.12.1) - 2018-06-14T09:08:28Z</summary>
**Bugfixes**

* [celery] add support for celery v1 tasks (old-style tasks) (#465, #423)
* [celery] `ddtrace-run` broke third-party script support; now it handles correctly the `argv` params (#469, #423)
* [celery] patch `TaskRegistry` to support old-style task with `ddtrace-run` (#484)
* [django] update error handling if another middleware has handled the exception already (#418, #462)
* [django] `DatabaseWrapper` loaded in right thread, after removing `setting_changed` signal from the `DatadogSettings` (#481, #435)
* [django/celery] add `shared_task` decorator wrapper to trace properly Celery tasks (#486, #451)
* [django/docs] notes about Debug Mode, and debugging (#476 -- thanks @ndkv!)
* [gevent] pass `sampling_priority` field when Distributed Tracing is enabled (#457)
* [mysqlb] add missing services info when they're flushed (#468, #428)
* [psycopg2] properly patch the driver when `quote_ident` typing is used (#477, #474, #383)
* [pylons] ensure the middleware code is Python 3 compatible to avoid crashes on import (#475, #472)
* [requests] add missing services info when they're flushed (#471, #428)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.12.0...v0.12.1) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/19?closed=1).
</details>
            
<details><summary>[v0.12.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.12.0) - 2018-05-03T12:04:59Z</summary>
**New integrations**
* [boto] Botocore and boto instrumentation is enabled by default using `patch_all()` (#319)
* [futures] provide context propagation for `concurrent` module (#429, [docs](http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.futures))
* [mysql] add `pymysql` support (#296, [docs](http://pypi.datadoghq.com/trace/docs/#mysql) -- thanks @wklken)

**Improvements**
* [core] introducing a low-level API to define configurations for each integration. This API is used only by the `requests` module and will be implemented in other integrations in newer releases (#445, #443, #450, #454, #441)
* [celery] split the service name in `celery-producer` and `celery-worker` for better stats (#432)
* [falcon] add distributed tracing (#437)
* [requests] provide a default service name for the request `Span` (#433)
* [requests] add `split_by_domain ` config to split service name by domain (#434)
* [tornado] better compatibility using `futures` instrumentation (#431)

**Bugfixes**
* [core] ensure `sitecustomize.py` is imported when `ddtrace-run` wrapper is used (#458)
* [flask] use `ddtrace` logger instead of Flask to avoid having a custom log filter (#447, #455)

**Breaking changes**
* [celery] the name of the service is now split in two different services: `celery-producer` and `celery-worker`. After the upgrade, you'll stop sending data to what was the default service name (`celery`). You should check the new services instead because you'll see a drop. Previously reported traces in the `celery` service, are still available if you move back the time selector.

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.11.1...v0.12.0) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/17?closed=1).
</details>
            
<details><summary>[v0.11.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.11.1) - 2018-03-30T09:47:54Z</summary>
**Improvements**

* [bottle] use the `route` argument in `TracePlugin`, to support Bottle 0.11.x (#439)

**Bugfixes**

* [django] gunicorn gevent worker wasn't instrumenting database connections (#442)
* [django] remove `MIDDLEWARE_CLASSES` deprecation warning from tests (#444)
* [django] ensure only `MIDDLEWARE` or `MIDDLEWARE_CLASSES` are loaded with tracing middlewares (#446)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.11.0...v0.11.1) and the [release milestone](https://github.com/DataDog/dd-trace-py/milestone/18?closed=1).
</details>
            
<details><summary>[v0.11.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.11.0) - 2018-03-05T10:50:23Z</summary>
**Security fixes**

* [dbapi] remove `sql.query` tag from SQL spans, so that the content is properly obfuscated in the Agent. This security fix is required to prevent wrong data collection of reported SQL queries. This issue impacts only MySQL integrations and NOT `psycopg2` or `sqlalchemy` while using the PostgreSQL driver. (#421)

**New integrations**

* [django] add support for Django 2.0 (#415 -- thanks @sciyoshi!)
* [mysql] `MySQL-python` and `mysqlclient` packages are currently supported (#376 -- thanks @yoichi!)
* [psycopg2] add support for version 2.4 (#424)
* [pylons] Pylons >= 0.9.6 is officially supported (#416)

**Bugfixes**

* [core] `ddtrace-run` script accepts `DATADOG_PRIORITY_SAMPLING` to enable [Priority Sampling](http://pypi.datadoghq.com/trace/docs/#priority-sampling) (#426)
* [pylons] add distributed tracing via kwarg and environment variable (#425, [docs](http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.pylons))
* [pylons] `ddtrace-run` script can patch a `PylonsApp` (#416)
* [pylons] add tracing to Pylons `render` function (#420)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.10.1...v0.11.0) and [0.11.0 milestone](https://github.com/DataDog/dd-trace-py/milestone/15?closed=1).
</details>
            
<details><summary>[v0.10.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.10.1) - 2018-02-05T14:17:49Z</summary>
**Distributed Tracing**
Add distributed tracing using integration settings for the following libraries/frameworks:
* `bottle` (#382)
* `requests` (#372)
* `pyramid` (#403)

**Improvements**
* [core] provide constants to pick Priority Sampling values (#391)
* [django] add support for Django Rest Framework (#389)
* [tooling] add missing classifiers for pypi (#395 -- thanks @PCManticore)
* [tornado] patch `concurrent.futures` if available, improving the way traces are built when propagation happens between threads (#362 -- thanks @codywilbourn)

**Bugfixes**
* [httplib] don't overwrite return value (#380 -- thanks @yoichi)
* [psycopg2] patch all imports of `register_type` (#393 -- thanks @stj)
* [pyramid] keep request as part of `render` kwargs (#384 -- thanks @joual)
* [pyramid] use pyramid `HTTPExceptions` as valid response types (#401, #386 -- thanks @TylerLubeck)
* [requests] add `unpatch` and double-patch protection (#404)
* [flask] don't override code of already handled errors (#390, #409)
* [flask] allow mutability of `resource` field within request (#353, #410)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.10.0...v0.10.1).
</details>
            
<details><summary>[v0.10.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.10.0) - 2017-11-08T17:59:28Z</summary>
**Distributed Sampling (beta)**

New feature that propagates the sampling priority across services. This is useful to mark traces as "don’t keep the trace" or "must have" when distributed tracing is used. This new functionality requires at least the Datadog Agent 5.19+. Frameworks with out-of-the-box support are: Django, Flask, Tornado (#358, #325, #359, #364, #366, #365, #371, [docs](http://pypi.datadoghq.com/trace/docs/#priority-sampling))

**Improvements**
* [core] update the Context propagation API, that includes a new way to retrieve and set the current active `Span` context. (#339)
* [core] implement Propagators API to simplify Distributed Tracing. You can use `HTTPPropagator` class to inject and extract the tracing context in HTTP headers (#363, #374 [docs](http://pypi.datadoghq.com/trace/docs/#ddtrace.propagation.http.HTTPPropagator))
* [celery] use service name from `DATADOG_SERVICE_NAME` env var, if defined (#347 -- thanks @miketheman)
* [django] respect env Agent host and port if defined (#354 -- thanks @spesnova)

**Bugfixes**
* [pylons] handle exception with non standard 'code' attribute (#350)
* [pyramid] the application was not traced when the tween list was explicitly specified (#349)

Read the full [changeset](https://github.com/DataDog/dd-trace-py/compare/v0.9.2...v0.10.0)
</details>
            
<details><summary>[v0.9.2](https://github.com/DataDog/dd-trace-py/releases/tag/v0.9.2) - 2017-09-12T13:24:39Z</summary>
**New features**
* [django] disable database or cache instrumentation via settings so that each Django component instrumentation can be disabled (#314, [docs](http://localhost:8000/#module-ddtrace.contrib.django) -- thanks @mcanaves)
* [django] it's not required anymore to add the Django middleware because the Django app ensures that it is installed. You can safely remove `ddtrace.contrib.django.TraceMiddleware` for your middleware list after the upgrade. This is not mandatory but suggested (#314, #346)
* [cassandra] trace `execute_async()` operations (#333)

**Bugfixes**
* [mysql]  prevent the Pin from attaching empty tags (#327)
* [django] fixed the initialization order to prevent logs when the tracer is disabled (#334)
* [sqlite3] add tests to ensure that services are properly sent (#337)
* [pyramid] fixed Pyramid crash when 'include()' is used with relative import paths (#342)
* [pylons] re-raise the exception with the original traceback in case of errors. Before Pylons exceptions were correctly handled but hidden by the tracing middleware. (#317)
* [pyramid] disable autocommit in Pyramid patching, to avoid altering the `Configurator` behavior (#343)
* [flask] fix Flask instrumentation that didn't close Jinja spans if an error was thrown (#344)

**Integration coverage**
* officially support ElasticSearch 1.6+ (#341)

**Documentation**
* fixed usage examples for `patch_all()` and `patch()` (#321 -- thanks @gomlgs)
* added a section about updating the hostname and port (#335)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.9.1...v0.9.2).
</details>
            
<details><summary>[v0.9.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.9.1) - 2017-08-01T11:29:46Z</summary>
**New features**
* [core] add a processing pipeline to the `AsyncWorker`, so that traces can be filtered easily. This change doesn't have any performance impact with existing installations, and is expected to work well with async frameworks / libraries (#303, [docs](http://pypi.datadoghq.com/trace/docs/#trace-filtering))
* [core] add language and library version metadata to keep track of them in the Datadog Agent. All values are sent via headers (#289)

**Bugfixes**
* [aiobotocore] update `async with` context manager so that it returns the wrapper instead of the wrapped object (#307)
* [boto, botocore] change the service metadata app for AWS with a more meaningful name (#315)

**Documentation**
* improving documentation so that it's more explicit how a framework should be auto-instrumented (#305, #308)
* add the list of auto-instrumented modules (#306)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.9.0...v0.9.1).
</details>
            
<details><summary>[v0.9.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.9.0) - 2017-07-05T12:20:40Z</summary>
**New features**

* [core] add process ID in root spans metadata (#293)

**Improvements**

* [falcon] extended support for Falcon 1.2; improved error handling (#295)
* [gevent] create a new `Context` when a Greenlet is created so that the tracing context is automatically propagated with the right parenting (#287)
* [asyncio] providing helpers and `patch()` method to automatically propagate the tracing context between different asyncio tasks (#260 #297, [docs](http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.asyncio) -- thanks @thehesiod)
* [aiohttp] add experimental feature to continue a trace from request headers (#259, [docs](http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.aiohttp) -- thanks @thehesiod)
* [django] add `DEFAULT_DATABASE_PREFIX` setting to append a prefix to database service (#291, [docs](http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.django) -- thanks @jairhenrique)

**Bugfixes**

* [logging] use specific logger instead of the root one in `monkey.py` module (#281)
* [django] `ddtrace` exception middleware catches exceptions even if a custom middleware returns a `Response` object (#278)
* [pylons] handle correctly the http status code when it's wrongly formatted (#284)
* [django] request resource handles the case where the `View` is a partial function (#292)
* [flask] attach stack trace to Flask errors (#302)

**New integrations**

* [httplib] add patching for `httplib` and `http.lib`(#137 -- thanks @brettlangdon)
* [aio-libs] add `aiobotocore` support (#257, #298, [docs](http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.aiobotocore) -- thanks @thehesiod)
* [aio-libs] add `aiopg` support (#258, [docs](http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.aiopg) -- thanks @thehesiod)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.8.5...v0.9.0).
</details>
            
<details><summary>[v0.8.5](https://github.com/DataDog/dd-trace-py/releases/tag/v0.8.5) - 2017-05-30T16:17:19Z</summary>
**Bugfixes**

* [flask] add the http method to flask spans (#274)
* [sqlite3] changed the app_type to `db` (#276)
* [core] `span.set_traceback()`now sets the traceback even if there's no exception (#277)

Read the [full changeset][1].

[1]: https://github.com/DataDog/dd-trace-py/compare/v0.8.4...v0.8.5
</details>
            
<details><summary>[v0.8.4](https://github.com/DataDog/dd-trace-py/releases/tag/v0.8.4) - 2017-05-19T09:27:43Z</summary>
**Bugfixes**

* [flask] avoid using weak references when Flask is instrumented via Blinker. This resolves initialization issues when the `traced_app = TraceMiddleware(app, ...)` reference goes out of the scope or is garbage collected (#273)
</details>
            
<details><summary>[v0.8.3](https://github.com/DataDog/dd-trace-py/releases/tag/v0.8.3) - 2017-05-15T11:17:17Z</summary>
**Improvements**

* [transport] add presampler header (`X-Datadog-Trace-Count`) so that the receiving agent has more information when dealing with sampling (#254)
* [docs] updated our documentation (#264, #271)

**Bugfixes**
* [core] patch loader raises `PatchException` that is handled in the `patch_all()` when the patch failed. This distinguishes: errors during patch, when an integration is not available and simply when the module is not installed (#262)
* [mysql] distinguish `MySQL-Python` instrumentation so that only `mysql-connector` package is patched; this provides better feedback about what library is supported (#263, #266)
* [sqlalchemy] provide a `patch()` method that uses the PIN object; this is not a breaking change, but the preferred way to instrument SQLAlchemy is through `patch_all(sqlalchemy=True)` or `patch(sqlalchemy=True)` (#261)
* [pylons] catch `BaseException` since a `SystemExit` might've been raised; `500` errors are handled if a timeout occurs (#267, #270)
* [pyramid] catch `BaseException` since a `SystemExit` might've been raised; `500` errors are handled if a timeout occurs (#269)

Read the [full changeset][1]

[1]: https://github.com/DataDog/dd-trace-py/compare/v0.8.2...v0.8.3
</details>
            
<details><summary>[v0.8.2](https://github.com/DataDog/dd-trace-py/releases/tag/v0.8.2) - 2017-04-28T15:43:49Z</summary>
**Bugfixes**

* [django] handle tuple `INSTALLED_APPS` for Django < 1.9 (#253)

Read the [full changeset][1]

[1]: https://github.com/DataDog/dd-trace-py/compare/v0.8.1...v0.8.2
</details>
            
<details><summary>[v0.8.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.8.1) - 2017-05-30T16:16:15Z</summary>
**Bugfixes**

* [core] fixed `msgpack-python` kwarg usage for versions earlier than `0.4.x` (#245)
* [pyramid] add request method to Pyramid trace span resource name (#249, thanks @johnpkennedy)

Read the [full changeset][1].

[1]: https://github.com/DataDog/dd-trace-py/compare/v0.8.0...v0.8.1
</details>
            
<details><summary>[v0.8.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.8.0) - 2017-04-10T17:19:35Z</summary>
**New integrations**
* Add support for Tornado web `4.0+`. Currently this integration is ignored by autopatching, but can be enabled via `patch_all(tornado=True)` (#204, [docs][1] -- thanks @ross for reviewing and testing the implementation)

**Bugfixes**
* [docs] Minor updates to our documentation (#239, #237, #242, #244 -- thanks @liubin @pahaz)
* [boto] Boto2 and Botocore integrations have safety check to prevent double patching (#240)
* [boto] Use frames directly without calling `getouterframes()`. This is a major improvement that reduces the impact of our tracing calls for Boto2 (#243 -- thanks @wackywendell)
* [django] make `func_name` work with any callable and not only with functions (#195, #203 -- thanks @m0n5t3r)

**Breaking change**
* [elasticsearch] when importing `elasticsearch` before executing `patch_all()`, no traces are created. This patch changed where the `PIN` object is attached, so you should update your instrumentation as described below (#238)

**Migrate from 0.7.x to 0.8.0**

* [elasticsearch] the PIN object was previously attached to the `elasticsearch` module while now it uses `elasticsearch.Transport`. If you were using the `Pin` to override some tracing settings, you must update your code from:
```python
Pin.override(client, service='elasticsearch-traces')
```
to:
```python
Pin.override(client.transport, service='elasticsearch-traces')
```

**Internals update**
* the Python traces logs and returns error when there is a communication issue with the APM Agent (#173)
* the `wrap()` tracer decorator can be extended by Python integrations when the usual approach is not suitable for the given execution context (#221)

Read the [full changeset][2].

[1]: http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.tornado
[2]: https://github.com/DataDog/dd-trace-py/compare/v0.7.0...v0.8.0
</details>
            
<details><summary>[v0.7.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.7.0) - 2017-03-29T18:08:09Z</summary>
**New integrations**
* Add support for `boto` (>=2.29.0) and `botocore` (>= 1.4.51) #209 . Currently these integrations are ignored by autopatching, but can be enabled via `patch_all(boto=True, botocore=True)`

**New features**
* Add the `ddtrace-run` command-line entrypoint to provide tracing without explicit additions to code. More information here http://pypi.datadoghq.com/trace/docs/#get-started #169 

**Bugfixes**
* [dbapi] Ensure cursors play well with context managers #231 
* [django] Provide a unique `datadog_django` app label to avoid clashes with existing app configs #235 
* [pyramid] Ensure pyramid spans have method and route metadata consistent with other web frameworks #220 (thanks @johnpkennedy)
</details>
            
<details><summary>[v0.6.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.6.0) - 2017-03-09T13:47:35Z</summary>
**New integrations**
* Add support for asynchronous Python. This is a major improvement that adds support for `asyncio`, `aiohttp` and `gevent` (#161, docs: [asyncio][1] - [aiohttp][2] - [gevent][3])
* Add Celery integration (#135, #196, [docs][6])

**New features**
* Add explicit support for Python 3.5, and 3.6 (#215, see [supported versions][7])
* print the list of unfinished spans if the `debug_logging` is activated; useful in synchronous environments to detect unfinished/unreported traces (#210)

**Bugfixes**
* [mysql] `mysql` integration is patched when using `patch()` or `patch_all()` (#178)
* [django] set global tracer tags from Django `DATADOG_TRACE` setting (#159)
* [bottle] wrong `tracer` reference when `set_service_info` is invoked (#199)

**Breaking changes**
* Default port `7777` has been replaced with the new `8126` available from Datadog Agent 5.11.0 and above (#212)
* Removed the `ThreadLocalSpanBuffer`. It has been fully replaced by the `Context` propagation (#211)

**Migrate from 0.5.x to 0.6.0**

* Datadog Agent 5.11.0 or above is required.
* If you're using the `ThreadLocalSpanBuffer` manually, you need to use the [Context class][8] in your logic so that it is compliant with the `Context` propagation. Check the [Advanced usage][9] section.

**Advanced usage**
This is a list of new features that may be used for manual instrumentation when you're using a library or a framework that is not currently supported:
* Use `Context` propagation instead of a global buffer. This plays well with asynchronous programming where a context switching may happen while handling different logical execution flows (#172)
* `tracer.trace()` handles automatically the `Context` propagation and remains the preferable API
* Add `tracer.get_call_context()` to retrieve the current `Context` instance that is holding the entire trace for this logical execution ([docs][4])
* Add `start_span` as a way to manually create spans, while handling the Context propagation ([docs][5])

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.5.5...v0.6.0).

[1]: http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.asyncio
[2]: http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.aiohttp
[3]: http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.gevent
[4]: http://pypi.datadoghq.com/trace/docs/#ddtrace.Tracer.get_call_context
[5]: http://pypi.datadoghq.com/trace/docs/#ddtrace.Tracer.start_span
[6]: http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.celery
[7]: http://pypi.datadoghq.com/trace/docs/#supported-versions
[8]: https://github.com/DataDog/dd-trace-py/blob/853081c0f2707bcda59c50239505a5ceaed33945/ddtrace/context.py#L8
[9]: http://pypi.datadoghq.com/trace/docs/#advanced-usage
</details>
            
<details><summary>[v0.5.5](https://github.com/DataDog/dd-trace-py/releases/tag/v0.5.5) - 2017-02-15T15:29:56Z</summary>
**Improvements**
- ElasticSearch integration takes care of the returning status code in case of a `TransportError` (#175)

**Bugfixes**
- Pyramid integration handles properly the `Span.error` attribute if the response is a server error (#176)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.5.4...v0.5.5).

</details>
            
<details><summary>[v0.5.4](https://github.com/DataDog/dd-trace-py/releases/tag/v0.5.4) - 2017-02-14T19:50:33Z</summary>
## Integrations
- added the Pyramid web framework

## Enhancements
- `tracer.set_tags()` will add tags to all spans created by a tracer.
- `span.tracer()` will return the tracer that created a given span 

## Bug Fixes
- correctly set service types on the Mongo and Falcon integrations.
- documentation fixes
- send less data to the agent in the SQL and redis integrations.

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.5.3...master)

</details>
            
<details><summary>[v0.5.3](https://github.com/DataDog/dd-trace-py/releases/tag/v0.5.3) - 2016-12-23T08:50:32Z</summary>
**Bugfixes**
- [ElasticSearch] use ElasticSearch serializer so that the serialization works with dates, decimals and UUIDs #131 
- [Django] use an integer value for `AGENT_PORT` because Django recast strings as unicode strings, which invalidate the input for `getaddrinfo()` in Python 2.7 #140 
- [Tracer] downgrade high throughput log messages to debug so that it doesn't flood users logs #143 

**Compatibility**
- don't check if `django.contrib.auth` is installed through the `django.apps` module. This improves the best-effort support for `Django < 1.7` #136 

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.5.2...v0.5.3)

</details>
            
<details><summary>[v0.5.2](https://github.com/DataDog/dd-trace-py/releases/tag/v0.5.2) - 2016-12-14T22:24:39Z</summary>
0.5.2 is a bugfix release.

### Bug Fixes
- include bottle docs

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.5.1...v0.5.2).

</details>
            
<details><summary>[v0.5.1](https://github.com/DataDog/dd-trace-py/releases/tag/v0.5.1) - 2016-12-13T04:21:44Z</summary>
0.5.1 is a bugfix release.

### Bug Fixes
- properly trace pymongo `$in` queries (See #125)
- properly normalize bound and batch cassandra statements (see #126)
- made the legacy cassandra tracing a no-op.

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.5.0...v0.5.1).

</details>
            
<details><summary>[v0.5.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.5.0) - 2016-12-07T10:40:02Z</summary>
**Major changes**
- added`msgpack-python` as a dependency
- using Trace Agent API `v0.3` that supports both JSON and Msgpack formats
- provided `JSONEncoder` and `MsgpackEncoder` that are switched at runtime the API `v0.3` is not reachable (`404`)
- `MsgpackEncoder` is the current default encoder
- `MsgpackEncoder` will not be used if the pure Python implementation is used

**Documentation**
- added [ElasticSearch docs](http://pypi.datadoghq.com/trace/docs/#module-ddtrace.contrib.elasticsearch)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.4.0...v0.5.0)

</details>
            
<details><summary>[v0.4.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.4.0) - 2016-11-26T23:35:40Z</summary>
0.4.0 is a "major" release of the `dd-trace-py`. Please test thoroughly on staging before rolling out to your production clusters.

### Enhancements
- automatically patch contrib libraries with `from ddtrace import monkey; monkey.patch_all()`. A few notes:
  - The previous ways of patching still exist, but are deprecated and might be no-ops. They will be removed in a future version.
  - When you add `patch_all` remove your old instrumentation code.
  - Web frameworks still require middleware.
- experimental support for (much faster) msgpack serialization. disabled by default. will be enabled in a future release.

### Integrations
- add integration for the [Bottle](web framework) web framework. (see #86)

### Bug Fixes
- correctly trace django without auth middleware (see #116)

### 

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.3.16...v0.4.0).

</details>
            
<details><summary>[v0.3.16](https://github.com/DataDog/dd-trace-py/releases/tag/v0.3.16) - 2016-11-03T23:30:02Z</summary>
### Bugfixes
- Handle memory leaks when tracing happens in a forked process (Issue #84) 
- Fix error code in spans from the request library (thanks @brettlangdon)
- Better handling of unicode tags (thanks @brettlangdon)
- Allow easy configuration of host & port in the Django integration.

### Enhancements
- Cap the number of traces buffered in memory.
- Higher trace submission throughput.
- Preliminary work on gevent support. Not fully complete.

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.3.15...v0.3.16)

</details>
            
<details><summary>[v0.3.15](https://github.com/DataDog/dd-trace-py/releases/tag/v0.3.15) - 2016-11-01T01:51:56Z</summary>
### Integrations
- add tracing for the requests library

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.3.14...v0.3.15)

</details>
            
<details><summary>[0.3.14](https://github.com/DataDog/dd-trace-py/releases/tag/0.3.14) - 2016-09-30T12:39:21Z</summary>
### Integrations
- [pylons] allow users to set resources inside handlers
- [django] add support for the Django cache framework

### Enhancements
- add a trace sampler so that users can discard spans using a `RateSampler` (more info: http://pypi.datadoghq.com/trace/docs/#sampling)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.3.13...v0.3.14)

</details>
            
<details><summary>[v0.3.13](https://github.com/DataDog/dd-trace-py/releases/tag/v0.3.13) - 2016-09-21T20:53:35Z</summary>
### New integrations
- added `pylibmc` Memcached client integration
- improved Django integration providing a Django app that instrument Django internals

Read the full [changeset](https://github.com/DataDog/dd-trace-py/compare/v0.3.12...v0.3.13)

</details>
            
<details><summary>[v0.3.12](https://github.com/DataDog/dd-trace-py/releases/tag/v0.3.12) - 2016-09-14T09:26:37Z</summary>
[change set](https://github.com/DataDog/dd-trace-py/compare/v0.3.11...v0.3.12)
- Added MySQL integration, using [mysql.connector](https://dev.mysql.com/doc/connector-python/en/) v2.1

</details>
            
<details><summary>[v0.3.11](https://github.com/DataDog/dd-trace-py/releases/tag/v0.3.11) - 2016-08-31T13:29:19Z</summary>
## Bugfixes
- fixed an unpacking error for `elasticsearch>=2.4`
- fixed the behavior of the `tracer.wrap()` method; now it works as expected

## Documentation
- better organization of libraries usage on docs
- provided a [benchmark script](https://github.com/DataDog/dd-trace-py/commit/7d30c2d6703e21ea3dc94ecdeb88dbe2ad9a286a)

Read the [full changeset](https://github.com/DataDog/dd-trace-py/compare/v0.3.10...v0.3.11)

</details>
            
<details><summary>[v0.3.10](https://github.com/DataDog/dd-trace-py/releases/tag/v0.3.10) - 2016-08-22T17:03:50Z</summary>
[change set](https://github.com/DataDog/dd-trace-py/compare/v0.3.9...v0.3.10)
- add `flask_cache` integration; supporting the `0.12` and `0.13` versions
- catch `500` errors on `pylons` integration

</details>
            
<details><summary>[v0.3.9](https://github.com/DataDog/dd-trace-py/releases/tag/v0.3.9) - 2016-08-12T21:12:41Z</summary>
[change set](https://github.com/DataDog/dd-trace-py/compare/v0.3.8...v0.3.9)
- send service info from the sqlalchemy integration

</details>
            
<details><summary>[v0.3.7](https://github.com/DataDog/dd-trace-py/releases/tag/v0.3.7) - 2016-08-12T17:01:19Z</summary>
[change set](https://github.com/DataDog/dd-trace-py/compare/v0.3.6...v0.3.7)
- Released Falcon Integration
- Minor bugfixes in Redis & Cassandra integration

</details>
            
<details><summary>[v0.3.8](https://github.com/DataDog/dd-trace-py/releases/tag/v0.3.8) - 2016-08-12T17:00:35Z</summary>
[change set](https://github.com/DataDog/dd-trace-py/compare/v0.3.7...v0.3.8)
- Added support for the most recent bugfix versions of pymongo 3.0, 3.1 and 3.2

</details>
            