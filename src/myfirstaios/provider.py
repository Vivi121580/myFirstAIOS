from __future__ import annotations

from dataclasses import dataclass


class LLMProvider:
    def generate(self, system_prompt: str, user_input: str) -> str:
        raise NotImplementedError


@dataclass
class OpenAIConfig:
    api_key: str
    model: str = "gpt-4o-mini"
    base_url: str | None = None


class OpenAIProvider:
    def __init__(self, config: OpenAIConfig) -> None:
        self.config = config
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise RuntimeError("Install openai: pip install openai") from exc
        self.client = OpenAI(api_key=config.api_key, base_url=config.base_url)

    def generate(self, system_prompt: str, user_input: str) -> str:
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content or ""


@dataclass
class OllamaConfig:
    model: str = "llama3.1"
    base_url: str = "http://localhost:11434"


class OllamaProvider:
    def __init__(self, config: OllamaConfig) -> None:
        self.config = config

    def generate(self, system_prompt: str, user_input: str) -> str:
        import requests

        payload = {
            "model": self.config.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input},
            ],
            "stream": False,
        }

        response = requests.post(
            f"{self.config.base_url}/api/chat",
            json=payload,
            timeout=120,
        )
        response.raise_for_status()
        data = response.json()
        return data.get("message", {}).get("content", "")
