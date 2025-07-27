from dishka import provide, Scope, Provider

from src.mirth.external.settings import Settings, NatsSettings, BotSettings


class SettingsProvider(Provider):
    scope = Scope.APP

    def __init__(self, settings: Settings):
        super().__init__()
        self.settings = settings

    @provide
    def get_config(self) -> Settings:
        return self.settings

    @provide
    def get_nats_config(self) -> NatsSettings:
        return self.settings.nats

    @provide
    def get_bot_config(self) -> BotSettings:
        return self.settings.bot
