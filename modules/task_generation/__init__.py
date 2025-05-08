"""Task generation for Dutique"""

###############################################################################
# Imports

import yaml

from core.base_module import BaseModule
from .graph import task_graph

###############################################################################
# Module

class TaskGenerationModule(BaseModule):
    """Generation of funny tasks"""
    name = "task_generation"
    depends_on = []
    optional_depends_on = []

    def init(self, state):
        """Initialize the module with a given state."""
        state.setdefault("tasks_quene", [])
        print(self.config)

    async def update(self, state):
        """Update the module's internal state based on the provided state."""
        task = await task_graph.ainvoke({
            "home": self.config,
        })
        state["tasks_quene"].append(task)
