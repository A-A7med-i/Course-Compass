from src.constants.constant import TASK_CONFIG_PATH
from src.utils.helper import load_yaml_config
from src.utils.helper import log_separator
from typing import Dict, List, Optional
from crewai import Task
from src import logger


class TaskManager:
    """
    A class for managing and creating tasks based on a configuration file.

    This class handles loading task configurations, creating Task objects,
    and providing access to available task types and configurations.

    Attributes:
        _task_configs (Dict[str, Dict[str, str]]): A dictionary containing task configurations,
            loaded from the TASK_CONFIG_PATH.
    """

    def __init__(self):
        """
        Initializes the Tasks object by loading the task configuration.
        """
        self._task_configs = load_yaml_config(TASK_CONFIG_PATH)

    def create_task(
        self,
        task_type: str,
        agent,
        output_file: Optional[str],
        output_json: Optional[bool] = None,
    ) -> Task:
        """
        Creates a Task object based on the specified task type and configuration.

        Args:
            task_type (str): The type of task to create.  This should correspond to a key
                in the task configuration loaded from TASK_CONFIG_PATH.
            output_json (Optional[bool]):  Whether the task should output JSON.
            output_file (Optional[str]): The file to write the task output to.
            agent (Agent): The agent to assign the task to.

        Returns:
            Task: The created Task object.

        Raises:
            ValueError: If the task configuration is not found for the given task_type.
            Exception: If any error occurs during task creation.
        """
        task_config = self._task_configs.get(task_type)

        if not task_config:
            raise ValueError(f"Task configuration not found for type: {task_type}")

        try:
            task = Task(
                description=task_config["description"],
                expected_output=task_config["expected_output"],
                output_json=output_json,
                output_file=output_file,
                agent=agent,
            )

            logger.info(f"Task of type '{task_type}' created successfully")
            return task

        except ValueError as ve:
            logger.error(str(ve))
            raise

        except Exception as e:
            logger.error(f"Task creation failed for type '{task_type}': {str(e)}")
            raise

        finally:
            log_separator()

    def get_available_task_types(self) -> List[str]:
        """
        Retrieves a list of available task types from the configuration.

        Returns:
            List[str]: A list of strings, where each string is a task type.
        """
        return list(self._task_configs.keys())

    def get_task_config(self, task_type: str) -> Optional[Dict[str, str]]:
        """
        Retrieves the configuration for a specific task type.

        Args:
            task_type (str): The type of the task to retrieve the configuration for.

        Returns:
            Optional[Dict[str, str]]: A dictionary containing the task configuration,
                or None if the task type is not found.
        """
        return self._task_configs.get(task_type)
