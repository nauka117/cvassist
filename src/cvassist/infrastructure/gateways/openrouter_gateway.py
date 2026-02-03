"""OpenRouter API gateway code."""

import requests
from typing import Optional

from cvassist.domain.entities.api_config import ApiConfig, ApiResponse
from cvassist.domain.interfaces.api_gateway import ApiGateway
from cvassist.domain.exceptions import ApiConnectionError


class OpenRouterGateway(ApiGateway):
    """Implementation of API gateway for OpenRouter API."""

    def test_connection(self, config: ApiConfig) -> ApiResponse:
        headers = {
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": config.model,
            "messages": [{"role": "user", "content": "Hello, this is a test message."}]
        }

        try:
            response = requests.post(config.base_url, headers=headers, json=payload)

            if response.status_code == 200:
                data = response.json()
                content = None

                if "choices" in data and len(data["choices"]) > 0:
                    content = data["choices"][0]["message"]["content"]

                return ApiResponse(
                    success=True,
                    status_code=response.status_code,
                    content=content
                )
            else:
                return ApiResponse(
                    success=False,
                    status_code=response.status_code,
                    error_message=response.text
                )

        except requests.exceptions.RequestException as e:
            return ApiResponse(
                success=False,
                error_message=f"Request failed: {str(e)}"
            )

        except Exception as e:
            return ApiResponse(
                success=False,
                error_message=f"Unexpected error: {str(e)}"
            )

    def send_prompt(self, config: ApiConfig, prompt: str) -> ApiResponse:
        """Send a prompt to the OpenRouter API and return the model's response."""
        headers = {
            "Authorization": f"Bearer {config.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": config.model,
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(config.base_url, headers=headers, json=payload)

            if response.status_code == 200:
                data = response.json()
                content = None

                if "choices" in data and len(data["choices"]) > 0:
                    content = data["choices"][0]["message"]["content"]

                return ApiResponse(
                    success=True,
                    status_code=response.status_code,
                    content=content
                )
            else:
                return ApiResponse(
                    success=False,
                    status_code=response.status_code,
                    error_message=response.text
                )

        except requests.exceptions.RequestException as e:
            return ApiResponse(
                success=False,
                error_message=f"Request failed: {str(e)}"
            )

        except Exception as e:
            return ApiResponse(
                success=False,
                error_message=f"Unexpected error: {str(e)}"
            )
