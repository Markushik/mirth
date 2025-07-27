from typing import Any, Awaitable, Callable, Dict, Union

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import CallbackQuery, Message, TelegramObject
from fluent.runtime import FluentLocalization


from src.mirth.entrypoints.telegram.dialogs.main_menu.states import MainMenu
from src.mirth.external.fluent import Locale


class FluentMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: dict[str, Any],
    ) -> Any:
        container = data["dishka_container"]

        locale = await container.get(Locale)

        data["aiogd_i18n_format"] = locale.format_value

        return await handler(event, data)
