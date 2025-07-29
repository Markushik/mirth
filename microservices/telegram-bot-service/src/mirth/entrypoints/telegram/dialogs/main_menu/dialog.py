from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.kbd import Back, Button, SwitchTo

from src.mirth.entrypoints.telegram.dialogs.auxiliary.fluent.format import FluentFormat

from src.mirth.entrypoints.telegram.dialogs.main_menu.states import MainMenu
from sulguk import SULGUK_PARSE_MODE

def main_menu() -> Dialog:
    dialog = Dialog(
        Window(
            FluentFormat("hello-user"),
            #Const(
            #    """
            #    <ol start="10">
            #        <li>some item</li>
            #        <li>other item</li>
            #    </ol>
            #    <p>Some <b>text</b> in a paragraph</p>
            #    """
            #),
            Button(Const("Hello"), id="hello"),
            state=MainMenu.START,
            parse_mode=SULGUK_PARSE_MODE,
        )
    )
    return dialog
