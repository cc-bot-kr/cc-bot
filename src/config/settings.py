from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    discord_token: str = Field(validation_alias="DISCORD_TOKEN")
    enable_message_content_intent: bool = Field(
        default=False,
        validation_alias="ENABLE_MESSAGE_CONTENT_INTENT",
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


def load_settings() -> Settings:
    return Settings()
