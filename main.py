"""Dutique generates small household tasks"""

###############################################################################
# Imports

import logging

import yaml

import task_generation


###############################################################################
# Implementation

#######################################
# main

logger = logging.getLogger('task_generation.nodes')
logger.setLevel(logging.DEBUG)

logging.basicConfig(
    level=logging.WARNING,  # Default auf WARNING
    format='[%(name)s] %(levelname)s: %(message)s',
)

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

    task = task_generation.task_graph.invoke({
        "home": config["home"]
    })
