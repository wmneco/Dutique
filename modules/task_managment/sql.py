"""SQL Commands for the Task Management Module"""

###############################################################################
# Table Creation SQL Commands

CREATE_TABLE_TASK = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT,
    assignment TEXT,
    state TEXT,
    task_id INTEGER,
    discription TEXT
);
"""
CREATE_TABLE_ACTION = """
CREATE TABLE IF NOT EXISTS actions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    method TEXT,
    frequency TEXT
 );
"""

CREATE_RELATION_TABLE_ACTION_ROOM_FURNISHINGS = """
CREATE TABLE IF NOT EXISTS action_room_furnishings (
    action_id INTEGER,
    room_furnishing_id INTEGER,
    PRIMARY KEY (action_id, room_furnishing_id)
);
"""

CREATE_TABLE_ROOM_FURNISHINGS = """
CREATE TABLE IF NOT EXISTS room_furnishings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    room_name TEXT
);
"""

CREATE_TABLE_ROOMS = """
CREATE TABLE IF NOT EXISTS rooms (
    name TEXT PRIMARY KEY,
    room_type TEXT
);
"""
