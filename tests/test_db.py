from datetime import date

from accountable import Database, Phase, Task


def test_add_and_complete_task(tmp_path):
    db_file = tmp_path / "test.db"
    db = Database(str(db_file))

    phase = db.add_phase(Phase(name="Intro"))
    task = db.add_task(Task(description="Read docs", due_date=date.today(), phase_id=phase.id))

    due = db.get_due_tasks(date.today())
    assert len(due) == 1
    assert due[0].description == "Read docs"

    db.complete_task(task.id)
    assert db.get_due_tasks(date.today()) == []

    db.close()
