from src.mirth.application.contracts import UserExistsContract
from src.mirth.application.transport import UserTransport


class UserExistsInteractor:
    async def __call__(self, contract: UserExistsContract) -> UserTransport:
        print(f"Processing contract: {contract}")
        print('Hello, UserExistsInteractor')
        return UserTransport(telegram_id=contract.telegram_id)


