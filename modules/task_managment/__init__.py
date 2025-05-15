"""This module manages, stores and retrives tasks. It creates lists of tasks for the user."""

###############################################################################
# Imports

import asyncio
import sqlite3

from typing_extensions import TypedDict

from core.base_module import BaseModule
from .sql import (
    CREATE_TABLE_TASK,
    CREATE_TABLE_ACTION,
    CREATE_TABLE_ROOM_FURNISHINGS,
    CREATE_TABLE_ROOMS,
    CREATE_RELATION_TABLE_ACTION_ROOM_FURNISHINGS
)

###############################################################################
# TaskManagementModule

class TaskManagementModule(BaseModule):
    """Manage, store and retrieve tasks. Keep track """
    name = "task_management"
    depends_on = []
    optional_depends_on = []
    all_tasks = []
    database = None

    def init(self, state):
        """Initialize the module with a given state."""
        state.setdefault(self.name, {})

        self.logger.debug("Creating database")
        # Check if table exits and create it if not
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            cursor.execute(CREATE_TABLE_TASK)
            cursor.execute(CREATE_TABLE_ACTION)
            cursor.execute(CREATE_TABLE_ROOM_FURNISHINGS)
            cursor.execute(CREATE_TABLE_ROOMS)
            cursor.execute(CREATE_RELATION_TABLE_ACTION_ROOM_FURNISHINGS)

            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            self.logger.error("Error creating database: %s",e)

        self.generate_database()

        state[self.name]["uncompleted_tasks"] = []
        state[self.name]["completed_tasks"] = []


    def generate_database(self) -> list[str]:
        """Load config for tasks and create the database if needed."""
        try:
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            # Test if there is a database!
            cursor.execute("SELECT * FROM tasks")
            rows = cursor.fetchall()

            self.logger.info(rows)

            if len(rows) == 0:

                room_config = self.config["home"]["rooms"]

                # Create a new database from config file.
                self.logger.info("Creating new database...")

                for room in self.config["home"]["rooms"]:
                    # Create Room if it dosen't exits
                    cursor.execute(
                        "INSERT OR IGNORE INTO rooms (name, room_type) VALUES (?, ?);",
                        (
                            room,
                            "public"
                        )
                    )
                    for furnishing in room_config[room]["room_furnishings"]:
                        furnishing_id = cursor.execute(
                            """
                            INSERT OR IGNORE
                            INTO room_furnishings (name, room_name)
                            VALUES (?, ?);
                            """,
                            (
                                furnishing,
                                room
                            )
                        ).fetchone()[0]

                        for action in room_config[room]["room_furnishings"][furnishing]["actions"]:
                            action_id = cursor.execute(
                                """INSERT OR IGNORE "
                                INTO actions (method, frequency) VALUES (?,?) 
                                RETURNING id;
                                """,
                                (
                                    action["method"],
                                    action["frequency"]
                                )
                            ).fetchone()[0]

                            # cursor.execute(
                               
                            # )

                conn.commit()

            else:
                self.logger.info("Loaded existing database")

            conn.close()
        except sqlite3.Error as e:
            self.logger.error("Error testing database: %s",e)

        self.logger.debug("Database loaded")

        return

    async def update(self, state):
        """Update the module's internal state based on the provided state."""
        await asyncio.sleep(10)
        rows = []
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM rooms")
        rows = cursor.fetchall()
        self.logger.debug(rows)


        cursor.execute("SELECT * FROM room_furnishings")
        rows = cursor.fetchall()
        self.logger.debug(rows)

        conn.close()

        self.logger.debug(rows)
