from dataclasses import dataclass, field


@dataclass
class SubtitleSession:
    guild_id: int
    channel_id: int
    active: bool = True


@dataclass
class SubtitleService:
    sessions: dict[int, SubtitleSession] = field(default_factory=dict)

    def start_session(self, guild_id: int, channel_id: int) -> SubtitleSession:
        session = SubtitleSession(guild_id=guild_id, channel_id=channel_id)
        self.sessions[guild_id] = session
        return session

    def stop_session(self, guild_id: int) -> bool:
        if guild_id in self.sessions:
            self.sessions[guild_id].active = False
            del self.sessions[guild_id]
            return True
        return False

    def is_active(self, guild_id: int) -> bool:
        return guild_id in self.sessions
