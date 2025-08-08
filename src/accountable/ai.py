"""Lightweight AI service using OpenAI's API.

The service is optional and only activated when an API key is provided.
"""

from __future__ import annotations

import os
from typing import Optional

try:
    import openai  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    openai = None


class AiClient:
    def __init__(self, api_key: Optional[str] = None) -> None:
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if openai and self.api_key:
            openai.api_key = self.api_key

    def _chat(self, prompt: str) -> str:
        if not openai or not self.api_key:
            raise RuntimeError("OpenAI not configured")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"].strip()

    def generate_plan(self, topic: str) -> str:
        """Generate a basic learning plan for the given topic."""
        return self._chat(f"Create a concise learning plan for {topic}.")

    def summarize_reflection(self, text: str) -> str:
        """Return a short summary of the reflection text."""
        return self._chat(f"Summarize the following reflection:\n{text}")
