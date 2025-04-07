"""Dutique generates small household tasks"""
import task_generation

task = task_generation.task_graph.invoke({
    "history": [],
    "room": "",
    "difficulty": "",
    "category": "",
    "discription": "",
    "success": False
})

print(task)
