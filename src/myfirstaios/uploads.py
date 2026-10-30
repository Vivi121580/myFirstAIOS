from __future__ import annotations

from pathlib import Path

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_upload(file_name: str, content: bytes) -> str:
    safe_name = Path(file_name).name
    target = UPLOAD_DIR / safe_name
    with open(target, "wb") as f:
        f.write(content)
    return str(target)
