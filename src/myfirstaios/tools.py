from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


@dataclass
class ToolCall:
    name: str
    description: str
    function: Callable[..., str]


@dataclass
class ToolRegistry:
    tools: dict[str, ToolCall] = field(default_factory=dict)

    def register(self, tool: ToolCall) -> None:
        self.tools[tool.name] = tool

    def list_tools(self) -> list[str]:
        return sorted(self.tools.keys())

    def call(self, name: str, *args, **kwargs) -> str:
        if name not in self.tools:
            raise KeyError(f"Unknown tool: {name}")
        return self.tools[name].function(*args, **kwargs)


def build_default_tool_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(
        ToolCall(
            name="echo",
            description="Return the text exactly as provided.",
            function=lambda text: str(text),
        )
    )
    registry.register(
        ToolCall(
            name="summarize",
            description="Create a simple note-style summary.",
            function=lambda text: f"Summary: {text[:200]}" if text else "Summary: (empty input)",
        )
    )
    return registry
