from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import os

from dotenv import load_dotenv


@lru_cache(maxsize=1)
def load_environment() -> None:
    load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env", override=False)


@dataclass(frozen=True)
class Settings:
    app_name: str = "myFirstAIOS"
    environment: str = "development"
    llm_provider: str = "openai"
    llm_model: str = "gpt-4o-mini"
    api_key: str | None = None
    ollama_url: str = "http://localhost:11434"

    @classmethod
    def from_env(cls) -> "Settings":
        load_environment()
        return cls(
            app_name=os.getenv("APP_NAME", "myFirstAIOS"),
            environment=os.getenv("APP_ENV", "development"),
            llm_provider=os.getenv("LLM_PROVIDER", "openai"),
            llm_model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
            api_key=os.getenv("OPENAI_API_KEY"),
            ollama_url=os.getenv("OLLAMA_URL", "http://localhost:11434"),
        )


settings = Settings.from_env()
