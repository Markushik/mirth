from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Back, Button, SwitchTo

from src.mirth.entrypoints.telegram.dialogs.main_menu.states import MainMenu


def main_menu() -> Dialog:
    dialog = Dialog(
        Window(
            Const("I'm Mirth"),
            Button(Const("Hello"), id="hello"),
            state=MainMenu.START,
        )
    )
    return dialog
