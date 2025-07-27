import asyncio

from dishka import AsyncContainer
from aiogram import Bot, Dispatcher
from pprint import pprint
from src.mirth.external.settings import get_settings
from src.mirth.external.logging import get_logger
from src.mirth.external.di import get_container
from src.mirth.external.fluent import get_locales
from faststream import FastStream


async def main() -> None:
    locales = get_locales()
    logger = get_logger()
    settings = get_settings()

    container: AsycnContainer = get_container(settings, locales)

    bot = await container.get(Bot)
    dispatcher = await container.get(Dispatcher)

    try:
        await asyncio.gather(dispatcher.start_polling(bot))
    except KeyboardInterrupt:
        pprint("exit")


def run():
    asyncio.run(main())


if __name__ == "__main__":
    run()
