from unittest.mock import AsyncMock

import pytest

from pipedream import AsyncPipedream, Pipedream


# Get started with writing tests with pytest at https://docs.pytest.org
@pytest.mark.skip(reason="Unimplemented")
def test_client() -> None:
    assert True


def test_sync_pipedream_raw_access_token() -> None:
    """Test synchronous Pipedream client raw_access_token property."""
    client = Pipedream(access_token="test-token", project_id="test-project")
    assert client.raw_access_token == "test-token"


def test_async_pipedream_raw_access_token() -> None:
    """Test AsyncPipedream client raw_access_token property with access_token."""
    client = AsyncPipedream(access_token="test-token", project_id="test-project")
    assert client.raw_access_token == "test-token"


async def test_async_pipedream_get_raw_access_token() -> None:
    """Test AsyncPipedream async method get_raw_access_token() with access_token."""
    client = AsyncPipedream(access_token="test-token", project_id="test-project")
    token = await client.get_raw_access_token()
    assert token == "test-token"


async def test_async_pipedream_get_raw_access_token_with_oauth() -> None:
    """Test AsyncPipedream async method with OAuth flow."""
    client = AsyncPipedream(
        client_id="test-client-id",
        client_secret="test-client-secret",
        project_id="test-project",
    )

    # The client should have _async_token set when using OAuth
    assert client._client_wrapper._async_token is not None

    # Mock the async token provider
    client._client_wrapper._async_token = AsyncMock(return_value="mocked-oauth-token")

    # Test the async method
    token = await client.get_raw_access_token()
    assert token == "mocked-oauth-token"
