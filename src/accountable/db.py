"""SQLite-backed storage for tasks and phases."""

from __future__ import annotations

import sqlite3
from datetime import date
from typing import Iterable, List

from .models import Phase, Task


class Database:
    def __init__(self, path: str = ":memory:") -> None:
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self._create_tables()

    def _create_tables(self) -> None:
        cur = self.conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS phases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                objective TEXT,
                description TEXT,
                completed INTEGER NOT NULL
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                due_date DATE,
                completed INTEGER NOT NULL,
                phase_id INTEGER,
                FOREIGN KEY(phase_id) REFERENCES phases(id)
            )
            """
        )
        self.conn.commit()

    # Phase operations
    def add_phase(self, phase: Phase) -> Phase:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO phases (name, objective, description, completed) VALUES (?, ?, ?, ?)",
            (phase.name, phase.objective, phase.description, int(phase.completed)),
        )
        phase.id = cur.lastrowid
        self.conn.commit()
        return phase

    # Task operations
    def add_task(self, task: Task) -> Task:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO tasks (description, due_date, completed, phase_id) VALUES (?, ?, ?, ?)",
            (
                task.description,
                task.due_date.isoformat() if task.due_date else None,
                int(task.completed),
                task.phase_id,
            ),
        )
        task.id = cur.lastrowid
        self.conn.commit()
        return task

    def complete_task(self, task_id: int) -> None:
        cur = self.conn.cursor()
        cur.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.conn.commit()

    def get_due_tasks(self, for_date: date) -> List[Task]:
        cur = self.conn.cursor()
        cur.execute(
            "SELECT id, description, due_date, completed, phase_id FROM tasks WHERE due_date <= ? AND completed = 0",
            (for_date.isoformat(),),
        )
        rows = cur.fetchall()
        tasks: List[Task] = []
        for row in rows:
            tasks.append(
                Task(
                    id=row["id"],
                    description=row["description"],
                    due_date=date.fromisoformat(row["due_date"]) if row["due_date"] else None,
                    completed=bool(row["completed"]),
                    phase_id=row["phase_id"],
                )
            )
        return tasks

    def close(self) -> None:
        self.conn.close()
