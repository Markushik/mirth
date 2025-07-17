from typing import Dict, Type, Callable, Any

class Mediator:
    def __init__(self):
        self.handlers: Dict[Type, Callable[..., Any]] = {}

    def include_interactor(self, interactor_type: Type, handler: Callable):
        self.handlers[interactor_type] = handler

    async def send(self, interactor: Any, *args, **kwargs) -> Any:
        handler = self.handlers.get(type(interactor))
        if not handler:
            raise ValueError(f"No handler for {type(interactor)}")
        return await handler(interactor, *args, **kwargs)
