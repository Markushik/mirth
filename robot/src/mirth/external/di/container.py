from dishka import AsyncContainer, make_async_container

from src.mirth.external.settings import SettingsProvider, Settings
from src.mirth.entrypoints.faststream import FaststreamProvider

def get_container(settings: Settings) -> AsyncContainer:
    container = make_async_container(
        *[
            SettingsProvider(settings),
            FaststreamProvider(),
        ]
    )
    return container
