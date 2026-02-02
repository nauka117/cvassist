import sys
from typing import NoReturn

from cvassist.application.services.api_service import ApiService
from cvassist.domain.exceptions import ConfigurationError
from cvassist.infrastructure.cli.commands import CliCommands
from cvassist.infrastructure.config.env_config import EnvConfigProvider
from cvassist.infrastructure.gateways.openrouter_gateway import OpenRouterGateway


def main() -> int:
    try:

        config_provider = EnvConfigProvider()
        api_gateway = OpenRouterGateway()

        api_service = ApiService(
            api_gateway=api_gateway,
            config_provider=config_provider
        )

        cli_commands = CliCommands(api_service)

        print("Testing OpenRouter API connection...")
        result = cli_commands.test_connection()

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

    except ConfigurationError as e:
        print(f"Configuration error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        return 130
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
