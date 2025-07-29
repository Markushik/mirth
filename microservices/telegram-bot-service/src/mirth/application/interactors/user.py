from src.mirth.application.contracts import UserExistsContract
from src.mirth.application.transport import UserTransport

from faststream.nats import NatsBroker

from ormsgpack import packb, unpackb

from pprint import pprint
from zstd import compress


class UserExistsInteractor:
    def __init__(self, broker: NatsBroker):
        self.broker = broker

    async def __call__(self, contract: UserExistsContract) -> UserTransport:
        request = await self.broker.request(
            compress(packb(contract)), 
            subject="test.user"
        )
        return unpackb(request.body)

