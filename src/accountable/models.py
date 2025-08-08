from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Task:
    """Represents a single task in a learning phase."""

    description: str
    due_date: Optional[date] = None
    completed: bool = False
    phase_id: Optional[int] = None
    id: Optional[int] = None


@dataclass
class Phase:
    """A learning phase grouping multiple tasks."""

    name: str
    objective: str = ""
    description: str = ""
    completed: bool = False
    id: Optional[int] = None
