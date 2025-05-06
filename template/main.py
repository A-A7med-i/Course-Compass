from src.utils.helper import log_separator
from template.setup import ProjectSetup
from src.constants.constant import *
import sys


def main():
    try:
        setup = ProjectSetup()
        setup.create_structure()
        setup.logger.info(
            f"Project structure for '{PROJECT_NAME}' created successfully."
        )
    except (ValueError, OSError) as e:
        setup.logger.error(f"Failed to create project structure: {e}")
        sys.exit(1)
    except Exception as e:
        setup.logger.error(f"An unexpected error occurred: {e}")
        sys.exit(1)
    finally:
        log_separator()


if __name__ == "__main__":
    main()
