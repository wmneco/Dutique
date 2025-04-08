"""Functions to log node output in a readable form"""

###############################################################################
# Imports

from logging import Logger

import colorama

from .state import TaskState


###############################################################################
# Implementation

def log_task(state : TaskState, logger : Logger) -> None:
    """Log the output of the Task function"""
    logger.info(
        state["kind"]
        + "-->"
        + state["target"]
        + "-->"
        + (state["surface"] if state["kind"] == "room" else "")
        + ": TASK: "
        + state["method"]
    )
