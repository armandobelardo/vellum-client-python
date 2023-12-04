# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...types.deployment_provider_payload_response import DeploymentProviderPayloadResponse
from ...types.deployment_read import DeploymentRead
from ...types.prompt_deployment_input_request import PromptDeploymentInputRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DeploymentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve(self, id: str) -> DeploymentRead:
        """
        Used to retrieve a deployment given its ID or name.

        Parameters:
            - id: str. Either the Deployment's ID or its unique name
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().default}/", f"v1/deployments/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeploymentRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve_provider_payload(
        self,
        *,
        deployment_id: typing.Optional[str] = OMIT,
        deployment_name: typing.Optional[str] = OMIT,
        inputs: typing.List[PromptDeploymentInputRequest],
    ) -> DeploymentProviderPayloadResponse:
        """
        Parameters:
            - deployment_id: typing.Optional[str]. The ID of the deployment. Must provide either this or deployment_name.

            - deployment_name: typing.Optional[str]. The name of the deployment. Must provide either this or deployment_id.

            - inputs: typing.List[PromptDeploymentInputRequest].
        ---
        from vellum.client import Vellum

        client = Vellum(
            api_key="YOUR_API_KEY",
        )
        client.deployments.retrieve_provider_payload(
            inputs=[],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"inputs": inputs}
        if deployment_id is not OMIT:
            _request["deployment_id"] = deployment_id
        if deployment_name is not OMIT:
            _request["deployment_name"] = deployment_name
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/", "v1/deployments/provider-payload"
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeploymentProviderPayloadResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDeploymentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve(self, id: str) -> DeploymentRead:
        """
        Used to retrieve a deployment given its ID or name.

        Parameters:
            - id: str. Either the Deployment's ID or its unique name
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_environment().default}/", f"v1/deployments/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeploymentRead, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve_provider_payload(
        self,
        *,
        deployment_id: typing.Optional[str] = OMIT,
        deployment_name: typing.Optional[str] = OMIT,
        inputs: typing.List[PromptDeploymentInputRequest],
    ) -> DeploymentProviderPayloadResponse:
        """
        Parameters:
            - deployment_id: typing.Optional[str]. The ID of the deployment. Must provide either this or deployment_name.

            - deployment_name: typing.Optional[str]. The name of the deployment. Must provide either this or deployment_id.

            - inputs: typing.List[PromptDeploymentInputRequest].
        ---
        from vellum.client import AsyncVellum

        client = AsyncVellum(
            api_key="YOUR_API_KEY",
        )
        await client.deployments.retrieve_provider_payload(
            inputs=[],
        )
        """
        _request: typing.Dict[str, typing.Any] = {"inputs": inputs}
        if deployment_id is not OMIT:
            _request["deployment_id"] = deployment_id
        if deployment_name is not OMIT:
            _request["deployment_name"] = deployment_name
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_environment().default}/", "v1/deployments/provider-payload"
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DeploymentProviderPayloadResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
