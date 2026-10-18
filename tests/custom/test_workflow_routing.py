import httpx
import pytest

from pipedream import AsyncPipedream, Pipedream

TARGETS = [
    ("https://workflow.example.com/run?mode=test", None, "https://workflow.example.com/run?mode=test"),
    ("http://localhost:8080/run", None, "http://localhost:8080/run"),
    ("workflow.example.com/run", None, "https://workflow.example.com/run"),
    ("en123", None, "https://en123.m.pipedream.net/"),
    ("en123", "workflows.example.com", "https://en123.workflows.example.com/"),
]


@pytest.mark.parametrize("target,domain,expected", TARGETS)
@pytest.mark.parametrize("external_user", [False, True])
def test_workflow_uses_workflow_host(target: str, domain: str | None, expected: str, external_user: bool) -> None:
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"ok": True})

    with httpx.Client(transport=httpx.MockTransport(handler)) as transport:
        client = Pipedream(
            access_token="test-token",
            project_id="test",
            base_url="https://api.example.com/prefix",
            workflow_domain=domain,
            httpx_client=transport,
        )
        if external_user:
            response = client.workflows.invoke_for_external_user(target, external_user_id="user-123")
        else:
            response = client.workflows.invoke(target)

    assert response.json() == {"ok": True}
    assert len(seen) == 1
    assert str(seen[0].url) == expected
    assert seen[0].headers["authorization"] == ("Bearer test-token" if external_user else "")
    if external_user:
        assert seen[0].headers["x-pd-external-user-id"] == "user-123"


@pytest.mark.parametrize("target,domain,expected", TARGETS)
@pytest.mark.parametrize("external_user", [False, True])
async def test_async_workflow_uses_workflow_host(
    target: str, domain: str | None, expected: str, external_user: bool
) -> None:
    seen = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"ok": True})

    async with httpx.AsyncClient(transport=httpx.MockTransport(handler)) as transport:
        client = AsyncPipedream(
            access_token="test-token",
            project_id="test",
            base_url="https://api.example.com/prefix",
            workflow_domain=domain,
            httpx_client=transport,
        )
        if external_user:
            response = await client.workflows.invoke_for_external_user(target, external_user_id="user-123")
        else:
            response = await client.workflows.invoke(target)

    assert response.json() == {"ok": True}
    assert len(seen) == 1
    assert str(seen[0].url) == expected
    assert seen[0].headers["authorization"] == ("Bearer test-token" if external_user else "")
    if external_user:
        assert seen[0].headers["x-pd-external-user-id"] == "user-123"
