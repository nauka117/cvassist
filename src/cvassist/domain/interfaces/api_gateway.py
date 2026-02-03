"""Interface for API Gateway."""

from abc import ABC, abstractmethod
from typing import Protocol

from ..entities.api_config import ApiConfig, ApiResponse


class ApiGateway(Protocol):
    """Abstract interface for API gateway implementations."""

    def test_connection(self, config: ApiConfig) -> ApiResponse:
        """Test the API connection with the given configuration."""
        ...

    def send_prompt(self, config: ApiConfig, prompt: str) -> ApiResponse:
        """Send a prompt to the API and return the model's response."""
        ...
