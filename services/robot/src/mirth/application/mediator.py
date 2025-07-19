from typing import Type, TypeVar, Callable, Awaitable, Dict, Any

T = TypeVar("T")

class Mediator:
    def __init__(self):
        self._handlers: Dict[Type[Any], Any] = {}

    def register(self, contract_type: Type[T], handler: Any):
        self._handlers[contract_type] = handler

    async def send(self, contract: T) -> Any:
        contract_type = type(contract)
        handler = self._handlers.get(contract_type)

        if handler is None:
            raise ValueError(f"No handler registered for contract type: {contract_type}")

        return await handler(contract)
