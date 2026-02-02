"""CLI command handlers."""

from cvassist.application.use_cases.test_connection import TestConnectionUseCase
from cvassist.application.services.api_service import ApiService


class CliCommands:
    """Handler for CLI commands."""

    def __init__(self, api_service: ApiService):
        self.test_connection_use_case = TestConnectionUseCase(api_service)

    def test_connection(self):
        """Handle the test connection command."""
        return self.test_connection_use_case.execute()
