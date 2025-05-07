from src.constants.constant import AGENT_CONFIG_PATH
from src.utils.helper import load_yaml_config
from crewai.tools.base_tool import BaseTool
from src.utils.helper import log_separator
from typing import List, Optional, Dict
from src.llm.model import LLMModel
from crewai import Agent
from src import logger


class AgentFactory:
    """
    A factory class for creating specialized AI agents.

    This factory handles the creation of different types of agents based on
    configurations defined in the application's config file. It manages the
    initialization of agents with appropriate roles, goals, backstories,
    and tools.

    Attributes:
        config (Dict[str, Dict[str, str]]): Configuration dictionary containing agent specifications.
        llm (LLMModel): Language model instance used by the agents.
        tools (Optional[List[Any]]): Optional tools that agents can use to perform tasks.
    """

    def __init__(self) -> None:
        """
        Initialize the AgentFactory with configuration and language model.

        Raises:
            Exception: If initialization fails due to configuration loading or LLM initialization.
        """

        try:
            self._agent_configs = load_yaml_config(AGENT_CONFIG_PATH)
            self._llm_model = LLMModel()
            logger.info("Agent factory initialized successfully")

        except Exception as e:
            logger.error(f"Failed to initialize Agent: {str(e)}")
            raise

    def create_agent(
        self, agent_type: str, tools: Optional[List[BaseTool]] = None
    ) -> Agent:
        """
        Create an agent of the specified type based on configuration.

        Args:
            agent_type (str): The type of agent to create. Must correspond to a key in the configuration loaded from CONFIG_PATH.
            tools (Optional[List[BaseTool]]): Optional list of tools that can be provided to agents.
                                        Defaults to None.

        Returns:
            Agent: The configured agent instance.

        Raises:
            ValueError: If the specified agent_type is not found in the configuration.
            Exception: If agent creation fails for any other reason.
        """
        try:
            agent_config = self._agent_configs.get(agent_type)

            if not agent_config:
                raise ValueError(
                    f"Agent configuration not found for type: {agent_type}"
                )

            agent = Agent(
                role=agent_config["role"],
                goal=agent_config["goal"],
                backstory=agent_config["backstory"],
                llm=self._llm_model,
                tools=tools if tools else [],
                verbose=True,
            )

            logger.info(f"Agent of type '{agent_type}' created successfully")
            return agent

        except ValueError as ve:
            logger.error(str(ve))
            raise

        except Exception as e:
            logger.error(f"Agent creation failed for type '{agent_type}': {str(e)}")
            raise

        finally:
            log_separator()

    def get_available_agent_types(self) -> List[str]:
        """
        Returns a list of available agent types defined in the configuration.

        Returns:
            List[str]: A list of agent type names (keys in the configuration).
        """
        return list(self._agent_configs.keys())

    def get_agent_config(self, agent_type: str) -> Optional[Dict[str, str]]:
        """
        Retrieves the configuration for a specific agent type.

        Args:
            agent_type (str): The type of agent to retrieve the configuration for.

        Returns:
            Optional[Dict[str, str]]: A dictionary containing the configuration for the specified agent type,
                                    or None if the agent type is not found.
        """

        return self._agent_configs.get(agent_type)
