from __future__ import annotations

import sqlite3
from pathlib import Path


class ChatStore:
    def __init__(self, db_path: str | Path = "data/chat.db") -> None:
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self) -> None:
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS chats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                user_message TEXT NOT NULL,
                assistant_reply TEXT NOT NULL
            )
            """
        )
        conn.commit()
        conn.close()

    def save(self, username: str, user_message: str, assistant_reply: str) -> None:
        conn = sqlite3.connect(self.db_path)
        conn.execute(
            "INSERT INTO chats(username, user_message, assistant_reply) VALUES (?, ?, ?)",
            (username, user_message, assistant_reply),
        )
        conn.commit()
        conn.close()

    def fetch_recent(self, username: str, limit: int = 10) -> list[dict]:
        conn = sqlite3.connect(self.db_path)
        rows = conn.execute(
            "SELECT user_message, assistant_reply FROM chats WHERE username = ? ORDER BY id DESC LIMIT ?",
            (username, limit),
        ).fetchall()
        conn.close()

        return [
            {"user_message": user_message, "assistant_reply": assistant_reply}
            for user_message, assistant_reply in rows
        ]
