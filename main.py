"""Dutique generates small household tasks"""

import yaml

import task_generation

# Read room config
def read_config(filename : str) -> dict:
    """Read yaml config"""
    data : dict = {}
    with open(filename, 'r', encoding="UTF-8") as file:
        data = yaml.safe_load(file)
    return data

config = read_config("config.yaml")
for room in config["home"]["rooms"]:
    print("Room:", room)

task = task_generation.task_graph.invoke({
    "history": [],
    "room": "",
    "difficulty": "",
    "category": "",
    "discription": "",
    "success": False
})

print(task)
