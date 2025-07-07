import os
from typing import (
    Literal,
    Optional,
)

from .client import (
    AsyncClient,
    Client,
)
from .environment import PipedreamEnvironment


class OAuthCredentials:

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
    ):
        self.client_id = client_id or os.getenv("PIPEDREAM_CLIENT_ID")
        self.client_secret = client_secret or os.getenv(
            "PIPEDREAM_CLIENT_SECRET")


class Pipedream(Client):

    def __init__(
        self,
        *,
        credentials: OAuthCredentials = OAuthCredentials(),
        project_id: Optional[str] = None,
        environment: Literal["production", "development"] = "production",
        api_environment: PipedreamEnvironment = PipedreamEnvironment.PROD,
        **kwargs,
    ):
        project_id = project_id or os.getenv("PIPEDREAM_PROJECT_ID")
        if not project_id:
            raise ValueError("Project ID is required")

        super().__init__(
            base_url=_get_base_url(api_environment),
            client_id=credentials.client_id,
            client_secret=credentials.client_secret,
            project_id=project_id,
            x_pd_environment=environment,
            **kwargs,
        )


class AsyncPipedream(AsyncClient):

    def __init__(
        self,
        *,
        credentials: OAuthCredentials = OAuthCredentials(),
        project_id: Optional[str] = None,
        environment: Literal["production", "development"] = "production",
        api_environment: PipedreamEnvironment = PipedreamEnvironment.PROD,
        **kwargs,
    ):
        project_id = project_id or os.getenv("PIPEDREAM_PROJECT_ID")
        if not project_id:
            raise ValueError("Project ID is required")

        super().__init__(
            base_url=_get_base_url(api_environment),
            client_id=credentials.client_id,
            client_secret=credentials.client_secret,
            project_id=project_id,
            x_pd_environment=environment,
            **kwargs,
        )


def _get_base_url(environment: PipedreamEnvironment) -> str:
    """
    Returns the base URL for the given environment.
    """
    return os.path.expandvars(environment.value)
