import logging
import logging.config
from pathlib import Path
from typing import Any


log_config: dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "use_colors": False,
            "fmt": '%(asctime)s - %(client_addr)s - "%(request_line)s" %(status_code)s',
        },
    },
    "handlers": {
        "access_stream": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
        "access_file": {
            "formatter": "access",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "log/uvicorn.access.log",
            "when": "midnight",
            "interval": 1,
            "backupCount": 0,
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "uvicorn.access": {
            "handlers": ["access_stream", "access_file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


def init():
    Path("log").mkdir(parents=True, exist_ok=True)
    logging.config.dictConfig(log_config)
