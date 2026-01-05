import logging
import os
from datetime import datetime


def setup_logger(level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("claimer")
    logger.setLevel(getattr(logging, level.upper(), logging.INFO))
    logger.propagate = False

    if logger.handlers:
        return logger

    os.makedirs("logs", exist_ok=True)
    log_file = os.path.join("logs", f"run_{datetime.now().strftime('%Y%m%d')}.log")

    fmt = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    return logger
