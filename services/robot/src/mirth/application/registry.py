from src.mirth.application.mediator import Mediator

from src.mirth.application.interactors import UserExistsInteractor
from src.mirth.application.contracts import UserExistsContract

def setup_interactors(mediator: Mediator):
    mediator.register(
        UserExistsContract,
        UserExistsInteractor,
    )
