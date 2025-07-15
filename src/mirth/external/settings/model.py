from dataclasses import dataclass


@dataclass
class BotSettings:
    token: str


@dataclass
class NatsSettings:
    host: str
    port: int


@dataclass
class Settings:
    bot: BotSettings
    nats: NatsSettings
