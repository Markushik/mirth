from src.mirth.entrypoints.telegram.handlers import get_handlers
from src.mirth.entrypoints.telegram.dialogs import get_dialogs
from src.mirth.entrypoints.telegram.middlewares import get_middlewares

from aiogram import Dispatcher

def setup_routers(dispatcher: Dispatcher):
    return dispatcher.include_routers(
        *get_handlers(), 
        *get_dialogs()
    )

def setup_middlewares(dispatcher: Dispatcher):
    return dispatcher.update.outer_middleware(
        *get_middlewares(),
    )
