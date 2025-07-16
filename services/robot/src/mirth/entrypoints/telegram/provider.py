from dishka import Scope, Provider, provide

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.base import BaseEventIsolation, BaseStorage, DefaultKeyBuilder
from typing import AsyncIterable

from src.mirth.external.settings import Settings

class DispatcherProvider(Provider):
    scope = Scope.APP

    @provide
    def get_storage(self) -> BaseStorage:
        memory = MemoryStorage()
        return memory
    
    @provide
    def get_dispatcher(
        self,
        storage: BaseStorage,
    ) -> Dispatcher:
        dispatcher = Dispatcher(storage=storage)
        return dispatcher


class BotProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_bot(
        self,
        settings: Settings, 
    ) -> AsyncIterable[Bot]:
        async with Bot(token=settings.bot.token) as bot:
            yield bot
