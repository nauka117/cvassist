"""CLI command handlers."""

from typing import Dict, Any
from cvassist.application.use_cases.test_connection import TestConnectionUseCase
from cvassist.application.services.api_service import ApiService


class CliCommands:
    """Handler for CLI commands."""

    def __init__(self, api_service: ApiService):
        self.test_connection_use_case = TestConnectionUseCase(api_service)

    def test_connection(self):
        """Handle the test connection command."""
        return self.test_connection_use_case.execute()


def handle_result(result: Dict[str, Any]) -> int:
    """
    Handle and display the result of a command.

    Args:
        result: The result dictionary from a use case execution

    Returns:
        int: Exit code (0 for success, non-zero for failure)
    """
    if result["success"]:
        print("Well, API is working correctly.")
        if result["content"]:
            print(f"Response from API: {result['content']}")
        return 0
    else:
        print("Not well. Connection failed.")
        if result["error_message"]:
            print(f"Error: {result['error_message']}")
        if result["status_code"]:
            print(f"Status code: {result['status_code']}")
        return 1
