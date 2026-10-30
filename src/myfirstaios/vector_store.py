from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass
class VectorItem:
    text: str
    vector: list[float]
    metadata: dict


class SimpleVectorStore:
    def __init__(self) -> None:
        self.items: list[VectorItem] = []

    def add(self, text: str, metadata: dict | None = None) -> None:
        metadata = metadata or {}
        vector = self._simple_embed(text)
        self.items.append(VectorItem(text=text, vector=vector, metadata=metadata))

    def search(self, query: str, limit: int = 5) -> list[VectorItem]:
        q = self._simple_embed(query)
        scored: list[tuple[float, VectorItem]] = []

        for item in self.items:
            score = cosine_similarity(q, item.vector)
            if score > 0:
                scored.append((score, item))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [item for _, item in scored[:limit]]

    def _simple_embed(self, text: str) -> list[float]:
        tokens = [t.lower() for t in text.replace("\n", " ").split() if t]
        vocab = sorted(set(tokens))
        vector = [0.0 for _ in vocab]

        counts = {token: 0 for token in vocab}
        for token in tokens:
            counts[token] += 1

        for i, token in enumerate(vocab):
            vector[i] = counts[token]

        return vector


def cosine_similarity(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        length = min(len(a), len(b))
        a = a[:length]
        b = b[:length]

    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)
