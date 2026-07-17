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
    # The Batches API bills all token usage at 50% of standard rates.
    batch_cost_multiplier = 0.5

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
        if msg.stop_reason == "max_tokens":
            print(
                f"[llm] warning: output hit max_tokens ({max_tokens}) — response "
                f"truncated; raise the stage's max_output_tokens in config.yaml",
                file=sys.stderr,
            )
        text = "".join(b.text for b in msg.content if b.type == "text")
        return text, msg.usage.input_tokens, msg.usage.output_tokens

    def complete_batch(
        self, jobs: dict[str, tuple[str, str, int]], poll_seconds: int = 15
    ) -> dict[str, tuple[str, int, int]]:
        """Submit one async batch, block until it finishes, return per-job results.

        `jobs` maps a caller-chosen id to (system, user, max_tokens); the return
        maps the same ids to (text, input_tokens, output_tokens). Delivery is
        async (no held HTTP connection), so the large-`max_tokens` streaming
        caveat doesn't apply — non-streaming params are fine here.
        """
        import time

        from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
        from anthropic.types.messages.batch_create_params import Request

        batch = self.client.messages.batches.create(
            requests=[
                Request(
                    custom_id=cid,
                    params=MessageCreateParamsNonStreaming(
                        model=self.model,
                        max_tokens=max_tokens,
                        thinking={"type": "adaptive"},
                        output_config={"effort": "high"},
                        system=[{"type": "text", "text": system}],
                        messages=[{"role": "user", "content": user}],
                    ),
                )
                for cid, (system, user, max_tokens) in jobs.items()
            ]
        )
        print(
            f"[llm] batch {batch.id}: submitted {len(jobs)} request(s)",
            file=sys.stderr,
        )
        while True:
            b = self.client.messages.batches.retrieve(batch.id)
            if b.processing_status == "ended":
                break
            print(
                f"[llm] batch {batch.id}: {b.processing_status}, "
                f"{b.request_counts.processing} still processing",
                file=sys.stderr,
            )
            time.sleep(poll_seconds)

        # Results arrive in arbitrary order — key by custom_id, never by position.
        out: dict[str, tuple[str, int, int]] = {}
        for r in self.client.messages.batches.results(batch.id):
            if r.result.type != "succeeded":
                raise RuntimeError(
                    f"batch request {r.custom_id} {r.result.type} (not succeeded)"
                )
            msg = r.result.message
            if msg.stop_reason == "refusal":
                raise RuntimeError(f"model refused ({r.custom_id}): {msg.stop_details}")
            if msg.stop_reason == "max_tokens":
                print(
                    f"[llm] warning: {r.custom_id} hit max_tokens "
                    f"({jobs[r.custom_id][2]}) — response truncated; raise the "
                    f"stage's max_output_tokens in config.yaml",
                    file=sys.stderr,
                )
            text = "".join(b.text for b in msg.content if b.type == "text")
            out[r.custom_id] = (text, msg.usage.input_tokens, msg.usage.output_tokens)

        missing = set(jobs) - set(out)
        if missing:
            raise RuntimeError(f"batch {batch.id} returned no result for {sorted(missing)}")
        return out

    def count_tokens(self, system: str, user: str) -> int:
        resp = self.client.messages.count_tokens(
            model=self.model,
            system=[{"type": "text", "text": system}],
            messages=[{"role": "user", "content": user}],
        )
        return resp.input_tokens


class GeminiBackend:
    # No batch endpoint wired up here; complete_batch loops synchronously, so
    # there's no discount to apply (the free tier is $0 anyway).
    batch_cost_multiplier = 1.0

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

    def complete_batch(
        self, jobs: dict[str, tuple[str, str, int]]
    ) -> dict[str, tuple[str, int, int]]:
        # No Gemini batch endpoint here — just run the jobs synchronously so the
        # interface matches AnthropicBackend. Keeps the free-tier dev path simple.
        return {
            cid: self.complete(system, user, max_tokens)
            for cid, (system, user, max_tokens) in jobs.items()
        }

    def count_tokens(self, system: str, user: str) -> int:
        resp = self.client.models.count_tokens(
            model=self.model, contents=[system, user]
        )
        return resp.total_tokens or 0


class LLM:
    def __init__(self, cfg: dict | None = None):
        llm_cfg = (cfg or load_config())["llm"]
        self.provider = llm_cfg["provider"]
        # When true, route calls through the async Batches API (50% cheaper,
        # higher latency). Off by default so local runs stay synchronous/snappy.
        self.batch = llm_cfg.get("batch", False)
        pcfg = llm_cfg["providers"][self.provider]
        self.model = pcfg["model"]
        self.in_price = pcfg["input_price_per_mtok"]
        self.out_price = pcfg["output_price_per_mtok"]
        backend_cls = {"anthropic": AnthropicBackend, "gemini": GeminiBackend}[
            self.provider
        ]
        self.backend = backend_cls(self.model)

    def _finish(
        self, tokens_in: int, tokens_out: int, text: str, multiplier: float
    ) -> LLMResult:
        cost = (tokens_in * self.in_price + tokens_out * self.out_price) / 1e6 * multiplier
        tag = " (batch -50%)" if multiplier < 1 else ""
        print(
            f"[llm] {self.provider}/{self.model}: {tokens_in} in, "
            f"{tokens_out} out, ${cost:.4f}{tag}",
            file=sys.stderr,
        )
        return LLMResult(text, tokens_in, tokens_out, cost)

    def complete(self, system: str, user: str, max_tokens: int) -> LLMResult:
        if self.batch:
            return self.complete_batch({"request": (system, user, max_tokens)})["request"]
        text, tokens_in, tokens_out = self.backend.complete(system, user, max_tokens)
        return self._finish(tokens_in, tokens_out, text, 1.0)

    def complete_batch(
        self, jobs: dict[str, tuple[str, str, int]]
    ) -> dict[str, LLMResult]:
        """Run several independent completions as one batch; keyed by caller id."""
        raw = self.backend.complete_batch(jobs)
        mult = self.backend.batch_cost_multiplier
        return {
            cid: self._finish(tokens_in, tokens_out, text, mult)
            for cid, (text, tokens_in, tokens_out) in raw.items()
        }

    def count_tokens(self, system: str, user: str) -> int:
        return self.backend.count_tokens(system, user)

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        mult = self.backend.batch_cost_multiplier if self.batch else 1.0
        return (input_tokens * self.in_price + output_tokens * self.out_price) / 1e6 * mult
