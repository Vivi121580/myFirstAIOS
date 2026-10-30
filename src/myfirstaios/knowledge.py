from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class KnowledgeDocument:
    path: str
    content: str


class KnowledgeBase:
    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)

    def iter_files(self) -> Iterable[Path]:
        for path in sorted(self.root.rglob("*")):
            if path.is_file() and path.suffix.lower() in {".md", ".txt", ".py", ".json", ".yaml", ".yml"}:
                yield path

    def load_documents(self) -> list[KnowledgeDocument]:
        docs: list[KnowledgeDocument] = []
        for file_path in self.iter_files():
            try:
                text = file_path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            docs.append(KnowledgeDocument(path=str(file_path.relative_to(self.root)), content=text))
        return docs
