from dishka import Provider, provide, Scope
from faststream import FastStream
from faststream.nats import NatsBroker

from src.mirth.external.settings import Settings

class FaststreamProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_broker(self, settings: Settings) -> NatsBroker:
        broker = NatsBroker(f"nats://{settings.nats.host}:{settings.nats.port}")
        return broker

    @provide(scope=Scope.APP)
    async def get_faststream(self, broker: NatsBroker) -> FastStream:
        faststream = FastStream(broker)
        return faststream
