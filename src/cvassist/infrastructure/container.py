"""Dependency injection container for the application."""

from cvassist.application.services.api_service import ApiService
from cvassist.application.use_cases.test_connection import TestConnectionUseCase
from cvassist.infrastructure.cli.commands import CliCommands
from cvassist.infrastructure.config.env_config import EnvConfigProvider
from cvassist.infrastructure.gateways.openrouter_gateway import OpenRouterGateway


def create_application() -> CliCommands:
    """
    Creates and configures the application with all its dependencies.
    
    Returns:
        CliCommands: The configured CLI command handler.
    """
    config_provider = EnvConfigProvider()
    api_gateway = OpenRouterGateway()

    api_service = ApiService(
        api_gateway=api_gateway,
        config_provider=config_provider
    )

    return CliCommands(api_service)