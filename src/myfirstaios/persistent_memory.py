from __future__ import annotations

import json
from pathlib import Path

from .memory import MemoryStore


class PersistentMemoryStore(MemoryStore):
    """Memory store backed by a local JSON file."""

    def __init__(self, file_path: str | Path) -> None:
        super().__init__()
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self._load()

    def _load(self) -> None:
        if not self.file_path.exists():
            self.file_path.write_text("[]", encoding="utf-8")
            return

        try:
            data = json.loads(self.file_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = []

        for item in data:
            self._items.append(
                type("MemoryItemProxy", (), item)() if False else {
                    "topic": item.get("topic", "unknown"),
                    "content": item.get("content", ""),
                    "tags": item.get("tags", []),
                }
            )

        # Convert to proper MemoryItem objects
        from .memory import MemoryItem

        self._items = [
            MemoryItem(topic=item["topic"], content=item["content"], tags=item.get("tags", []))
            for item in self._items
        ]

    def save(self) -> None:
        payload = [
            {"topic": item.topic, "content": item.content, "tags": item.tags}
            for item in self._items
        ]
        self.file_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    def add(self, topic: str, content: str, tags: list[str] | None = None) -> object:
        item = super().add(topic, content, tags)
        self.save()
        return item
