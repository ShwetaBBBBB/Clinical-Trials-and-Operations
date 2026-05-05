import os
from dotenv import load_dotenv
from pydantic import Field, ConfigDict
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    # LLM Configuration
    azure_openai_api_key: str = Field(alias="AZURE_OPENAI_API_KEY")
    azure_openai_endpoint: str = Field(alias="AZURE_OPENAI_ENDPOINT")
    azure_openai_deployment_name: str = Field(alias="AZURE_OPENAI_DEPLOYMENT_NAME", default="gpt-4o")
    api_version: str = Field(alias="AZURE_OPENAI_API_VERSION", default="2024-02-01")
    
    # Optional Database/Vault (for future use or cleanup)
    azure_keyvault_url: str = Field(alias="AZURE_KEYVAULT_URL", default="")
    pgsql_connection_string: str = Field(alias="PGSQLDB_CONNECTION_STRING", default="")

    model_config = ConfigDict(
        env_file=".env",
        populate_by_name=True,
        extra="ignore"
    )

settings = Settings()
