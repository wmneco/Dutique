"""Dutique generates small household tasks"""
###############################################################################
# Imports

from core.engine import Engine
from modules.task_managment import TaskManagementModule


###############################################################################
# Main

if __name__ == "__main__":
    engine = Engine()
    #engine.register_module(TaskGenerationModule())
    engine.register_module(TaskManagementModule())
    engine.run()
