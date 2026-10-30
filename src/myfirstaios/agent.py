from __future__ import annotations

from dataclasses import dataclass, field

from .memory import MemoryStore


@dataclass
class PersonalAgent:
    name: str = "PersonalAgent"
    memory: MemoryStore = field(default_factory=MemoryStore)

    def respond(self, user_input: str) -> str:
        return f"[{self.name}] You said: {user_input}"

    def run_tool(self, tool_name: str, *args, **kwargs) -> str:
        return f"Tool {tool_name} not implemented in this starter version."


__all__ = ["PersonalAgent"]
