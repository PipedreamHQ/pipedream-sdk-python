import os
from string import Template

from .client import (
    AsyncClient,
    Client,
)
from .environment import PipedreamEnvironment


class Pipedream(Client):
    def __init__(
        self,
        project_id: str,
        environment: PipedreamEnvironment = PipedreamEnvironment.PROD,
        *args,
        **kwargs,
    ):
        super().__init__(base_url=_get_base_url(environment), *args, **kwargs)
        self.project_id = project_id


class AsyncPipedream(AsyncClient):
    def __init__(
        self,
        project_id: str,
        environment: PipedreamEnvironment = PipedreamEnvironment.PROD,
        *args,
        **kwargs,
    ):
        super().__init__(base_url=_get_base_url(environment), *args, **kwargs)
        self.project_id = project_id


def _get_base_url(environment: PipedreamEnvironment) -> str:
    if not environment:
        raise Exception("Please pass environment to construct the client")

    user = os.getenv("DEV_NAMESPACE", "")
    return Template(environment.value).substitute(
        {
            "user": user,
        }
    )
