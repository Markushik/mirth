from .fluent import FluentMiddleware

# from sulguk import AiogramSulgukMiddleware as SulgukMiddleware


def get_middlewares() -> list:
    return [
        FluentMiddleware(),
    ]
