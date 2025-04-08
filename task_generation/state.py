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
    difficulty: int
    category: str
    discription: str
    success: bool
