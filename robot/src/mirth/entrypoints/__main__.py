import asyncio

from pprint import pprint
from src.mirth.external.settings import get_settings
from src.mirth.external.logging import get_logger
from src.mirth.external.di import get_container
from faststream import FastStream


# разделение локалей по папкам


async def main() -> None:
    logger = get_logger()
    settings = get_settings()
    container = get_container(settings)

    pprint(await container.get(FastStream))



if __name__ == "__main__":
    asyncio.run(main())
