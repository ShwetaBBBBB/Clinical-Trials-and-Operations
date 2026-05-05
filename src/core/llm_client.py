from langchain_openai import AzureChatOpenAI
from src.core.config import settings
from src.core.logger import logger

class LLMClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LLMClient, cls).__new__(cls)
            cls._instance._llm = None
        return cls._instance

    @property
    def llm(self) -> AzureChatOpenAI:
        if self._llm is None:
            try:
                logger.info("Initializing Azure OpenAI Chat Model...")
                self._llm = AzureChatOpenAI(
                    azure_deployment=settings.azure_openai_deployment_name,
                    api_key=settings.azure_openai_api_key,
                    azure_endpoint=settings.azure_openai_endpoint,
                    api_version=settings.api_version,
                    temperature=0
                )
                logger.info("Azure OpenAI Chat Model initialized successfully.")
            except Exception as e:
                logger.error(f"Failed to initialize LLM: {e}")
                raise
        return self._llm

llm_client = LLMClient()
