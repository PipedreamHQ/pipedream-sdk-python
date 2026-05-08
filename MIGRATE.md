# Migrating from v1.x

This guide will help you migrate your existing Pipedream Python SDK v1.x
integration to the latest version.

## Table of contents

- [Migrating from v1.x](#migrating-from-v1x)
  - [Table of contents](#table-of-contents)
  - [Deprecation](#deprecation)
  - [Breaking changes](#breaking-changes)
  - [Python version requirement](#python-version-requirement)
  - [Removed types](#removed-types)
    - [`ConfigurableProp_*` discriminator aliases](#configurableprop_-discriminator-aliases)
    - [`Emitter_*` discriminator aliases](#emitter_-discriminator-aliases)
    - [`ConfigurablePropDiscord`](#configurablepropdiscord)
    - [`SyncCustomPager` / `AsyncCustomPager`](#synccustompager--asynccustompager)
  - [Retry behavior change](#retry-behavior-change)
  - [Client initialization](#client-initialization)
  - [New features in v2.x](#new-features-in-v2x)
    - [aiohttp transport](#aiohttp-transport)
    - [Structured logging](#structured-logging)
    - [Expanded constructor parameters](#expanded-constructor-parameters)
    - [Additional type and namespace exports](#additional-type-and-namespace-exports)
  - [Important removed functionality](#important-removed-functionality)
  - [Migration checklist](#migration-checklist)

## Deprecation

The v1.x version of the Pipedream Python SDK is now deprecated. This means that
no changes will be made to this version unless there are critical security
issues. We recommend that you migrate to the latest version of the SDK to take
advantage of new features, improvements, and bug fixes if possible.

## Breaking changes

The new SDK version introduces a small number of breaking changes that you need
to be aware of when migrating from v1.x. The public, namespaced API (e.g.,
`client.actions.run(...)`, `client.proxy.get(...)`,
`client.workflows.invoke(...)`) is **unchanged** between v1.x and v2.x — most
application code that uses the `Pipedream` / `AsyncPipedream` wrapper will
continue to work as-is. The breaks are concentrated in three areas:

- **Python `>= 3.10` is now required.** Python 3.8 and 3.9 are no longer
  supported.
- **Removed type aliases.** The `ConfigurableProp_*` and `Emitter_*`
  discriminator-style aliases have been removed. The `ConfigurablePropDiscord`
  root type has also been removed.
- **Removed pagination types.** `SyncCustomPager` and `AsyncCustomPager` have
  been removed from `pipedream.core`. Use `SyncPager` / `AsyncPager` instead.
- **Default retry status codes expanded.** `409 Conflict` is now retried by
  default in addition to `408`, `429`, and `5xx`. Mutating calls may need
  `max_retries=0` to avoid duplicate side effects.
- **`pydantic-core` upper-bounded to `< 3.0.0`.** If you previously pinned a
  `pydantic-core` 3.x pre-release, update your constraint.

## Python version requirement

The minimum supported Python version is now **3.10**. Python 3.8 and 3.9 are no
longer supported. The package metadata reflects this:

```toml
# pyproject.toml
[tool.poetry.dependencies]
python = "^3.10"
```

If you are still on Python 3.8 or 3.9, upgrade your runtime before installing
v2.x.

## Removed types

### `ConfigurableProp_*` discriminator aliases

The 22 `ConfigurableProp_*` aliases (e.g., `ConfigurableProp_Alert`,
`ConfigurableProp_String`, `ConfigurableProp_Integer`, …) have been removed. The
un-prefixed variants — which were always exported alongside the aliases — remain
and are now the canonical names.

```python
# v1.x (old)
from pipedream import (
    ConfigurableProp_Alert,
    ConfigurableProp_Integer,
    ConfigurableProp_String,
)

# v2.x (new)
from pipedream import (
    ConfigurablePropAlert,
    ConfigurablePropInteger,
    ConfigurablePropString,
)
```

The full list of removed aliases:

`ConfigurableProp_AirtableBaseId`, `ConfigurableProp_AirtableFieldId`,
`ConfigurableProp_AirtableTableId`, `ConfigurableProp_AirtableViewId`,
`ConfigurableProp_Alert`, `ConfigurableProp_Any`, `ConfigurableProp_App`,
`ConfigurableProp_Boolean`, `ConfigurableProp_DataStore`,
`ConfigurableProp_Dir`, `ConfigurableProp_DiscordChannel`,
`ConfigurableProp_DiscordChannelArray`, `ConfigurableProp_HttpRequest`,
`ConfigurableProp_Integer`, `ConfigurableProp_IntegerArray`,
`ConfigurableProp_InterfaceApphook`, `ConfigurableProp_InterfaceHttp`,
`ConfigurableProp_InterfaceTimer`, `ConfigurableProp_Object`,
`ConfigurableProp_ServiceDb`, `ConfigurableProp_Sql`, `ConfigurableProp_String`,
`ConfigurableProp_StringArray`.

For each, drop the underscore and use the un-prefixed name (e.g.,
`ConfigurableProp_AirtableBaseId` → `ConfigurablePropAirtableBaseId`).

### `Emitter_*` discriminator aliases

The `Emitter_*` aliases have been removed. The `Emitter` union itself is still
exported, but it now references the underlying types directly:

```python
# v1.x (old)
from pipedream import (
    Emitter,
    Emitter_DeployedComponent,
    Emitter_HttpInterface,
    Emitter_TimerInterface,
)

# v2.x (new)
from pipedream import (
    Emitter,            # still exported
    DeployedComponent,
    HttpInterface,
    TimerInterface,
)
# Emitter is now: typing.Union[DeployedComponent, HttpInterface, TimerInterface]
```

If you were pattern-matching on `Emitter_*` types, switch to matching on
`DeployedComponent` / `HttpInterface` / `TimerInterface` directly.

### `ConfigurablePropDiscord`

The root `ConfigurablePropDiscord` type (representing `type ==
"$.discord.channel"` at the top level) has been removed. The related types
`ConfigurablePropDiscordChannel` and `ConfigurablePropDiscordChannelArray` are
unchanged.

```python
# v1.x (old)
from pipedream import ConfigurablePropDiscord

# v2.x (new)
from pipedream import (
    ConfigurablePropDiscordChannel,
    ConfigurablePropDiscordChannelArray,
)
```

### `SyncCustomPager` / `AsyncCustomPager`

The custom pager classes have been removed from `pipedream.core`. The standard
`SyncPager` and `AsyncPager` classes (also exported from `pipedream.core`) are
now used for every paginated endpoint. The iteration interface is unchanged.

```python
# v1.x (old)
from pipedream.core import SyncCustomPager, AsyncCustomPager

# v2.x (new)
from pipedream.core import SyncPager, AsyncPager
```

If you only iterated over paginated responses (e.g., `for app in
client.apps.list(...): ...`) and did not import the pager type directly, no
change is required.

## Retry behavior change

The set of HTTP status codes that the SDK retries by default has been expanded.
This is a runtime behavior change that does not surface in your type checker, so
it is worth calling out explicitly.

| Version | Retried status codes       |
| ------- | -------------------------- |
| v1.x    | `408`, `429`, `5xx`        |
| v2.x    | `408`, `409`, `429`, `5xx` |

The retry limit (`max_retries=2`) is unchanged. The new behavior matters for
**mutating** calls — proxy `POST` / `PUT` / `PATCH` / `DELETE`, action runs
(`client.actions.run`), trigger deploys (`client.triggers.deploy`),
deployed-trigger updates, and so on — where retrying a `409 Conflict` response
can produce duplicate side effects on the downstream system.

To opt out of retries on a specific call or globally, set `max_retries=0`:

```python
from pipedream import Pipedream
from pipedream.core import RequestOptions

# Globally: never retry
client = Pipedream(
    project_id="...",
    client_id="...",
    client_secret="...",
    max_retries=0,
)

# Per-request: never retry this one mutation
client.proxy.post(
    url="https://api.example.com/orders",
    external_user_id="external_user_id",
    account_id="account_id",
    body={"sku": "ABC"},
    request_options=RequestOptions(max_retries=0),
)
```

## Client initialization

The `Pipedream` and `AsyncPipedream` constructor signatures in v2.x are a
**strict superset** of v1.x. Existing initialization code continues to work
unchanged.

```python
# v1.x — still works in v2.x without modification
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

client.actions.run(
    id="gitlab-list-commits",
    external_user_id="external_user_id",
    configured_props={
        "gitlab": {"authProvisionId": "apn_kVh9AoD"},
        "projectId": 45672541,
        "refName": "main",
    },
)
```

v2.x adds new optional keyword arguments to the wrapper constructor — `headers`,
`max_retries`, `follow_redirects`, `httpx_client`, and `logging`. These
previously required dropping down to the underlying generated `Client` /
`AsyncClient`:

```python
# v2.x — new optional kwargs available directly on the wrapper
import httpx

from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    headers={"X-My-Custom-Header": "value"},
    max_retries=0,
    follow_redirects=True,
    httpx_client=httpx.Client(timeout=30.0),
    logging={"level": "info"},
)
```

Environment-variable-driven configuration is unchanged from v1.x.
`PIPEDREAM_ACCESS_TOKEN`, `PIPEDREAM_CLIENT_ID`, `PIPEDREAM_CLIENT_SECRET`,
`PIPEDREAM_PROJECT_ID`, `PIPEDREAM_PROJECT_ENVIRONMENT`, `PIPEDREAM_BASE_URL`,
and `PIPEDREAM_WORKFLOW_DOMAIN` continue to be picked up automatically.

## New features in v2.x

### aiohttp transport

You can now opt into an aiohttp-backed async transport by installing the
`aiohttp` extra:

```bash
pip install 'pipedream[aiohttp]'
```

When `httpx-aiohttp` is installed, `AsyncPipedream` automatically uses it for
the underlying transport. No code change is required — the SDK detects the
optional dependency at construction time. If `httpx-aiohttp` is not installed,
the default `httpx.AsyncClient` continues to be used.

### Structured logging

v2.x adds an optional `logging=` parameter to the wrapper constructors. You can
pass either a `LogConfig` dictionary or a fully-constructed `Logger` instance.

```python
from pipedream import Pipedream

# Simplest: pass a LogConfig dict
client = Pipedream(
    project_id="...",
    client_id="...",
    client_secret="...",
    logging={"level": "debug"},  # "debug" | "info" | "warn" | "error"
)
```

For more control — including plugging in your own logger that conforms to the
`ILogger` protocol — use the lower-level building blocks from `pipedream.core`:

```python
from pipedream import Pipedream
from pipedream.core import ConsoleLogger, Logger

custom_logger = Logger(level="info", logger=ConsoleLogger(), silent=False)

client = Pipedream(
    project_id="...",
    client_id="...",
    client_secret="...",
    logging=custom_logger,
)
```

The full set of new logging exports from `pipedream.core` is: `LogConfig`,
`LogLevel`, `Logger`, `ILogger`, `ConsoleLogger`, and `create_logger`.

### Expanded constructor parameters

In addition to `logging`, the wrapper constructors gained four new optional
kwargs in v2.x:

- `headers` — additional HTTP headers to send with every request.
- `max_retries` — overrides the default retry limit (default: `2`). Set to `0`
  to disable retries entirely.
- `follow_redirects` — controls whether the default httpx client follows
  redirects (default: `True`).
- `httpx_client` — pass your own pre-configured `httpx.Client` /
  `httpx.AsyncClient` if you need custom transport, proxy, or middleware
  behavior.

In v1.x these were only reachable by instantiating the underlying generated
`Client` / `AsyncClient` directly.

### Additional type and namespace exports

`WorkflowsClient` and `AsyncWorkflowsClient` are now exported from the package
root, so you no longer need to reach into the submodule:

```python
# v1.x (old)
from pipedream.workflows.client import WorkflowsClient

# v2.x (new) — both still work
from pipedream import WorkflowsClient
```

A number of types that correspond to existing v1 endpoints are now surfaced at
the package root for direct import:

- `AccountCredentials`
- `ConnectUsage`, `ConnectUsageResponse`
- `ExternalUser`, `GetUsersResponse`
- `Webhook`, `WebhookWithSigningKey`, `WebhookWithOptionalSigningKey`,
  `TriggerWebhook`
- `GetWebhookResponse`, `GetWebhookWithSigningKeyResponse`, `SetWebhookResponse`
- `ConfigurablePropBaseType`, `ConfigurablePropDirAccessMode`,
  `ConfigurablePropStringFormat`

The endpoints that produce these values (`client.usage.*`,
`client.users.list(...)`, the `client.deployed_triggers` webhook operations,
etc.) already existed in late v1.x — only the type exports are new in v2.x.

`pipedream.core` also gains `ParsingError` (raised when a server response fails
to validate against its expected shape), `encode_path_param`, `Rfc2822DateTime`,
and `parse_rfc2822_datetime`.

## Important removed functionality

The following has been removed in v2.x and has no v1.x-style replacement:

1. **`ConfigurableProp_*` discriminator aliases** — use the un-prefixed variants
   (e.g., `ConfigurablePropString`).
2. **`Emitter_*` discriminator aliases** — use `DeployedComponent`,
   `HttpInterface`, `TimerInterface` directly. The `Emitter` union itself
   remains.
3. **`ConfigurablePropDiscord`** — removed entirely. The related
   `ConfigurablePropDiscordChannel` and `ConfigurablePropDiscordChannelArray`
   types are unchanged.
4. **`SyncCustomPager` / `AsyncCustomPager`** — use `SyncPager` / `AsyncPager`
   from `pipedream.core`.

## Migration checklist

- [ ] Confirm your runtime is on Python 3.10 or newer.
- [ ] Replace any imports of `ConfigurableProp_*`, `Emitter_*`,
  `ConfigurablePropDiscord`, `SyncCustomPager`, or `AsyncCustomPager` with their
  v2.x equivalents.
- [ ] Audit mutating calls (`client.proxy.post` / `put` / `patch` / `delete`,
  `client.actions.run`, `client.triggers.deploy`,
  `client.deployed_triggers.update`, …) and decide whether retrying on `409
  Conflict` is safe. Pass `max_retries=0` (per-client or per-request) where it
  isn't.
- [ ] If you previously pinned `pydantic-core` to a `3.x` pre-release, update
  the constraint to satisfy `< 3.0.0`.
- [ ] (Optional) Install `pipedream[aiohttp]` if you want the aiohttp transport
  for async workloads.
- [ ] (Optional) Wire up the new `logging=` parameter if you want SDK-level
  structured logs.
- [ ] Run your test suite against v2.x.
