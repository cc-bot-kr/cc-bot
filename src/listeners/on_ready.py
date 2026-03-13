import logging

from discord.ext import commands
from discord.ext.commands import CommandNotFound

logger = logging.getLogger(__name__)


class ReadyListener(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        if self.bot.user:
            logger.info("Bot connected as %s", self.bot.user)

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError) -> None:
        if isinstance(error, CommandNotFound):
            await ctx.reply("알 수 없는 명령어입니다. `!ping` 또는 `/ping`을 사용해보세요.", mention_author=False)
            return

        logger.exception("Unhandled command error", exc_info=error)
