import logging

import discord
from discord.ext import commands

logger = logging.getLogger(__name__)


class VoiceStateListener(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(
        self,
        member: discord.Member,
        before: discord.VoiceState,
        after: discord.VoiceState,
    ) -> None:
        if before.channel == after.channel:
            return

        if after.channel is not None:
            logger.info("%s joined voice channel %s", member.display_name, after.channel.id)
        elif before.channel is not None:
            logger.info("%s left voice channel %s", member.display_name, before.channel.id)
