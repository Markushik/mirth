from typing import Any, Dict, Protocol

from aiogram_dialog.api.protocols import DialogManager
from aiogram_dialog.widgets.common import WhenCondition
from aiogram_dialog.widgets.text import Text


class Values(Protocol):
    def __getitem__(self, item: Any) -> Any:
        raise NotImplementedError


def default_format_text(text: str, data: Values) -> str:
    return text.format_map(data)


async def update_format(dialog_manager: DialogManager, locale: str) -> None:
    l10n = dialog_manager.middleware_data["l10ns"][locale]
    dialog_manager.middleware_data["aiogd_i18n_format"] = l10n.format_value


class FluentFormat(Text):
    def __init__(self, text: str, when: WhenCondition = None):
        super().__init__(when)
        self.text = text

    async def _render_text(self, data: Dict, manager: DialogManager) -> str:
        format_text = manager.middleware_data.get(
            "aiogd_i18n_format", default_format_text
        )
        return format_text(self.text, data)
