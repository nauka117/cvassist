"""Use case for sending prompts to the OpenRouter API."""

from typing import Dict, Any

from cvassist.application.services.api_service import ApiService


class SendPromptUseCase:
    """Use case for sending prompts to the API and getting model responses."""

    def __init__(self, api_service: ApiService):
        self._api_service = api_service

    def execute(self, prompt: str) -> Dict[str, Any]:
        """
        Execute the use case to send a prompt to the API.

        Args:
            prompt: The prompt to send to the API

        Returns:
            Dictionary containing the result of the API call
        """
        response = self._api_service.send_prompt(prompt)

        return {
            "success": response.success,
            "content": response.content,
            "status_code": response.status_code,
            "error_message": response.error_message
        }