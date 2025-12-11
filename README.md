# Pipedream Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2FPipedreamHQ%2Fpipedream-sdk-python)
[![pypi](https://img.shields.io/pypi/v/pipedream)](https://pypi.python.org/pypi/pipedream)

The Pipedream Python library provides convenient access to the Pipedream APIs from Python.

## Table of Contents

- [Installation](#installation)
- [Reference](#reference)
- [Usage](#usage)
- [Async Client](#async-client)
- [Exception Handling](#exception-handling)
- [Pagination](#pagination)
- [Oauth Token Override](#oauth-token-override)
- [Advanced](#advanced)
  - [Access Raw Response Data](#access-raw-response-data)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Custom Client](#custom-client)
- [Contributing](#contributing)

## Installation

```sh
pip install pipedream
```

## Reference

A full reference for this library is available [here](https://github.com/PipedreamHQ/pipedream-sdk-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.actions.run(
    id="id",
    external_user_id="external_user_id",
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from pipedream import AsyncPipedream

client = AsyncPipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main() -> None:
    await client.actions.run(
        id="id",
        external_user_id="external_user_id",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from pipedream.core.api_error import ApiError

try:
    client.actions.run(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from pipedream import Pipedream

client = Pipedream(
    project_id="YOUR_PROJECT_ID",
    project_environment="YOUR_PROJECT_ENVIRONMENT",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
response = client.apps.list(
    after="after",
    before="before",
    limit=1,
    q="q",
    sort_key="name",
    sort_direction="asc",
    has_components=True,
    has_actions=True,
    has_triggers=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

```python
# You can also iterate through pages and access the typed response per page
pager = client.apps.list(...)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)
```

## Oauth Token Override

This SDK supports two authentication methods: OAuth client credentials flow (automatic token management) or direct bearer token authentication. You can choose between these options when initializing the client:

```python
from pipedream import Pipedream

# Option 1: Direct bearer token (bypass OAuth flow)
client = Pipedream(..., token="my-pre-generated-bearer-token")

from pipedream import Pipedream

# Option 2: OAuth client credentials flow (automatic token management)
client = Pipedream(
    ..., client_id="your-client-id", client_secret="your-client-secret"
)
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from pipedream import Pipedream

client = Pipedream(
    ...,
)
response = client.actions.with_raw_response.run(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object
pager = client.apps.list(...)
print(pager.response)  # access the typed response for the first page
for item in pager:
    print(item)  # access the underlying object(s)
for page in pager.iter_pages():
    print(page.response)  # access the typed response for each page
    for item in page:
        print(item)  # access the underlying object(s)
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.actions.run(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from pipedream import Pipedream

client = Pipedream(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.actions.run(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from pipedream import Pipedream

client = Pipedream(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
