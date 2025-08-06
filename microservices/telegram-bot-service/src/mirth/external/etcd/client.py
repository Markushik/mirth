import httpx
from typing import Optional, Dict, Any


class EtcdClient:
    def __init__(self, url: str):
        self.base_url = url
        self._client: Optional[httpx.AsyncClient] = None

    async def connect(self):
        if self._client is None:
            self._client = httpx.AsyncClient(base_url=self.base_url)

    async def close(self):
        if self._client:
            await self._client.aclose()
            self._client = None

    async def put(self, key: str, value: str) -> Dict[str, Any]:
        if not self._client:
            await self.connect()
        resp = await self._client.post("/kv/put", json={"key": key, "value": value})
        resp.raise_for_status()
        return resp.json()
