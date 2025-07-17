from src.mirth.application.contracts import Interactor


class UserExist(Interactor[int, bool]):
    def __init__(self):
        pass

    async def __call__(self, telegram_id: int) -> bool:
        print(telegram_id)
        print("HELLO FROM USEREXIST")
        return True
