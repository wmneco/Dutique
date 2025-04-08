"""Define the graph (chain) for the task generation"""

###############################################################################
# Imports

from langgraph.graph import START, END, StateGraph

from .state import TaskState
from .nodes import (
    task_generation,
    description_generation,
    quality_check,
    repair,
    storage
)

###############################################################################
# Implementation

#######################################
# Graph

task_graph_builder = StateGraph(state_schema=TaskState)

# Add nodes

task_graph_builder.add_node(task_generation)
task_graph_builder.add_node(description_generation)
task_graph_builder.add_node(quality_check)
task_graph_builder.add_node(repair)
task_graph_builder.add_node(storage)

# Add edges

task_graph_builder.add_edge(START, "task_generation")
task_graph_builder.add_edge("task_generation", "description_generation")

task_graph_builder.add_conditional_edges(
    "description_generation",
    quality_check,
    {"Retry": "repair", "Pass": "storage", "Fail": END},
)

task_graph_builder.add_conditional_edges(
    "repair",
    quality_check,
    {"Retry": "repair", "Pass": "storage", "Fail": END},
)

task_graph_builder.add_edge("description_generation", END)

# Compile graph

task_graph = task_graph_builder.compile()
