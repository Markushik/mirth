from dishka import AsyncContainer, make_async_container

from src.mirth.external.settings import SettingsProvider, Settings
from src.mirth.entrypoints.faststream import FaststreamProvider
from src.mirth.entrypoints.telegram import BotProvider, DispatcherProvider


def get_container(settings: Settings) -> AsyncContainer:
    container = make_async_container(
        *[
            SettingsProvider(settings),
            FaststreamProvider(),
            BotProvider(),
            DispatcherProvider(),
        ]
    )
    return container
