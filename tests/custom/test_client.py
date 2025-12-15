import pytest

from pipedream import AsyncPipedream, Pipedream


# Get started with writing tests with pytest at https://docs.pytest.org
@pytest.mark.skip(reason="Unimplemented")
def test_client() -> None:
    assert True


def test_pipedream_accepts_timeout_with_access_token() -> None:
    """Test that Pipedream accepts the timeout parameter with access_token."""
    client = Pipedream(
        project_id="test-project-id",
        access_token="test-token",
        timeout=5.0,
    )
    assert client._client_wrapper._timeout == 5.0


def test_pipedream_accepts_timeout_with_client_credentials() -> None:
    """Test that Pipedream accepts the timeout parameter with client credentials."""
    client = Pipedream(
        project_id="test-project-id",
        client_id="test-client-id",
        client_secret="test-client-secret",
        timeout=10.0,
    )
    assert client._client_wrapper._timeout == 10.0


def test_async_pipedream_accepts_timeout_with_access_token() -> None:
    """Test that AsyncPipedream accepts the timeout parameter with access_token."""
    client = AsyncPipedream(
        project_id="test-project-id",
        access_token="test-token",
        timeout=5.0,
    )
    assert client._client_wrapper._timeout == 5.0


def test_async_pipedream_accepts_timeout_with_client_credentials() -> None:
    """Test that AsyncPipedream accepts the timeout parameter with client credentials."""
    client = AsyncPipedream(
        project_id="test-project-id",
        client_id="test-client-id",
        client_secret="test-client-secret",
        timeout=15.0,
    )
    assert client._client_wrapper._timeout == 15.0


def test_pipedream_default_timeout() -> None:
    """Test that Pipedream uses the default timeout of 60 seconds when not specified."""
    client = Pipedream(
        project_id="test-project-id",
        access_token="test-token",
    )
    assert client._client_wrapper._timeout == 60


def test_async_pipedream_default_timeout() -> None:
    """Test that AsyncPipedream uses the default timeout of 60 seconds when not specified."""
    client = AsyncPipedream(
        project_id="test-project-id",
        access_token="test-token",
    )
    assert client._client_wrapper._timeout == 60
