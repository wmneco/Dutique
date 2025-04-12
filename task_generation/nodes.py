"""Node functions for task graph"""

###############################################################################
# Imports

import random
import logging
import uuid
from datetime import datetime

from langchain_ollama import ChatOllama

from .state import TaskState
from .prompts import (
    description_task,
    check_description,
    repair_task_description
)

from .log import log_description, log_check, log_repair

###############################################################################
# Nodes

#######################################
# Logging

logger = logging.getLogger(__name__)


#######################################
# Load LLM

llm = ChatOllama(
    model="llama3.2:1b",
    configurable_fields=("temperature","seed"),
    base_url="host.docker.internal:11434",
)

#######################################
# Generation

def random_key (dictornary : dict) -> str:
    """Generate a random dict key"""
    return random.choice(list(dictornary))

def task_generation(state : TaskState):
    """Initial task parameter creation"""
    home = state["home"]
    kind = random_key(home)
    target = random_key(home[kind])
    method = random_key(home[kind][target]["tasks"])["method"]
    room = home[kind][target]["room"]

    return {
        "trys": 0,
        "uuid": str(uuid.uuid4()),
        "success": False,
        "kind":kind,
        "target":target,
        "method": method,
        "room": room
    }

def description_generation(state : TaskState):
    """LLM creates descriptions based on generated task parameters"""

    prompt = description_task.invoke({
        "room": state['target'],
        "target": state['kind'].capitalize() + ": " + state['target'],
        "task": state["method"],
    })

    state["description"] = llm.with_config({
        "temperature": 1.5,
        "seed": state["uuid"]
    }).invoke(prompt).content.rstrip()

    log_description(state, logger)

    return state

def repair(state : TaskState):
    """Repair Tasks that fail quality checks with an LLM to improve the task"""

    prompt = repair_task_description.invoke({
        "room": state['target'],
        "target": state['kind'].capitalize() + ": " + state['target'],
        "task": state["method"],
    })

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
         metadatas= [{
            "created": str(datetime.now()),
            "kind" : state["kind"],
            "room": state['target'],
            "surface": state["surface"] if "surface" in state else "",
            "task": state["method"]

        }],
        ids=[state["uuid"]],
    )

    return {"success" : True}


#######################################
# Checks

def quality_check(state : TaskState):
    """LLM checks the task quality criteria"""

    if state["trys"] > 5:
        return "fail"

    prompt = check_description.invoke({
        "description": state["description"],
        "target": state['kind'].capitalize() + ": " + state['target'],
        "room" : state["room"],
        "task": state["method"]
    })

    result = llm.invoke(prompt).content.casefold().rstrip()
    log_check(result, logger)

    if (result == "pass" or result == "retry"):
        return result

    raise ValueError
