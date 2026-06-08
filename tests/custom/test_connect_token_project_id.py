"""When authenticating with a Connect token, callers may omit the project ID
(the backend derives it from the token). The wrapper keeps project_id="" and
normalizes the resulting "/v1/connect//..." path down to "/v1/connect/...".
"""

import asyncio

import httpx
import pytest

from pipedream import AsyncPipedream, Pipedream

_ACCOUNTS_BODY: dict = {"data": [], "page_info": {}}


def _capturing_sync_client(seen: list) -> httpx.Client:

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        return httpx.Response(200, json=_ACCOUNTS_BODY)

    return httpx.Client(transport=httpx.MockTransport(handler))


def _capturing_async_client(seen: list) -> httpx.AsyncClient:

    async def handler(request: httpx.Request) -> httpx.Response:
        seen.append(str(request.url))
        return httpx.Response(200, json=_ACCOUNTS_BODY)

    return httpx.AsyncClient(transport=httpx.MockTransport(handler))


def test_token_auth_without_project_id_collapses_connect_path() -> None:
    seen: list = []
    client = Pipedream(
        access_token="ctok",
        project_id=None,
        base_url="https://api.example.com",
        httpx_client=_capturing_sync_client(seen),
    )

    client.accounts.list()

    assert seen, "expected a request to be made"
    assert "/v1/connect/accounts" in seen[0]
    assert "/v1/connect//accounts" not in seen[0]


def test_token_auth_async_without_project_id_collapses_connect_path() -> None:
    seen: list = []

    async def run() -> None:
        client = AsyncPipedream(
            access_token="ctok",
            project_id=None,
            base_url="https://api.example.com",
            httpx_client=_capturing_async_client(seen),
        )
        await client.accounts.list()

    asyncio.run(run())

    assert seen, "expected a request to be made"
    assert "/v1/connect/accounts" in seen[0]
    assert "/v1/connect//accounts" not in seen[0]


def test_explicit_project_id_is_preserved() -> None:
    seen: list = []
    client = Pipedream(
        access_token="ctok",
        project_id="p_explicit",
        base_url="https://api.example.com",
        httpx_client=_capturing_sync_client(seen),
    )

    client.accounts.list()

    assert seen
    assert "/v1/connect/p_explicit/accounts" in seen[0]
