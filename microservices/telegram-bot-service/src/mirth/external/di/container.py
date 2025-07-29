from dishka import AsyncContainer, make_async_container

from src.mirth.external.settings import SettingsProvider, Settings
from src.mirth.entrypoints.faststream import FaststreamProvider
from src.mirth.entrypoints.telegram import BotProvider, DispatcherProvider
from src.mirth.application import MediatorProvider
from src.mirth.external.fluent import FluentProvider

from src.mirth.external.etcd import EtcdProvider


def get_container(settings: Settings, locales) -> AsyncContainer:
    container = make_async_container(
        *[
            SettingsProvider(settings),
            EtcdProvider(),
            FluentProvider(locales),
            MediatorProvider(),
            FaststreamProvider(),
            BotProvider(),
            DispatcherProvider(),
        ]
    )
    return container
