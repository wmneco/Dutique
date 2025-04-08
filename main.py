"""Dutique generates small household tasks"""

###############################################################################
# Imports

import logging

import yaml
from colorama import Fore, Style

import task_generation


###############################################################################
# Implementation

#######################################
# Logging Config

class LogFormatter(logging.Formatter):
    """Formate"""
    format_template = "%(levelname)s: [%(name)s]: %(message)s"

    FORMATS = {
        logging.DEBUG: format_template,
        logging.INFO: format_template,
        logging.WARNING: Fore.YELLOW + format_template + Style.RESET_ALL,
        logging.ERROR: Fore.RED + format_template + Style.RESET_ALL,
        logging.CRITICAL: Fore.LIGHTRED_EX + format_template + Style.RESET_ALL
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

task_generation_logger = logging.getLogger("task_generation")

stream = logging.StreamHandler()
stream.setLevel(logging.INFO)
stream.setFormatter(LogFormatter())

logger.addHandler(stream)
task_generation_logger.addHandler(stream)

#######################################
# Read room config

def read_config(filename : str) -> dict:
    """Read yaml config"""
    data : dict = {}
    with open(filename, 'r', encoding="UTF-8") as file:
        data = yaml.safe_load(file)
    return data


#######################################
# main

if __name__ == "__main__":
    config = read_config("config.yaml")

    for x in range (10):
        task = task_generation.task_graph.invoke({
            "home": config["home"]
        })

        logger.info("TASK: %s\n", task["description"])
