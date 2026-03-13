import discord
from discord.ext import commands
import logging

from src.bot.intents import build_intents
from src.bot.lifecycle import ServiceContainer, build_services
from src.commands.ping import PingCog
from src.config.settings import load_settings
from src.infra.logger import configure_logging
from src.listeners.on_ready import ReadyListener
from src.listeners.on_voice_state_update import VoiceStateListener

logger = logging.getLogger(__name__)


class CCBot(commands.Bot):
    services: ServiceContainer

    def __init__(self) -> None:
        super().__init__(command_prefix="!", intents=build_intents())
        self.services = build_services()



def build_bot() -> CCBot:
    bot = CCBot()
    bot.add_cog(PingCog(bot))
    bot.add_cog(ReadyListener(bot))
    bot.add_cog(VoiceStateListener(bot))

    loaded_prefix_commands = sorted(command.name for command in bot.commands)
    logger.info("Loaded prefix commands: %s", ", ".join(loaded_prefix_commands) or "<none>")
    return bot



def run_bot() -> None:
    configure_logging()
    settings = load_settings()
    bot = build_bot()
    bot.run(settings.discord_token)
