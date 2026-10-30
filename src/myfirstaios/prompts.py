from __future__ import annotations

from pathlib import Path


DEFAULT_SYSTEM_PROMPT = """
You are a personal AI capability assistant.
Your job is to help organize prompts, tools, and workflows for personal productivity.
Stay concise, practical, and useful.
"""

task_prompt_template = """
User request:
{user_input}

Please provide a helpful, structured response.
"""


def read_prompt_file(filename: str) -> str:
    base_dir = Path(__file__).resolve().parents[2]
    prompt_path = base_dir / "prompts" / filename
    return prompt_path.read_text(encoding="utf-8")
