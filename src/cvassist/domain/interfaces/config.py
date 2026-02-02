"""Interface for Configuration."""

from abc import ABC, abstractmethod
from typing import Protocol

from ..entities.api_config import ApiConfig


class ConfigProvider(Protocol):
    """Abstract interface for configuration providers."""

    def get_api_config(self) -> ApiConfig:
        """Get the API configuration."""
        ...
