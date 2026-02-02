"""API Configuration entity."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ApiConfig:
    """Configuration for API connections."""

    api_key: str
    base_url: str
    model: str = "openai/gpt-3.5-turbo"

    def __post_init__(self):
        """Validate the API configuration."""
        if not self.api_key:
            raise ValueError("API key cannot be empty")
        if not self.base_url:
            raise ValueError("Base URL cannot be empty")


@dataclass
class ApiResponse:
    """Response from API calls."""

    success: bool
    status_code: Optional[int] = None
    content: Optional[str] = None
    error_message: Optional[str] = None
