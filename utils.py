import os
import logging.config
from pathlib import Path


Path(os.getcwd() + "/logs").mkdir(parents=True, exist_ok=True)

formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")


def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


setup_logger("system_logger", "logs/sys_logs.log")
system_logger = logging.getLogger("system_logger")

TOKEN = "669096995768f6690969957692"

PROD_SERV = "https://games.datsteam.dev/"
TEST_SERV = "https://games-test.datsteam.dev/"
