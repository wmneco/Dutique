"""States for the task generation graph"""

###############################################################################
# Imports

from typing_extensions import TypedDict
from chromadb import Collection


###############################################################################
# Graph States

class TaskState(TypedDict):
    """States for task generation"""
    home: dict
    target: str
    room: str
    method : str
    kind : str
    trys: int
    description: str
    success: bool
    collection: Collection
    uuid: str
    frequency : str
