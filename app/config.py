from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "sqlite:///./tasks.db"
    access_token_ttl_minutes: int = 60

    model_config = SettingsConfigDict(env_prefix="TASKS_API_")


@lru_cache
def get_settings() -> Settings:
    return Settings()
