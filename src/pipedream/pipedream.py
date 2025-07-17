import os
from typing import Optional

from .client import (
    AsyncClient,
    Client,
)
from .environment import PipedreamEnvironment
from .types.project_environment import ProjectEnvironment


class Pipedream(Client):

    def __init__(
        self,
        *,
        access_token: Optional[str] = os.getenv("PIPEDREAM_ACCESS_TOKEN"),
        client_id: Optional[str] = os.getenv("PIPEDREAM_CLIENT_ID"),
        client_secret: Optional[str] = os.getenv("PIPEDREAM_CLIENT_SECRET"),
        project_id: Optional[str] = os.getenv("PIPEDREAM_PROJECT_ID"),
        project_environment: ProjectEnvironment = os.getenv(
            "PIPEDREAM_PROJECT_ENVIRONMENT",
            "production",
        ),
        environment: PipedreamEnvironment = PipedreamEnvironment.PROD,
    ):
        if not project_id:
            raise ValueError("Project ID is required")

        super().__init__(
            _token_getter_override=_new_token_getter(access_token),
            base_url=_get_base_url(environment),
            client_id=client_id,
            client_secret=client_secret,
            project_id=project_id,
            project_environment=project_environment,
        )


class AsyncPipedream(AsyncClient):

    def __init__(
        self,
        *,
        access_token: Optional[str] = os.getenv("PIPEDREAM_ACCESS_TOKEN"),
        client_id: Optional[str] = os.getenv("PIPEDREAM_CLIENT_ID"),
        client_secret: Optional[str] = os.getenv("PIPEDREAM_CLIENT_SECRET"),
        project_id: Optional[str] = os.getenv("PIPEDREAM_PROJECT_ID"),
        project_environment: ProjectEnvironment = os.getenv(
            "PIPEDREAM_PROJECT_ENVIRONMENT",
            "production",
        ),
        environment: PipedreamEnvironment = PipedreamEnvironment.PROD,
    ):
        project_id = project_id
        if not project_id:
            raise ValueError("Project ID is required")

        super().__init__(
            _token_getter_override=_new_token_getter(access_token),
            base_url=_get_base_url(environment),
            client_id=client_id,
            client_secret=client_secret,
            project_id=project_id,
            project_environment=project_environment,
        )


def _get_base_url(environment: PipedreamEnvironment) -> str:
    """
    Returns the base URL for the given environment.
    """
    return os.path.expandvars(environment.value)


def _new_token_getter(access_token: Optional[str] = None):
    """
    Returns a new token getter function that retrieves the access token.
    """
    return (lambda: access_token) if access_token else None
