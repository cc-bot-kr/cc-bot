from dataclasses import dataclass

from src.services.subtitle_service import SubtitleService

@dataclass
class ServiceContainer:
    subtitle_service: SubtitleService


def build_services() -> ServiceContainer:
    return ServiceContainer(subtitle_service=SubtitleService())
