import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    discord_token: str
    enable_message_content_intent: bool = False



def load_settings() -> Settings:
    token = os.getenv("DISCORD_TOKEN", "").strip()
    if not token:
        raise RuntimeError("DISCORD_TOKEN is required")

    raw_message_content = os.getenv("ENABLE_MESSAGE_CONTENT_INTENT", "false").strip().lower()
    enable_message_content_intent = raw_message_content in {"1", "true", "yes", "on"}

    return Settings(
        discord_token=token,
        enable_message_content_intent=enable_message_content_intent,
    )
