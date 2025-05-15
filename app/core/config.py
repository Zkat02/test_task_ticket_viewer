from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@localhost:5435/postgres"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()