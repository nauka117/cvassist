from typing import Dict, Any

from cvassist.domain.exceptions import ConfigurationError
from cvassist.application.services.api_service import ApiService


class TestConnectionUseCase:

    def __init__(self, api_service: ApiService):
        self._api_service = api_service

    def execute(self) -> Dict[str, Any]:
        """Execute the test connection use case."""
        try:
            result = self._api_service.test_connection()

            return {
                "success": result.success,
                "status_code": result.status_code,
                "content": result.content,
                "error_message": result.error_message
            }
        except ConfigurationError as e:
            return {
                "success": False,
                "error_message": str(e)
            }
        except Exception as e:
            return {
                "success": False,
                "error_message": f"Unexpected error: {str(e)}"
            }
