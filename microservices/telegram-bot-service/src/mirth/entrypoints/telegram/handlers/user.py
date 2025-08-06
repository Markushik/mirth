from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram_dialog import DialogManager, StartMode
from dishka.integrations.aiogram import FromDishka, inject

from src.mirth.entrypoints.telegram.dialogs.main_menu.states import MainMenu
from faststream.nats import NatsBroker
from src.mirth.application.interactors import UserExistsInteractor
from src.mirth.application.contracts import UserExistsContract
from src.mirth.application.mediator import Mediator
from src.mirth.application.transport import UserTransport

from src.mirth.external.etcd import EtcdClient


@inject
async def command_start(
    message: Message,
    dialog_manager: DialogManager,
    mediator: FromDishka[Mediator],
    etcd: FromDishka[EtcdClient],
) -> None:
    # await etcd.put("1213", "Mark")
    contract = UserExistsContract(telegram_id=message.from_user.id)
    response = await mediator.send(contract)
    print(response)

    await dialog_manager.start(state=MainMenu.START)


def setup() -> Router:
    router = Router(name=__name__)

    router.message.register(command_start, CommandStart())

    return router
