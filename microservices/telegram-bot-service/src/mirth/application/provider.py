from dishka import provide, Provider, Scope

from src.mirth.application.mediator import Mediator
from src.mirth.application.registry import setup_interactors

from faststream.nats import NatsBroker


class MediatorProvider(Provider):
    @provide(scope=Scope.APP)
    def get_mediator(self, broker: NatsBroker) -> Mediator:
        mediator = Mediator()
        setup_interactors(mediator, broker)
        return mediator
