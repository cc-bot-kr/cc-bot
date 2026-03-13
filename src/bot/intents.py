import discord


def build_intents(enable_message_content_intent: bool = False) -> discord.Intents:
    intents = discord.Intents.default()
    intents.message_content = enable_message_content_intent
    intents.voice_states = True
    return intents
