import asyncio
from dishka import AsyncContainer
from aiogram import Bot, Dispatcher

async def main(container: AsyncContainer) -> None:
    bot = await container.get(Bot)
    dispatcher = await container.get(Dispatcher)

    await dispatcher.start_polling(bot)

