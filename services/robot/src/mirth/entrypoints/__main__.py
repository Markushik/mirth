import asyncio

from pprint import pprint
from src.mirth.external.settings import get_settings
from src.mirth.external.logging import get_logger
from src.mirth.external.di import get_container
from faststream import FastStream

from src.mirth.entrypoints.telegram import main as main_telegram
#from src.mirth.entrypoints.faststream import main as main_faststream

# разделение локалей по папкам

async def _main() -> None:
    logger = get_logger()
    settings = get_settings()
    container = get_container(settings)
    
    try:
        await asyncio.gather(
            main_telegram(container)
            #main_faststream(container)
        )
    except KeyboardInterrupt:
        pprint("exit")


def run():
    asyncio.run(_main())


if __name__ == "__main__":
    run()
