from src.mirth.application.mediator import Mediator

from src.mirth.application.interactors import UserExistsInteractor
from src.mirth.application.contracts import UserExistsContract

from faststream.nats import NatsBroker

def setup_interactors(mediator: Mediator, broker: NatsBroker):
    mediator.register_interactor(UserExistsContract, UserExistsInteractor(broker))
