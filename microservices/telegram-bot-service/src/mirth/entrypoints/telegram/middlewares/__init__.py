from .fluent import FluentMiddleware

def get_middlewares() -> list:
    return [FluentMiddleware()]
