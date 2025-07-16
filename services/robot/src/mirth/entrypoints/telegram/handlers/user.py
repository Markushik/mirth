from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import FromDishka, inject

from src.mirth.entrypoints.telegram.dialogs.main_menu.states import MainMenu
from dishka.integrations.aiogram import FromDishka, inject
from faststream.nats import NatsBroker

@inject
async def command_start(message: Message, dialog_manager: DialogManager, broker: FromDishka[NatsBroker]) -> None:
    print(broker)
    await broker.connect()
    await dialog_manager.start(state=MainMenu.START)
    await broker.publish("hello", "test.data")


def setup() -> Router:
    router = Router(name=__name__)

    router.message.register(command_start, CommandStart())

    return router
