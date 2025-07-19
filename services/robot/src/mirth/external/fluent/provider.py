from dishka import Provider, provide, Scope

from src.mirth.external.fluent.model import Locale

class FluentProvider(Provider):
    scope = Scope.APP

    def __init__(self, locale):
        super().__init__()
        self.locale = locale

    @provide
    def get_locale(self) -> Locale:
        print(self.locale["en"])
        return self.locale["en"]

