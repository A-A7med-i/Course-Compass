from src.constants.constant import LOG_DIR, LOG_FILE
from typing import Dict, Any
from src import logger
import yaml
import os


def log_separator(
    message: str = "NEW RUN STARTED", width: int = 100, separator_char: str = "-"
) -> None:
    """
    Prints a separator line to the log file to clearly mark the start of a new run.

    Args:
        message (str): The message to display in the center of the separator.
        width (int): The total width of the separator line.
        separator_char (str): The character to use for the separator line.

    Returns:
        None
    """
    separator_line = message.center(width, separator_char)
    log_file_path = os.path.join(LOG_DIR, LOG_FILE)

    with open(log_file_path, "a") as file:
        file.write(f"{separator_line}\n")


def load_yaml_config(file_path: str) -> Dict[str, Any]:
    """
    Load and parse a YAML configuration file.

    Args:
        file_path (str): Path to the YAML configuration file.

    Returns:
        Dict[str, Any]: Parsed YAML content as a dictionary.

    Raises:
        FileNotFoundError: If the configuration file doesn't exist.
        yaml.YAMLError: If the file contains invalid YAML syntax.
        PermissionError: If the file cannot be accessed due to permission issues.
        Exception: For any other unexpected errors during file loading.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as config_file:
            return yaml.safe_load(config_file)

    except FileNotFoundError:
        logger.error(f"Configuration file not found at: {file_path}")
        raise FileNotFoundError(f"Configuration file not found at: {file_path}")

    except yaml.YAMLError as yaml_error:
        logger.error(f"Error parsing YAML file at {file_path}: {str(yaml_error)}")
        raise yaml.YAMLError(
            f"Invalid YAML syntax in file: {file_path}. Error: {str(yaml_error)}"
        )

    except PermissionError as permission_error:
        logger.error(
            f"Permission denied when accessing file at {file_path}: {str(permission_error)}"
        )
        raise PermissionError(
            f"Cannot access file at {file_path} due to permission issues."
        )

    except Exception as unexpected_error:
        logger.exception(f"Unexpected error loading YAML file from {file_path}")
        raise Exception(
            f"Failed to load YAML file from {file_path}: {str(unexpected_error)}"
        )
