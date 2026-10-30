from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class MemoryItem:
    topic: str
    content: str
    tags: list[str] = field(default_factory=list)


class MemoryStore:
    """Simple in-memory knowledge store for the personal AI OS."""

    def __init__(self) -> None:
        self._items: list[MemoryItem] = []

    def add(self, topic: str, content: str, tags: list[str] | None = None) -> MemoryItem:
        item = MemoryItem(topic=topic, content=content, tags=tags or [])
        self._items.append(item)
        return item

    def search(self, query: str) -> list[MemoryItem]:
        q = query.lower()
        return [
            item
            for item in self._items
            if q in item.topic.lower() or q in item.content.lower() or any(q in tag.lower() for tag in item.tags)
        ]

    def recent(self, limit: int = 5) -> list[MemoryItem]:
        return self._items[-limit:]

    def list_topics(self) -> list[str]:
        return sorted({item.topic for item in self._items})

    def as_dict(self) -> List[dict]:
        return [
            {"topic": item.topic, "content": item.content, "tags": item.tags}
            for item in self._items
        ]
