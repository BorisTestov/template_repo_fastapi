import logging

from .settings import log_settings


def setup_logging():
    formatter = logging.Formatter(
        "%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s"
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logging.basicConfig(level=log_settings.level, handlers=[stream_handler])


def get_logger(name):
    return logging.getLogger(name)


setup_logging()
