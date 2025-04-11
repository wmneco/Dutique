"""Dutique generates small household tasks"""

###############################################################################
# Imports

import logging

import yaml
from colorama import Fore, Style
import chromadb

import task_generation


###############################################################################
# Init

#######################################
# Logging Config

class LogFormatter(logging.Formatter):
    """Formate"""
    format_template = "%(levelname)s: [%(name)s]: %(message)s"

    FORMATS = {
        logging.DEBUG: format_template,
        logging.INFO: Fore.BLUE + format_template + Style.RESET_ALL,
        logging.WARNING: Fore.YELLOW + format_template + Style.RESET_ALL,
        logging.ERROR: Fore.RED + format_template + Style.RESET_ALL,
        logging.CRITICAL: Fore.LIGHTRED_EX + format_template + Style.RESET_ALL
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

task_generation_logger = logging.getLogger("task_generation")

stream = logging.StreamHandler()
stream.setLevel(logging.DEBUG)
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
# ChromaDB

chroma_client = chromadb.Client()
task_collection = chroma_client.create_collection(name="task_collection")


###############################################################################
# Helper functions

def query_tasks(query : str) -> None:
    """Query the task collection with a search string"""
    result = task_collection.query(
        query_texts=[query],
        n_results=1,
    )

    logger.info("QUERY: %s %s", result["documents"][0][0], result["metadatas"][0][0])

###############################################################################
# main

if __name__ == "__main__":
    config = read_config("config.yaml")

    for x in range (10):
        task = task_generation.task_graph.invoke({
            "home": config["home"],
            "collection" : task_collection
        })

        logger.debug("TASK: %s", task["description"])

    # Some testing
    query_tasks("easy")
    query_tasks("Kitchen")
