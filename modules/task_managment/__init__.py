"""This module manages, stores and retrives tasks. It creates lists of tasks for the user."""

###############################################################################
# Imports

from core.base_module import BaseModule

class TaskManagementModule(BaseModule):
    """Manage, store and retrieve tasks. Keep track """
    name = "task_management"
    depends_on = []
    optional_depends_on = []

    def init(self, state):
        """Initialize the module with a given state."""
        state[self.name]["tasks"] = []
        state[self.name]["completed_tasks"] = []

    async def update(self, state):
        """Update the module's internal state based on the provided state."""
