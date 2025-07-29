from dishka import Provider, provide, Scope

from src.mirth.external.etcd import EtcdClient
from httpx import AsyncClient

from src.mirth.external.settings import Settings
from typing import AsyncIterable

class EtcdProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_etcd(self, settings: Settings) -> AsyncIterable[EtcdClient]:
        client = EtcdClient(f"http://{settings.etcd.host}:{settings.etcd.port}/v3")
        await client.connect()
        yield client
        await client.close()

