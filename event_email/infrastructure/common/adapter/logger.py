import logging
from typing import Optional

from event_email.core.common.port.logger import ILogger


class Logger(ILogger):
    logging.getLogger().setLevel(logging.DEBUG)

    def info(self, msg: str) -> None:
        logging.info(msg)

    def warn(self, msg: str) -> None:
        logging.warning(msg)

    def error(self, msg: str, exception: Optional[Exception] = None, extra: dict = None) -> None:
        if exception is not None:
            logging.exception(msg, extra=extra)
        else:
            logging.error(msg, extra=extra)
