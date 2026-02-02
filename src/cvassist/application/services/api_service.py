from typing import Protocol

from cvassist.domain.entities.api_config import ApiConfig, ApiResponse
from cvassist.domain.interfaces.api_gateway import ApiGateway
from cvassist.domain.interfaces.config import ConfigProvider


class ApiService:
    """Service for handling API operations."""

    def __init__(self, api_gateway: ApiGateway, config_provider: ConfigProvider):
        self._api_gateway = api_gateway
        self._config_provider = config_provider

    def test_connection(self) -> ApiResponse:
        """Test the API connection."""
        config = self._config_provider.get_api_config()
        return self._api_gateway.test_connection(config)
