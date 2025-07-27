from dishka import Provider, provide, Scope
from faststream import FastStream
from faststream.nats import NatsBroker

from src.mirth.external.settings import Settings

from typing import AsyncIterable

class FaststreamProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_broker(self, settings: Settings) -> AsyncIterable[NatsBroker]:
        broker = NatsBroker(f"nats://{settings.nats.host}:{settings.nats.port}")
        await broker.connect()
        yield broker
        await broker.close()

    @provide(scope=Scope.APP)
    async def get_faststream(self, broker: NatsBroker) -> FastStream:
        faststream = FastStream(broker)
        return faststream
