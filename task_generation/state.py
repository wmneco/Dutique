"""States for the task generation graph"""

###############################################################################
# Imports

from typing_extensions import TypedDict


###############################################################################
# Graph States

class TaskState(TypedDict):
    """States for task generation"""
    history: list
    room: str
    difficulty: int
    category: str
    discription: str
    success: bool
