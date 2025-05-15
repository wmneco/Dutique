"""Base Module for Dutique"""
###############################################################################
# Imports

from abc import ABC, abstractmethod
import logging


###############################################################################
# Base Module

class BaseModule(ABC):
    """Base Module for Dutique"""
    name = "unnamed"
    depends_on = []
    optional_depends_on = []
    config = {}
    logger = None

    def __init__(self):
        self._available_modules = set()
        self.logger = logging.getLogger(self.name)

    def _check_optional(self, module_name):
        return module_name in self._available_modules

    def set_available_modules(self, available_modules):
        """Set all avaible modules."""
        self._available_modules = set(available_modules)

    @abstractmethod
    def init(self, state):
        """Initialize the module with a given state."""

    @abstractmethod
    async def update(self, state):
        """Update the module's internal state based on the provided state."""
