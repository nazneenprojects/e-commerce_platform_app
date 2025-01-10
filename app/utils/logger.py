import logging
import structlog


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create console handler for INFO and above
    info_handler = logging.StreamHandler()
    info_handler.setLevel(logging.INFO)
    info_formatter = logging.Formatter('%(message)s')
    info_handler.setFormatter(info_formatter)
    logger.addHandler(info_handler)

    # Create console handler for ERROR and above
    error_handler = logging.StreamHandler()
    error_handler.setLevel(logging.ERROR)
    error_formatter = logging.Formatter('%(message)s')
    error_handler.setFormatter(error_formatter)
    logger.addHandler(error_handler)

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )

def get_logger(name: str):
    return structlog.get_logger(name)