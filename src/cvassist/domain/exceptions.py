"""Domain-specific exceptions."""

from typing import Optional


class ApiConnectionError(Exception):
    """Raised when there's an error connecting to the API."""

    def __init__(self, message: str, status_code: Optional[int] = None):
        super().__init__(message)
        self.status_code = status_code


class ConfigurationError(Exception):
    """Raised when there's an error with the configuration."""
    pass
