from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import FromDishka, inject

from src.mirth.entrypoints.telegram.dialogs.main_menu.states import MainMenu
from dishka.integrations.aiogram import FromDishka, inject
from faststream.nats import NatsBroker
from src.mirth.application.interactors import UserExist
from src.mirth.application.mediator import Mediator

# todo: rewrite mediator pattern
@inject
async def command_start(_, dialog_manager: DialogManager, mediator: FromDishka[Mediator]) -> None:
    await dialog_manager.start(state=MainMenu.START)


def setup() -> Router:
    router = Router(name=__name__)

    router.message.register(command_start, CommandStart())

    return router
