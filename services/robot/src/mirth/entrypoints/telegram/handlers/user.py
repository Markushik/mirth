from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import FromDishka, inject

from src.mirth.entrypoints.telegram.dialogs.main_menu.states import MainMenu
from dishka.integrations.aiogram import FromDishka, inject
from faststream.nats import NatsBroker
from src.mirth.application.interactors import UserExistsInteractor
from src.mirth.application.contracts import UserExistsContract
from src.mirth.application.mediator import Mediator
from src.mirth.application.transport import UserTransport

# todo: rewrite mediator pattern
@inject
async def command_start(message: Message, dialog_manager: DialogManager, mediator: FromDishka[Mediator]) -> None:
    #user_transport = UserTransport(telegram_id=message.from_user.id)
    #contract = UserExistsContract(telegram_id=message.from_user.id)
    #print(contract)

    #user_exists = await mediator.send(contract)
    #print(user_exists)
    
    await dialog_manager.start(state=MainMenu.START)


def setup() -> Router:
    router = Router(name=__name__)

    router.message.register(command_start, CommandStart())

    return router
