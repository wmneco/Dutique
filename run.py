"""Dutique generates small household tasks"""
###############################################################################
# Imports

from core.engine import Engine
from modules.task_generation import TaskGenerationModule


###############################################################################
# Main

if __name__ == "__main__":
    engine = Engine()
    engine.register_module(TaskGenerationModule())
    engine.run()
