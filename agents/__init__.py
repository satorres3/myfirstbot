"""Pluggable AI agent backends.

This package exposes a minimal interface for adding new LLM providers. Each
provider should implement a `generate(prompt: str) -> str` function.
"""

from typing import Protocol


class Agent(Protocol):
    """Simple protocol all agents must follow."""

    def generate(self, prompt: str) -> str:  # pragma: no cover - interface only
        ...
