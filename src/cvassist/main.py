import sys
from typing import NoReturn

from cvassist.domain.exceptions import ConfigurationError
from cvassist.infrastructure.container import create_application
from cvassist.infrastructure.cli.commands import handle_result


def main() -> int:
    try:
        print("Testing OpenRouter API connection...")

        cli_commands = create_application()
        result = cli_commands.test_connection()

        return handle_result(result)

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
