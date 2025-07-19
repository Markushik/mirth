from src.mirth.application.contracts import Interactor, UserExistsContract
from src.mirth.application.transport import UserTransport

class UserExistsInteractor:
    def __init__(self):
        pass 

    async def __call__(self, contract: UserExistsContract) -> UserTransport:
        print(contract)
        print('Hello, UserExistsInteractor')
        return UserTransport(telegram_id=contract.telegram_id)
