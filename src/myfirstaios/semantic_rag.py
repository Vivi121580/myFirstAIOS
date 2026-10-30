from __future__ import annotations

from pathlib import Path

from .knowledge import KnowledgeBase
from .vector_store import SimpleVectorStore


class SemanticRAG:
    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)
        self.store = SimpleVectorStore()
        self._index_documents()

    def _index_documents(self) -> None:
        kb = KnowledgeBase(self.root)
        for doc in kb.load_documents():
            self.store.add(doc.content, {"path": doc.path})

    def search(self, query: str, limit: int = 5) -> list[str]:
        results = self.store.search(query, limit=limit)
        return [
            f"File: {item.metadata.get('path', 'unknown')}\n{item.text[:800]}"
            for item in results
        ]

    def answer(self, query: str) -> str:
        results = self.search(query, limit=3)
        if not results:
            return "No semantic matches found."
        return "\n\n".join(results)
