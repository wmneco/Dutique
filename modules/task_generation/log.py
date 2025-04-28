"""Functions to log node output in a readable form"""

###############################################################################
# Imports

from logging import Logger

from .state import TaskState


###############################################################################
# Implementation

def log_task(state : TaskState, logger : Logger) -> None:
    """Log the output of the Task function"""
    logger.debug(
        "TASK: "
        +state["kind"]
        + "->"
        + state["target"]
        + "->"
        + (state["surface"] + "->" if state["kind"] == "rooms" else "")
        + state["method"]
    )

def log_description (state : TaskState, logger : Logger) -> None:
    """Log the task description"""
    logger.debug(
        "DESCRIPTION: "
        +state["description"]
    )

def log_repair (state : TaskState, logger : Logger) -> None:
    """Log the task description"""
    logger.debug(
        "REPAIRED: "
        +state["description"]
    )

def log_check (result ,logger : Logger) -> None:
    """Log the check result"""
    logger.debug(
        "CHECK: "
        +result
    )

def log_check_error(logger : Logger) -> None:
    """Log if a task finally gets aborted"""
    logger.warning(
        "TASK FAIL"
    )
