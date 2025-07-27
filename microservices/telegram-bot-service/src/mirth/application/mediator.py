from typing import Dict, Type, Any, Callable


class Mediator:
    def __init__(self):
        self._interactors: Dict[Type, Callable] = {}

    def register_interactor(self, contract_type: Type, interactor: Callable):
        self._interactors[contract_type] = interactor

    async def send(self, contract: Any) -> Any:
        contract_type = type(contract)
        if contract_type not in self._interactors:
            raise ValueError(f"No interactor registered for {contract_type}")

        interactor = self._interactors[contract_type]
        return await interactor(contract)
