from myfirstaios.workflow import Workflow, Task
from myfirstaios.session import SessionState


def test_workflow_runs_tasks():
    workflow = Workflow("demo")
    workflow.add_task(Task("hello", "run a basic action", lambda: "done"))
    result = workflow.run()
    assert result[0]["result"] == "done"


def test_session_tracks_context_and_memory():
    session = SessionState(session_id="abc123", user_name="Vivi")
    session.set_context("goal", "build AI OS")
    session.remember("Use local prompts first")

    assert session.get_context("goal") == "build AI OS"
    assert "Use local prompts first" in session.memory
    assert session.snapshot()["user_name"] == "Vivi"
