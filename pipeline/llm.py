"""Provider layer: one completion interface over Anthropic (production) and
Gemini (free-tier dev/testing). Selected by `llm.provider` in config.yaml.

Prompts are plain markdown in/out; nothing provider-specific leaks upstream.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass

from .common import load_config


@dataclass
class LLMResult:
    text: str
    input_tokens: int
    output_tokens: int
    cost: float


class AnthropicBackend:
    def __init__(self, model: str):
        import anthropic

        self.client = anthropic.Anthropic()
        self.model = model

    def complete(self, system: str, user: str, max_tokens: int) -> tuple[str, int, int]:
        with self.client.messages.stream(
            model=self.model,
            max_tokens=max_tokens,
            thinking={"type": "adaptive"},
            output_config={"effort": "high"},
            system=[{"type": "text", "text": system}],
            messages=[{"role": "user", "content": user}],
        ) as stream:
            msg = stream.get_final_message()
        if msg.stop_reason == "refusal":
            raise RuntimeError(f"model refused: {msg.stop_details}")
        text = "".join(b.text for b in msg.content if b.type == "text")
        return text, msg.usage.input_tokens, msg.usage.output_tokens

    def count_tokens(self, system: str, user: str) -> int:
        resp = self.client.messages.count_tokens(
            model=self.model,
            system=[{"type": "text", "text": system}],
            messages=[{"role": "user", "content": user}],
        )
        return resp.input_tokens


class GeminiBackend:
    def __init__(self, model: str):
        from google import genai

        self.client = genai.Client()  # reads GEMINI_API_KEY
        self.model = model

    def complete(self, system: str, user: str, max_tokens: int) -> tuple[str, int, int]:
        from google.genai import types

        # Gemini counts internal "thinking" tokens against max_output_tokens,
        # so a tight cap truncates the visible answer. Free tier: give headroom.
        resp = self.client.models.generate_content(
            model=self.model,
            contents=user,
            config=types.GenerateContentConfig(
                system_instruction=system,
                max_output_tokens=max(max_tokens * 8, 32000),
            ),
        )
        if resp.candidates and str(resp.candidates[0].finish_reason) not in (
            "FinishReason.STOP",
            "STOP",
        ):
            print(
                f"[llm] warning: finish_reason={resp.candidates[0].finish_reason}",
                file=sys.stderr,
            )
        usage = resp.usage_metadata
        out_tokens = (usage.candidates_token_count or 0) + (
            usage.thoughts_token_count or 0
        )
        return resp.text or "", usage.prompt_token_count or 0, out_tokens

    def count_tokens(self, system: str, user: str) -> int:
        resp = self.client.models.count_tokens(
            model=self.model, contents=[system, user]
        )
        return resp.total_tokens or 0


class LLM:
    def __init__(self, cfg: dict | None = None):
        llm_cfg = (cfg or load_config())["llm"]
        self.provider = llm_cfg["provider"]
        pcfg = llm_cfg["providers"][self.provider]
        self.model = pcfg["model"]
        self.in_price = pcfg["input_price_per_mtok"]
        self.out_price = pcfg["output_price_per_mtok"]
        backend_cls = {"anthropic": AnthropicBackend, "gemini": GeminiBackend}[
            self.provider
        ]
        self.backend = backend_cls(self.model)

    def complete(self, system: str, user: str, max_tokens: int) -> LLMResult:
        text, tokens_in, tokens_out = self.backend.complete(system, user, max_tokens)
        cost = (tokens_in * self.in_price + tokens_out * self.out_price) / 1e6
        print(
            f"[llm] {self.provider}/{self.model}: {tokens_in} in, "
            f"{tokens_out} out, ${cost:.4f}",
            file=sys.stderr,
        )
        return LLMResult(text, tokens_in, tokens_out, cost)

    def count_tokens(self, system: str, user: str) -> int:
        return self.backend.count_tokens(system, user)

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        return (input_tokens * self.in_price + output_tokens * self.out_price) / 1e6
