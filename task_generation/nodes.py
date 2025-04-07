"""Node functions for task graph"""

###############################################################################
# Imports

from .state import TaskState


###############################################################################
# Nodes


#######################################
# Generation

def task_generation(state : TaskState):
    """Initial task parameter creation"""
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