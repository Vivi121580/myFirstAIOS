from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SessionState:
    session_id: str
    user_name: str | None = None
    context: dict[str, Any] = field(default_factory=dict)
    memory: list[str] = field(default_factory=list)

    def remember(self, item: str) -> None:
        if item not in self.memory:
            self.memory.append(item)

    def set_context(self, key: str, value: Any) -> None:
        self.context[key] = value

    def get_context(self, key: str, default: Any = None) -> Any:
        return self.context.get(key, default)

    def snapshot(self) -> dict[str, Any]:
        return {
            "session_id": self.session_id,
            "user_name": self.user_name,
            "context": self.context.copy(),
            "memory": list(self.memory),
        }
