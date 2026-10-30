from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class Task:
    name: str
    description: str
    action: Callable[[], Any]


@dataclass
class Workflow:
    name: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)

    def run(self) -> list[dict[str, Any]]:
        results: list[dict[str, Any]] = []
        for task in self.tasks:
            results.append({
                "task": task.name,
                "description": task.description,
                "result": task.action(),
            })
        return results
