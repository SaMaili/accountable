"""Simple command line interface for experimenting with the core module."""

from __future__ import annotations

import argparse
from datetime import date

from .db import Database
from .models import Task


def main() -> None:
    parser = argparse.ArgumentParser(description="Accountable CLI")
    sub = parser.add_subparsers(dest="cmd")

    add_task = sub.add_parser("add-task", help="Add a new task")
    add_task.add_argument("description", help="Task description")
    add_task.add_argument("--due-date", help="Due date in YYYY-MM-DD format")

    list_due = sub.add_parser("list-due", help="List tasks due by date")
    list_due.add_argument("--date", required=True, help="Date in YYYY-MM-DD format")

    args = parser.parse_args()
    db = Database("accountable.db")

    if args.cmd == "add-task":
        due = date.fromisoformat(args.due_date) if args.due_date else None
        task = db.add_task(Task(description=args.description, due_date=due))
        print(f"Created task {task.id}")
    elif args.cmd == "list-due":
        day = date.fromisoformat(args.date)
        for task in db.get_due_tasks(day):
            status = "done" if task.completed else "open"
            due = task.due_date.isoformat() if task.due_date else ""
            print(f"[{task.id}] {task.description} ({due}) - {status}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
