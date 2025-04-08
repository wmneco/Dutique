"""States for the task generation graph"""

###############################################################################
# Imports

from typing_extensions import TypedDict


###############################################################################
# Graph States

class TaskState(TypedDict):
    """States for task generation"""
    home: dict
    history: list
    target: str
    surface: str
    method : str
    kind : str
    trys: int
    difficulty: int
    category: str
    description: str
    success: bool
