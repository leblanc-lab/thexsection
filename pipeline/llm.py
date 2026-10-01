"""Provider layer: one completion interface over Anthropic (production),
Gemini (free-tier dev/testing) and the Claude Code CLI (`claude -p`, billed to
the local subscription rather than API credit). Selected by `llm.provider` in
config.yaml.

Prompts are plain markdown in/out; nothing provider-specific leaks upstream.
"""

from __future__ import annotations

import sys
import time
from dataclasses import dataclass

from .common import load_config


@dataclass
class LLMResult:
    text: str
    input_tokens: int
    output_tokens: int
    cost: float
    # True when the response hit max_tokens. Callers that can still use a
    # partial answer should degrade rather than discard it.
    truncated: bool = False


class BatchTimeout(RuntimeError):
    """A batch outran its wall-clock deadline and was cancelled.

    Raised by a backend's complete_batch; LLM.complete_batch catches it and
    re-runs the jobs synchronously when llm.batch_fallback_sync is on.
    """


class AnthropicBackend:
    # The Batches API bills all token usage at 50% of standard rates.
    batch_cost_multiplier = 0.5

    def __init__(self, model: str):
        import anthropic

        self.client = anthropic.Anthropic()
        self.model = model

    def complete(
        self, system: str, user: str, max_tokens: int
    ) -> tuple[str, int, int, bool]:
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
        truncated = msg.stop_reason == "max_tokens"
        if truncated:
            print(
                f"[llm] warning: output hit max_tokens ({max_tokens}) — response "
                f"truncated; raise the stage's max_output_tokens in config.yaml",
                file=sys.stderr,
            )
        text = "".join(b.text for b in msg.content if b.type == "text")
        return text, msg.usage.input_tokens, msg.usage.output_tokens, truncated

    def complete_batch(
        self,
        jobs: dict[str, tuple[str, str, int]],
        poll_seconds: int = 15,
        deadline_seconds: float | None = None,
    ) -> dict[str, tuple[str, int, int, bool]]:
        """Submit one async batch, block until it finishes, return per-job results.

        `jobs` maps a caller-chosen id to (system, user, max_tokens); the return
        maps the same ids to (text, input_tokens, output_tokens). Delivery is
        async (no held HTTP connection), so the large-`max_tokens` streaming
        caveat doesn't apply — non-streaming params are fine here.

        `deadline_seconds` caps the wait: the API allows a batch up to 24h, far
        longer than a CI job lives, so an unbounded poll turns one slow batch
        into a lost run. On expiry the batch is cancelled (so we aren't billed
        for output nobody reads) and BatchTimeout is raised.
        """
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
        started = time.monotonic()
        while True:
            b = self.client.messages.batches.retrieve(batch.id)
            if b.processing_status == "ended":
                break
            waited = time.monotonic() - started
            if deadline_seconds is not None and waited >= deadline_seconds:
                # Cancel so in-flight requests stop billing; already-finished
                # ones in this batch are lost either way since we can't wait.
                try:
                    self.client.messages.batches.cancel(batch.id)
                except Exception as exc:  # cancellation is best-effort
                    print(
                        f"[llm] batch {batch.id}: cancel failed ({exc})",
                        file=sys.stderr,
                    )
                raise BatchTimeout(
                    f"batch {batch.id} still {b.processing_status} after "
                    f"{waited / 60:.1f} min (deadline {deadline_seconds / 60:.0f} min); "
                    f"cancelled with {b.request_counts.processing} request(s) unfinished"
                )
            print(
                f"[llm] batch {batch.id}: {b.processing_status}, "
                f"{b.request_counts.processing} still processing "
                f"({waited / 60:.1f} min elapsed)",
                file=sys.stderr,
            )
            time.sleep(poll_seconds)

        # Results arrive in arbitrary order — key by custom_id, never by position.
        out: dict[str, tuple[str, int, int, bool]] = {}
        for r in self.client.messages.batches.results(batch.id):
            if r.result.type != "succeeded":
                raise RuntimeError(
                    f"batch request {r.custom_id} {r.result.type} (not succeeded)"
                )
            msg = r.result.message
            if msg.stop_reason == "refusal":
                raise RuntimeError(f"model refused ({r.custom_id}): {msg.stop_details}")
            truncated = msg.stop_reason == "max_tokens"
            if truncated:
                print(
                    f"[llm] warning: {r.custom_id} hit max_tokens "
                    f"({jobs[r.custom_id][2]}) — response truncated; raise the "
                    f"stage's max_output_tokens in config.yaml",
                    file=sys.stderr,
                )
            text = "".join(b.text for b in msg.content if b.type == "text")
            out[r.custom_id] = (
                text,
                msg.usage.input_tokens,
                msg.usage.output_tokens,
                truncated,
            )

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

    def complete(
        self, system: str, user: str, max_tokens: int
    ) -> tuple[str, int, int, bool]:
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
        truncated = False
        if resp.candidates and str(resp.candidates[0].finish_reason) not in (
            "FinishReason.STOP",
            "STOP",
        ):
            finish = str(resp.candidates[0].finish_reason)
            truncated = finish.endswith("MAX_TOKENS")
            print(f"[llm] warning: finish_reason={finish}", file=sys.stderr)
        usage = resp.usage_metadata
        out_tokens = (usage.candidates_token_count or 0) + (
            usage.thoughts_token_count or 0
        )
        return resp.text or "", usage.prompt_token_count or 0, out_tokens, truncated

    def complete_batch(
        self,
        jobs: dict[str, tuple[str, str, int]],
        poll_seconds: int = 15,
        deadline_seconds: float | None = None,
    ) -> dict[str, tuple[str, int, int, bool]]:
        # No Gemini batch endpoint here — just run the jobs synchronously so the
        # interface matches AnthropicBackend. Keeps the free-tier dev path simple.
        # Runs inline, so there is no deadline to enforce.
        return {
            cid: self.complete(system, user, max_tokens)
            for cid, (system, user, max_tokens) in jobs.items()
        }

    def count_tokens(self, system: str, user: str) -> int:
        resp = self.client.models.count_tokens(
            model=self.model, contents=[system, user]
        )
        return resp.total_tokens or 0


class ClaudeCLIBackend:
    """Shell out to the Claude Code CLI (`claude -p`) for each completion.

    A fallback for when API credit runs out: the CLI is authenticated against
    the local subscription, so runs cost nothing on the API balance. No batch
    endpoint; complete_batch loops synchronously. Only usable where the CLI is
    installed and logged in, i.e. a laptop, not CI.
    """

    batch_cost_multiplier = 1.0

    def __init__(self, model: str, binary: str = "claude"):
        import shutil

        self.binary = shutil.which(binary) or binary
        self.model = model

    def complete(
        self, system: str, user: str, max_tokens: int
    ) -> tuple[str, int, int, bool]:
        import json
        import os
        import subprocess

        # Running inside a Claude Code session sets CLAUDECODE; a nested `claude`
        # refuses to start unless it is cleared.
        env = {k: v for k, v in os.environ.items() if k != "CLAUDECODE"}
        cmd = [
            self.binary,
            "-p",
            "--model", self.model,
            "--system-prompt", system,
            "--tools", "",
            "--output-format", "json",
        ]
        proc = subprocess.run(
            cmd, input=user, capture_output=True, text=True, env=env, check=False
        )
        if proc.returncode != 0:
            raise RuntimeError(
                f"claude CLI exited {proc.returncode}: {proc.stderr.strip()[:2000]}"
            )
        try:
            payload = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                f"claude CLI returned non-JSON output: {proc.stdout[:500]}"
            ) from exc
        if payload.get("is_error") or payload.get("subtype") != "success":
            raise RuntimeError(f"claude CLI error: {payload.get('result', payload)}")
        text = payload.get("result") or ""
        usage = payload.get("usage") or {}
        tokens_in = (
            (usage.get("input_tokens") or 0)
            + (usage.get("cache_creation_input_tokens") or 0)
            + (usage.get("cache_read_input_tokens") or 0)
        )
        tokens_out = usage.get("output_tokens") or 0
        # The CLI has its own output ceiling; report truncation only when the
        # model itself stopped for length.
        truncated = payload.get("stop_reason") == "max_tokens"
        if truncated:
            print(
                f"[llm] warning: CLI response stopped at max_tokens — truncated",
                file=sys.stderr,
            )
        return text, tokens_in, tokens_out, truncated

    def complete_batch(
        self,
        jobs: dict[str, tuple[str, str, int]],
        poll_seconds: int = 15,
        deadline_seconds: float | None = None,
    ) -> dict[str, tuple[str, int, int, bool]]:
        return {
            cid: self.complete(system, user, max_tokens)
            for cid, (system, user, max_tokens) in jobs.items()
        }

    def count_tokens(self, system: str, user: str) -> int:
        # No counting endpoint through the CLI; callers fall back to chars/4.
        raise NotImplementedError("claude CLI cannot count tokens")


class LLM:
    def __init__(self, cfg: dict | None = None):
        import os

        llm_cfg = (cfg or load_config())["llm"]
        # LLM_PROVIDER overrides config.yaml for one run (e.g. a hand-run day on
        # `claude-cli` while the committed default stays `anthropic` for CI).
        self.provider = os.environ.get("LLM_PROVIDER") or llm_cfg["provider"]
        # When true, route calls through the async Batches API (50% cheaper,
        # higher latency). Off by default so local runs stay synchronous/snappy.
        self.batch = llm_cfg.get("batch", False)
        # Cap the batch wait well under the CI job limit, and decide what to do
        # when we hit it: fall back to synchronous calls (full price, but the
        # run still produces a digest) or fail the run outright.
        self.batch_deadline_seconds = llm_cfg.get("batch_deadline_minutes", 45) * 60
        self.batch_fallback_sync = llm_cfg.get("batch_fallback_sync", True)
        # LLM_RUN_DEADLINE (unix seconds) bounds batch waiting across the whole
        # run. Stages are separate sequential processes, so a per-batch cap
        # alone lets several slow batches stack past the CI job limit (lost
        # runs 2026-09-30 and 2026-10-01: 45 + 45 + ... > 120 min).
        run_deadline = os.environ.get("LLM_RUN_DEADLINE")
        self.run_deadline = float(run_deadline) if run_deadline else None
        pcfg = llm_cfg["providers"][self.provider]
        self.model = pcfg["model"]
        self.in_price = pcfg["input_price_per_mtok"]
        self.out_price = pcfg["output_price_per_mtok"]
        backend_cls = {
            "anthropic": AnthropicBackend,
            "gemini": GeminiBackend,
            "claude-cli": ClaudeCLIBackend,
        }[self.provider]
        self.backend = backend_cls(self.model)

    def _finish(
        self,
        tokens_in: int,
        tokens_out: int,
        text: str,
        multiplier: float,
        truncated: bool = False,
    ) -> LLMResult:
        cost = (tokens_in * self.in_price + tokens_out * self.out_price) / 1e6 * multiplier
        tag = " (batch -50%)" if multiplier < 1 else ""
        print(
            f"[llm] {self.provider}/{self.model}: {tokens_in} in, "
            f"{tokens_out} out, ${cost:.4f}{tag}",
            file=sys.stderr,
        )
        return LLMResult(text, tokens_in, tokens_out, cost, truncated)

    def complete(self, system: str, user: str, max_tokens: int) -> LLMResult:
        if self.batch:
            return self.complete_batch({"request": (system, user, max_tokens)})["request"]
        text, tokens_in, tokens_out, truncated = self.backend.complete(
            system, user, max_tokens
        )
        return self._finish(tokens_in, tokens_out, text, 1.0, truncated)

    def complete_batch(
        self, jobs: dict[str, tuple[str, str, int]]
    ) -> dict[str, LLMResult]:
        """Run several independent completions as one batch; keyed by caller id.

        A batch that outruns its deadline degrades to synchronous calls rather
        than stalling the run: the digest is worth more than the 50% discount.
        Once the run-wide budget (LLM_RUN_DEADLINE) is spent, batching is
        skipped outright and calls go straight to synchronous.
        """
        deadline = self.batch_deadline_seconds
        if self.run_deadline is not None:
            deadline = min(deadline, self.run_deadline - time.time())
        try:
            if deadline < 60:
                raise BatchTimeout(
                    "run-wide batch budget (LLM_RUN_DEADLINE) spent; not submitting a batch"
                )
            raw = self.backend.complete_batch(jobs, deadline_seconds=deadline)
            mult = self.backend.batch_cost_multiplier
        except BatchTimeout as exc:
            if not self.batch_fallback_sync:
                raise
            print(
                f"[llm] {exc}\n[llm] falling back to synchronous calls for "
                f"{len(jobs)} request(s) at full price",
                file=sys.stderr,
            )
            raw = {
                cid: self.backend.complete(system, user, max_tokens)
                for cid, (system, user, max_tokens) in jobs.items()
            }
            mult = 1.0
        return {
            cid: self._finish(tokens_in, tokens_out, text, mult, truncated)
            for cid, (text, tokens_in, tokens_out, truncated) in raw.items()
        }

    def count_tokens(self, system: str, user: str) -> int:
        return self.backend.count_tokens(system, user)

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        mult = self.backend.batch_cost_multiplier if self.batch else 1.0
        return (input_tokens * self.in_price + output_tokens * self.out_price) / 1e6 * mult
