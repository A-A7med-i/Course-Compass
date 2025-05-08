from src.constants.constant import MODEL_NAME, TEMPERATURE, GROQ_API_KEY
from src.utils.helper import log_separator
from typing import Optional
from crewai import LLM
from src import logger


class LLMModel(LLM):
    """
    A wrapper class for interacting with language models via litellm.
    Provides a simplified interface for generating responses from LLMs.

    Attributes:
        model_name (str): The identifier of the language model to use.
        temperature (float): Controls randomness in responses (0.0 to 1.0).
        api_key (str): The API key for authenticating with the LLM service.
    """

    def __init__(
        self,
        model_name: Optional[str] = None,
        temperature: Optional[float] = None,
        api_key: Optional[str] = None,
    ) -> None:
        """
        Initialize the LLM model with specific configuration.

        Args:
            model_name (Optional[str]): The identifier of the language model to use.
            temperature (Optional[float]): Controls randomness in responses (0.0 to 1.0).
            api_key (Optional[str]): The API key for authenticating with the LLM service.

        Raises:
            ValueError: If the API key is not provided.
            RuntimeError: If initialization of the LLM fails.
        """
        self.model_name = model_name or MODEL_NAME
        self.temperature = temperature or TEMPERATURE
        self.api_key = api_key or GROQ_API_KEY

        if not self.api_key:
            logger.error("No API key provided for LLM. Please set GROQ_API_KEY.")
            raise ValueError("API key is required for LLM initialization")

        logger.info(
            f"Initializing LLMModel with model_name={self.model_name}, "
            f"temperature={self.temperature}"
        )
        try:
            super().__init__(
                api_key=self.api_key,
                temperature=self.temperature,
                model=self.model_name,
            )
            logger.debug("LLM initialization successful")

        except Exception as e:
            logger.exception("Failed to initialize LLM")
            raise RuntimeError("LLM initialization failed") from e

        finally:
            log_separator()
