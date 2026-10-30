from __future__ import annotations

from typing import List

from .knowledge import KnowledgeBase, KnowledgeDocument


class SimpleRAG:
    def __init__(self, knowledge_base: KnowledgeBase) -> None:
        self.knowledge_base = knowledge_base
        self.documents = knowledge_base.load_documents()

    def search(self, query: str, limit: int = 5) -> List[KnowledgeDocument]:
        q = query.lower()
        scored: list[tuple[float, KnowledgeDocument]] = []

        for doc in self.documents:
            score = 0.0
            if q in doc.path.lower():
                score += 2.0
            if q in doc.content.lower():
                score += 1.0
            if score > 0:
                scored.append((score, doc))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for _, doc in scored[:limit]]

    def answer(self, query: str) -> str:
        matches = self.search(query, limit=3)
        if not matches:
            return "No relevant files found for your query."

        context = "\n\n".join(
            f"File: {doc.path}\n{doc.content[:800]}\n" for doc in matches
        )
        return context
