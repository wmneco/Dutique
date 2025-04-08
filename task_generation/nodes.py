"""Node functions for task graph"""

###############################################################################
# Imports

import random
import logging

from .state import TaskState


###############################################################################
# Nodes

logger = logging.getLogger(__name__)

def log_task(state : TaskState) -> None:
    """Log the output of the Task function"""
    logger.info(
        "TASK: "
        +state["kind"]
        + "-->"
        + state["target"]
        + "-->"
        + (state["surface"] + "-->" if state["kind"] == "room" else "")
        + state["method"]
    )


#######################################
# Generation

def random_key (dictornary : dict) -> str:
    """Generate a random dict key"""
    return random.choice(list(dictornary))

def task_generation(state : TaskState):
    """Initial task parameter creation"""

    home = state["home"]
    state["kind"] = random_key(home)

    if state["kind"]  == "rooms":
        state["target"] = random_key(home[state["kind"]])
        state["surface"] = random_key(home[state["kind"]][state["target"]]["surfaces"])
        state["method"] = random.choice(home[state["kind"]][state["target"]]["surfaces"][state["surface"]]["methods"])
    else:
        state["target"] = random_key(home[state["kind"]])
        state["method"] = random_key(home[state["kind"]][state["target"]]["methods"])

    log_task(state)

    return state

def description_generation(state : TaskState):
    """LLM creates descriptions based on generated task parameters"""
    return state

def repair(state : TaskState):
    """Repair Tasks that fail quality checks with an LLM to improve the task"""
    return {"discription" : state.discription+"FIXED"}

def storage(state : TaskState):
    """Store the task in ChromaDB"""
    return {"success" : True}


#######################################
# Checks

def quality_check(state : TaskState):
    """LLM checks the task quality criteria"""
    return "Pass"
