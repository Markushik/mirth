import structlog
import logging
import sys

from functools import cache


@cache
def get_logger():
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.INFO,
    )

    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.TimeStamper(fmt="iso", utc=True),
            structlog.processors.add_log_level,
            structlog.processors.EventRenamer("event"),
            structlog.processors.dict_tracebacks,
            structlog.processors.JSONRenderer(indent=None),
        ],
    )

    return structlog.get_logger()
