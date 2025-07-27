from dishka import provide, Provider, Scope

from src.mirth.application.mediator import Mediator
from src.mirth.application.registry import setup_interactors


class MediatorProvider(Provider):
    @provide(scope=Scope.APP)
    def get_mediator(self) -> Mediator:
        mediator = Mediator()
        setup_interactors(mediator)
        return mediator
