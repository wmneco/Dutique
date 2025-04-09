"""Node functions for task graph"""

###############################################################################
# Imports

import random
import logging
import uuid

from langchain_ollama import ChatOllama

from .state import TaskState
from .prompts import (
    description_appliance_task,
    description_room_task,
    check_room_task_description,
    check_appliance_description,
    repair_room_task_description,
    repair_appliance_task_description
)

from .log import log_task, log_description, log_check, log_repair

###############################################################################
# Nodes

#######################################
# Logging

logger = logging.getLogger(__name__)


#######################################
# Load LLM

llm = ChatOllama(
    model="llama3.2:latest",
    configurable_fields=("temperature","seed"),
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
        state["method"] = random.choice(
            home[state["kind"]][state["target"]]["surfaces"][state["surface"]]["methods"]
        )
    else:
        state["target"] = random_key(home[state["kind"]])
        state["method"] = random_key(home[state["kind"]][state["target"]]["methods"])

    log_task(state, logger)

    return state

def description_generation(state : TaskState):
    """LLM creates descriptions based on generated task parameters"""

    # Init
    state["trys"] = 0
    state["uuid"] = str(uuid.uuid4())

    if state["kind"] == "rooms":
        prompt = description_room_task.invoke(
            {
                "room": state['target'],
                "surface": state["surface"],
                "task": state["method"]
            }
        )
    else:
        prompt = description_appliance_task.invoke(
            {
                "appliance": state['target'],
                "task": state["method"]
            }
        )

    state["description"] = llm.with_config(
        {"temperature": 1, "seed": state["uuid"]}).invoke(prompt).content.rstrip()

    log_description(state, logger)

    return state

def repair(state : TaskState):
    """Repair Tasks that fail quality checks with an LLM to improve the task"""

    if state["kind"] == "rooms":
        prompt = repair_room_task_description.invoke(
            {
                "description": state["description"],
                "room": state['target'],
                "surface": state["surface"],
                "task": state["method"]
            }
        )
    else:
        prompt = repair_appliance_task_description.invoke(
            {
                "description": state["description"],
                "appliance": state['target'],
                "task": state["method"]
            }
        )

    state["description"] = llm.invoke(prompt).content.rstrip()
    log_repair(state, logger)

    state["trys"] += 1

    return state

def storage(state : TaskState):
    """Store the task in ChromaDB"""
    state["collection"].add(
        documents=[
            state["description"]
        ],
        # metadatas= [

        # ],
        ids=[state["uuid"]],
    )

    return {"success" : True}


#######################################
# Checks

def quality_check(state : TaskState):
    """LLM checks the task quality criteria"""

    if state["trys"] > 5:
        return "fail"

    if state["kind"] == "rooms":
        prompt = check_room_task_description.invoke(
            {
                "description": state["description"],
                "room": state['target'],
                "surface": state["surface"],
                "task": state["method"]
            }
        )
    else:
        prompt = check_appliance_description.invoke(
            {
                "description": state["description"],
                "appliance": state['target'],
                "task": state["method"]
            }
        )

    result = llm.invoke(prompt).content.casefold().rstrip()
    log_check(result, logger)

    if (result == "pass" or result == "retry"):
        return result

    raise ValueError
