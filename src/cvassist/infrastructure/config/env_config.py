"""Environment-based configuration provider."""

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

from cvassist.domain.entities.api_config import ApiConfig
from cvassist.domain.interfaces.config import ConfigProvider
from cvassist.domain.exceptions import ConfigurationError


class EnvConfigProvider(ConfigProvider):
    """Configuration provider that loads settings from environment variables."""

    def __init__(
        self,
        api_key_env_var: str = "OPENROUTER_API_KEY",
        base_url: str = "https://openrouter.ai/api/v1/chat/completions",
        model: str = "openai/gpt-3.5-turbo"
    ):
        self.api_key_env_var = api_key_env_var
        self.base_url = base_url
        self.model = model

    def get_api_config(self) -> ApiConfig:
        """Get the API configuration from environment variables."""
        api_key = os.getenv(self.api_key_env_var)

        if not api_key:
            raise ConfigurationError(
                f"{self.api_key_env_var} environment variable not set."
            )

        return ApiConfig(
            api_key=api_key,
            base_url=self.base_url,
            model=self.model
        )
