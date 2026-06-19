from __future__ import annotations

import json
import logging
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "data" / "reports"
RAW_DIR = ROOT / "data" / "raw"
LATEST_FILE = PROCESSED_DIR / "hip4_outcome_latest.json"
HISTORY_FILE = PROCESSED_DIR / "hip4_outcome_history.json"
REPORT_FILE = REPORT_DIR / "latest_hip4_outcome.md"

DEFAULT_INFO_URL = "https://api.hyperliquid.xyz/info"
DEFAULT_TIMEOUT = 15
DEFAULT_HISTORY_MAX_RECORDS = 720
DEFAULT_HISTORY_MAX_BYTES = 80_000_000

logger = logging.getLogger(__name__)


def update_hip4_outcome_snapshot(now: datetime) -> dict[str, Any]:
    if os.getenv("HIP4_OUTCOME_ENABLED", "true").lower() == "false":
        return {"enabled": False, "reason": "HIP4_OUTCOME_ENABLED=false"}

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    info_url = os.getenv("HIP4_INFO_URL", DEFAULT_INFO_URL).strip() or DEFAULT_INFO_URL
    timeout = int(os.getenv("HIP4_REQUEST_TIMEOUT", str(DEFAULT_TIMEOUT)))
    top_limit = int(os.getenv("HIP4_TOP_LIMIT", "25"))
    history_max = int(os.getenv("HIP4_HISTORY_MAX_RECORDS", str(DEFAULT_HISTORY_MAX_RECORDS)))
    history_max_bytes = int(os.getenv("HIP4_HISTORY_MAX_BYTES", str(DEFAULT_HISTORY_MAX_BYTES)))

    meta_payload, meta_error = post_info(info_url, {"type": "outcomeMeta"}, timeout)

    # Try several known and candidate endpoint shapes for asset contexts.
    # HIP-4 launched 2026-05-02 and the live shape differs from perps/spot.
    ctx_candidates: list[tuple[str, dict[str, Any]]] = [
        ("outcomeMetaAndAssetCtxs", {"type": "outcomeMetaAndAssetCtxs"}),
        ("outcomeAssetCtxs", {"type": "outcomeAssetCtxs"}),
    ]
    # Add per-outcome candidates when we already know which outcomes exist.
    known_outcomes = extract_outcomes(meta_payload, None)
    for outcome in known_outcomes[:5]:
        outcome_id = (
            outcome.get("outcome") or outcome.get("outcomeId") or outcome.get("id")
        )
        if outcome_id is None:
            continue
        ctx_candidates.extend(
            [
                (f"outcomeAssetCtxs[{outcome_id}]", {"type": "outcomeAssetCtxs", "outcome": outcome_id}),
                (f"outcomeAssetCtx[{outcome_id}]", {"type": "outcomeAssetCtx", "outcome": outcome_id}),
                (f"outcomeState[{outcome_id}]", {"type": "outcomeState", "outcome": outcome_id}),
            ]
        )

    ctx_payload: Any = None
    ctx_error: str | None = None
    ctx_attempts: list[str] = []
    for label, body in ctx_candidates:
        payload, error = post_info(info_url, body, timeout)
        ctx_attempts.append(f"{label}: {'ok' if error is None else error}")
        if error is None and payload is not None:
            ctx_payload = payload
            ctx_error = None
            save_raw_payload(now, f"ctx_ok_{label}", payload, None)
            break
        ctx_error = error

    # Always fetch allMids; HIP-4 outcome tokens appear as "#<encoding>" keys.
    mids_payload, mids_error = post_info(info_url, {"type": "allMids"}, timeout)

    save_raw_payload(now, "outcome_meta", meta_payload, meta_error)
    save_raw_payload(now, "ctx_attempts", {"attempts": ctx_attempts, "last_error": ctx_error}, None)
    save_raw_payload(now, "all_mids", mids_payload, mids_error)

    outcomes = extract_outcomes(meta_payload, ctx_payload)
    asset_ctxs = extract_asset_ctxs(ctx_payload)
    all_mids = mids_payload if isinstance(mids_payload, dict) else {}
    rows = build_rows(outcomes, asset_ctxs, all_mids)
    aggregates = aggregate_rows(rows)
    request_errors = [err for err in (meta_error, mids_error) if err]
    request_warnings = [ctx_error] if ctx_error else []

    latest = {
        "generated_at": now.isoformat(),
        "info_url": info_url,
        "source_status": {
            "outcome_meta": "ok" if meta_error is None else "error",
            "asset_context": "ok" if ctx_payload is not None else "unavailable",
            "all_mids": "ok" if mids_error is None else "error",
        },
        "request_errors": request_errors,
        "request_warnings": request_warnings,
        "outcome_count": aggregates["outcome_count"],
        "side_count": len(rows),
        "by_underlying": aggregates["by_underlying"],
        "by_class": aggregates["by_class"],
        "by_status": aggregates["by_status"],
        "rows": rows,
    }

    LATEST_FILE.write_text(json.dumps(latest, indent=2, ensure_ascii=False), encoding="utf-8")
    history_records = append_history(now, latest, history_max, history_max_bytes)
    REPORT_FILE.write_text(render_report(latest, top_limit), encoding="utf-8")
    logger.info(
        "Wrote %s (outcomes=%s, sides=%s)",
        LATEST_FILE,
        latest["outcome_count"],
        latest["side_count"],
    )

    return {
        "enabled": True,
        "updated_at": now.isoformat(),
        "outcome_count": latest["outcome_count"],
        "side_count": latest["side_count"],
        "history_records": history_records,
        "request_errors": latest["request_errors"],
        "request_warnings": latest["request_warnings"],
        "latest_file": "data/processed/hip4_outcome_latest.json",
        "history_file": "data/processed/hip4_outcome_history.json",
        "report_file": "data/reports/latest_hip4_outcome.md",
        "by_underlying": latest["by_underlying"],
        "by_class": latest["by_class"],
        "top_by_implied_probability": top_rows(rows, "implied_probability", top_limit, abs_value=False),
        "top_by_volume_24h": top_rows(rows, "volume_24h", top_limit, abs_value=False),
        "top_by_open_interest": top_rows(rows, "open_interest", top_limit, abs_value=False),
    }


def post_info(url: str, body: dict[str, Any], timeout: int) -> tuple[Any, str | None]:
    try:
        response = requests.post(
            url,
            json=body,
            headers={"Content-Type": "application/json"},
            timeout=timeout,
        )
        response.raise_for_status()
        return response.json(), None
    except Exception as e:
        message = f"{body.get('type')}: {e}"
        logger.warning("HIP-4 info request failed (%s)", message)
        return None, message


def save_raw_payload(now: datetime, label: str, payload: Any, error: str | None) -> None:
    if payload is None and error is None:
        return
    raw_dir = RAW_DIR / now.strftime("%Y-%m-%d")
    raw_dir.mkdir(parents=True, exist_ok=True)
    target = raw_dir / f"hip4_{label}_{now.strftime('%H%M%S')}.json"
    body: dict[str, Any] = {"label": label}
    if payload is not None:
        body["payload"] = payload
    if error is not None:
        body["error"] = error
    target.write_text(json.dumps(body, indent=2, ensure_ascii=False), encoding="utf-8")


def extract_outcomes(meta_payload: Any, ctx_payload: Any) -> list[dict[str, Any]]:
    candidates: list[Any] = []

    if isinstance(meta_payload, dict):
        candidates.extend(_outcomes_from_meta(meta_payload))
    if isinstance(meta_payload, list):
        candidates.extend(_outcomes_from_list(meta_payload))

    if not candidates and isinstance(ctx_payload, list) and ctx_payload:
        if isinstance(ctx_payload[0], dict):
            candidates.extend(_outcomes_from_meta(ctx_payload[0]))
    if not candidates and isinstance(ctx_payload, dict):
        candidates.extend(_outcomes_from_meta(ctx_payload))

    return [item for item in candidates if isinstance(item, dict)]


def _outcomes_from_meta(meta: dict[str, Any]) -> list[Any]:
    for key in ("outcomes", "universe", "outcomeMarkets", "markets"):
        value = meta.get(key)
        if isinstance(value, list) and value:
            return value
    return []


def _outcomes_from_list(payload: list[Any]) -> list[Any]:
    if not payload:
        return []
    head = payload[0]
    if isinstance(head, dict) and any(
        key in head for key in ("outcome", "outcomeId", "name", "sideSpecs")
    ):
        return payload
    if isinstance(head, dict):
        for inner in head.values():
            if isinstance(inner, list):
                return inner
    return []


def extract_asset_ctxs(ctx_payload: Any) -> list[Any]:
    if isinstance(ctx_payload, list) and len(ctx_payload) >= 2 and isinstance(ctx_payload[1], list):
        return ctx_payload[1]
    if isinstance(ctx_payload, dict):
        for key in ("assetCtxs", "outcomeAssetCtxs", "ctxs"):
            value = ctx_payload.get(key)
            if isinstance(value, list):
                return value
    return []


def build_rows(
    outcomes: list[dict[str, Any]],
    asset_ctxs: list[Any],
    all_mids: dict[str, Any] | None = None,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    asset_index = 0
    all_mids = all_mids if isinstance(all_mids, dict) else {}

    for outcome in outcomes:
        outcome_id = outcome.get("outcome")
        if outcome_id is None:
            outcome_id = outcome.get("outcomeId") or outcome.get("id")
        outcome_int = to_int(outcome_id)
        name = outcome.get("name") or outcome.get("question")
        description = outcome.get("description")
        underlying = derive_underlying(name, description)
        outcome_class = derive_class(description, name)
        expiry = derive_expiry(description, outcome)
        target_price = derive_target_price(description, outcome)
        period = derive_period(description, outcome)
        status = outcome.get("status") or outcome.get("state")

        side_specs = outcome.get("sideSpecs") or outcome.get("sides") or []
        if not isinstance(side_specs, list) or not side_specs:
            side_specs = [{"name": "Yes"}, {"name": "No"}]

        for side_index, side in enumerate(side_specs):
            if not isinstance(side, dict):
                side = {"name": str(side)}
            side_name = side.get("name") or ("Yes" if side_index == 0 else "No")
            ctx = (
                asset_ctxs[asset_index]
                if asset_index < len(asset_ctxs) and isinstance(asset_ctxs[asset_index], dict)
                else {}
            )
            asset_index += 1

            encoding = derive_outcome_encoding(outcome_int, side_index, side, ctx)
            symbol = derive_outcome_symbol(encoding, side, ctx)
            all_mids_price = to_float_or_none(all_mids.get(symbol)) if symbol else None
            mark_ctx = first_float(ctx.get("markPx"), ctx.get("mark"))
            mid_ctx = first_float(ctx.get("midPx"), ctx.get("mid"))
            mark = mark_ctx if mark_ctx is not None else all_mids_price
            mid = mid_ctx if mid_ctx is not None else all_mids_price
            best_bid = first_float(ctx.get("bestBidPx"), ctx.get("bidPx"))
            best_ask = first_float(ctx.get("bestAskPx"), ctx.get("askPx"))
            implied_probability = probability_from_prices(mark, mid)
            price_source = "asset_ctx" if mark_ctx is not None or mid_ctx is not None else (
                "allMids" if all_mids_price is not None else None
            )
            asset_id = (
                side.get("assetId")
                or ctx.get("assetId")
                or (100_000_000 + encoding if encoding is not None else None)
            )

            rows.append(
                {
                    "outcome_id": outcome_id,
                    "outcome_name": name,
                    "outcome_class": outcome_class,
                    "underlying": underlying,
                    "expiry": expiry,
                    "target_price": target_price,
                    "period": period,
                    "status": status,
                    "side_index": side_index,
                    "side_name": side_name,
                    "symbol": symbol,
                    "encoding": encoding,
                    "asset_id": asset_id,
                    "token_index": side.get("tokenIndex") or side.get("index") or encoding,
                    "mark_price": mark,
                    "mid_price": mid,
                    "best_bid": best_bid,
                    "best_ask": best_ask,
                    "implied_probability": implied_probability,
                    "price_source": price_source,
                    "volume_24h": to_float(ctx.get("dayNtlVlm") or ctx.get("dayVlm") or ctx.get("volume24h")),
                    "open_interest": to_float(ctx.get("openInterest") or ctx.get("oi")),
                    "raw_outcome": {k: v for k, v in outcome.items() if k != "sideSpecs"},
                    "raw_side_spec": side,
                    "raw_ctx": ctx,
                }
            )
    return rows


def derive_outcome_encoding(
    outcome_id: int | None,
    side_index: int,
    side: dict[str, Any],
    ctx: dict[str, Any],
) -> int | None:
    for value in (
        side.get("encoding"),
        side.get("tokenIndex"),
        side.get("index"),
        ctx.get("encoding"),
        ctx.get("tokenIndex"),
        ctx.get("index"),
    ):
        parsed = to_int(value)
        if parsed is not None:
            return parsed
    if outcome_id is None:
        return None
    return outcome_id * 10 + side_index


def derive_outcome_symbol(
    encoding: int | None,
    side: dict[str, Any],
    ctx: dict[str, Any],
) -> str | None:
    for value in (
        side.get("symbol"),
        side.get("coin"),
        side.get("nameOnExchange"),
        ctx.get("symbol"),
        ctx.get("coin"),
        ctx.get("name"),
    ):
        if isinstance(value, str) and value.startswith("#"):
            return value
    return f"#{encoding}" if encoding is not None else None


def probability_from_prices(mark: float | None, mid: float | None) -> float | None:
    for value in (mark, mid):
        if value is not None and 0 <= value <= 1:
            return value
    return None


def parse_description(description: Any) -> dict[str, str]:
    """Parse description: pipe-delimited 'key:value|key:value' string or dict."""
    if isinstance(description, dict):
        return {str(k): str(v) for k, v in description.items() if v is not None}
    if isinstance(description, str) and description:
        result = {}
        for part in description.split("|"):
            if ":" in part:
                key, _, value = part.partition(":")
                result[key.strip()] = value.strip()
        return result
    return {}


def derive_underlying(name: Any, description: Any) -> str | None:
    desc = parse_description(description)
    for key in ("underlying", "asset", "underlyingAsset", "symbol"):
        value = desc.get(key)
        if value:
            return str(value)
    if isinstance(name, str):
        for symbol in ("BTC", "ETH", "SOL", "HYPE", "BNB", "XRP", "DOGE"):
            if symbol in name.upper():
                return symbol
    return None


def derive_class(description: Any, name: Any) -> str | None:
    desc = parse_description(description)
    value = desc.get("class") or desc.get("type") or desc.get("category")
    if value:
        return str(value)
    if isinstance(description, str):
        text = description.strip().lower()
        if text == "other":
            return "fallback"
        if text.startswith("index:"):
            return "namedOutcome"
    if isinstance(name, str) and "ABOVE" in name.upper():
        return "price_above"
    if isinstance(name, str) and "BELOW" in name.upper():
        return "price_below"
    return None


def derive_expiry(description: Any, outcome: dict[str, Any]) -> str | None:
    desc = parse_description(description)
    for key in ("expiry", "expiresAt", "settlementTime", "endTime"):
        value = desc.get(key)
        if value:
            return str(value)
    for key in ("expiry", "expiresAt", "endTime"):
        value = outcome.get(key)
        if value:
            return str(value)
    return None


def derive_target_price(description: Any, outcome: dict[str, Any]) -> float | None:
    desc = parse_description(description)
    for key in ("targetPrice", "strike", "threshold"):
        value = desc.get(key)
        if value not in (None, ""):
            return to_float(value) or None
    for key in ("targetPrice", "strike"):
        value = outcome.get(key)
        if value not in (None, ""):
            return to_float(value) or None
    return None


def derive_period(description: Any, outcome: dict[str, Any]) -> str | None:
    desc = parse_description(description)
    for key in ("period", "interval", "frequency"):
        value = desc.get(key)
        if value:
            return str(value)
    for key in ("period", "interval"):
        value = outcome.get(key)
        if value:
            return str(value)
    return None


def aggregate_rows(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_underlying: dict[str, int] = {}
    by_class: dict[str, int] = {}
    by_status: dict[str, int] = {}
    seen_outcomes: set[Any] = set()

    for row in rows:
        outcome_id = row.get("outcome_id")
        if outcome_id is not None and outcome_id not in seen_outcomes:
            seen_outcomes.add(outcome_id)
            underlying = row.get("underlying") or "unknown"
            by_underlying[underlying] = by_underlying.get(underlying, 0) + 1
            outcome_class = row.get("outcome_class") or "unknown"
            by_class[outcome_class] = by_class.get(outcome_class, 0) + 1
            status = str(row.get("status") or "unknown")
            by_status[status] = by_status.get(status, 0) + 1

    return {
        "outcome_count": len(seen_outcomes) if seen_outcomes else len({r.get("outcome_id") for r in rows}),
        "by_underlying": by_underlying,
        "by_class": by_class,
        "by_status": by_status,
    }


def append_history(now: datetime, latest: dict[str, Any], max_records: int, max_bytes: int) -> int:
    history = load_history()
    bucket_minutes = int(os.getenv("HIP4_BUCKET_MINUTES", "15"))
    bucket = floor_time(now, bucket_minutes).isoformat()

    snapshot_rows = [
        {
            "outcome_id": row.get("outcome_id"),
            "outcome_name": row.get("outcome_name"),
            "side_index": row.get("side_index"),
            "side_name": row.get("side_name"),
            "symbol": row.get("symbol"),
            "encoding": row.get("encoding"),
            "asset_id": row.get("asset_id"),
            "underlying": row.get("underlying"),
            "outcome_class": row.get("outcome_class"),
            "implied_probability": row.get("implied_probability"),
            "mark_price": row.get("mark_price"),
            "mid_price": row.get("mid_price"),
            "price_source": row.get("price_source"),
            "volume_24h": row.get("volume_24h"),
            "open_interest": row.get("open_interest"),
        }
        for row in latest.get("rows", [])
    ]

    history.append(
        {
            "observed_at": bucket,
            "generated_at": latest["generated_at"],
            "outcome_count": latest["outcome_count"],
            "side_count": latest["side_count"],
            "by_underlying": latest["by_underlying"],
            "by_class": latest["by_class"],
            "by_status": latest["by_status"],
            "request_errors": latest["request_errors"],
            "request_warnings": latest.get("request_warnings", []),
            "rows": snapshot_rows,
        }
    )
    max_records = max(1, max_records)
    history = history[-max_records:]
    payload = json.dumps(history, ensure_ascii=False, separators=(",", ":"))
    if max_bytes > 0:
        while history and len(payload.encode("utf-8")) > max_bytes:
            drop_count = max(1, min(len(history) - 1, max(len(history) // 10, 1)))
            history = history[drop_count:]
            payload = json.dumps(history, ensure_ascii=False, separators=(",", ":"))
    HISTORY_FILE.write_text(payload, encoding="utf-8")
    return len(history)


def load_history() -> list[dict[str, Any]]:
    if not HISTORY_FILE.exists():
        return []
    try:
        data = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []
    return data if isinstance(data, list) else []


def floor_time(now: datetime, minutes: int) -> datetime:
    minutes = max(1, minutes)
    floored = now.replace(second=0, microsecond=0)
    delta_minutes = floored.minute - (floored.minute % minutes)
    return floored.replace(minute=delta_minutes).astimezone(timezone.utc)


def top_rows(
    rows: list[dict[str, Any]],
    field: str,
    limit: int,
    abs_value: bool,
) -> list[dict[str, Any]]:
    def key(row: dict[str, Any]) -> float:
        value = to_float(row.get(field))
        return abs(value) if abs_value else value

    ranked = sorted(rows, key=key, reverse=True)[:limit]
    return [
        {
            "outcome_id": row.get("outcome_id"),
            "outcome_name": row.get("outcome_name"),
            "side_name": row.get("side_name"),
            "symbol": row.get("symbol"),
            "underlying": row.get("underlying"),
            "implied_probability": row.get("implied_probability"),
            "mark_price": row.get("mark_price"),
            "mid_price": row.get("mid_price"),
            "price_source": row.get("price_source"),
            "volume_24h": row.get("volume_24h"),
            "open_interest": row.get("open_interest"),
        }
        for row in ranked
    ]


def render_report(latest: dict[str, Any], top_limit: int) -> str:
    by_underlying = latest.get("by_underlying", {})
    by_class = latest.get("by_class", {})
    underlying_lines = render_counts(by_underlying)
    class_lines = render_counts(by_class)
    error_lines = "\n".join(f"- `{err}`" for err in latest.get("request_errors", []))
    warning_lines = "\n".join(f"- `{err}`" for err in latest.get("request_warnings", []))

    rows = latest.get("rows", [])
    top_probability = top_rows(rows, "implied_probability", top_limit, abs_value=False)
    top_volume = top_rows(rows, "volume_24h", top_limit, abs_value=False)
    top_oi = top_rows(rows, "open_interest", top_limit, abs_value=False)

    return (
        "# Latest HIP-4 Outcome Markets\n\n"
        f"- Generated: `{latest.get('generated_at')}`\n"
        f"- Info endpoint: `{latest.get('info_url')}`\n"
        f"- Outcome markets: `{latest.get('outcome_count')}`\n"
        f"- Outcome sides (rows): `{latest.get('side_count')}`\n\n"
        "## Markets by Underlying\n\n"
        f"{underlying_lines}\n\n"
        "## Markets by Class\n\n"
        f"{class_lines}\n\n"
        "## Current Implied Probabilities\n\n"
        f"{render_market_rows(top_probability) or '- No probability data available.'}\n\n"
        "## Top by 24h Volume\n\n"
        f"{render_market_rows(top_volume) or '- No volume data available.'}\n\n"
        "## Top by Open Interest\n\n"
        f"{render_market_rows(top_oi) or '- No open-interest data available.'}\n\n"
        "## Request Errors\n\n"
        f"{error_lines or '- None.'}\n\n"
        "## Request Warnings\n\n"
        f"{warning_lines or '- None.'}\n\n"
        "Public output stores aggregate HIP-4 outcome data only. It is not a trade signal.\n"
    )


def render_counts(counts: dict[str, Any]) -> str:
    if not isinstance(counts, dict) or not counts:
        return "- No data."
    return "\n".join(
        f"- {key}: `{value}`" for key, value in sorted(counts.items())
    )


def render_market_rows(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return ""
    lines = []
    for row in rows:
        prob = row.get("implied_probability")
        prob_text = f"{round(prob, 4)}" if isinstance(prob, (int, float)) else "n/a"
        lines.append(
            f"- {row.get('outcome_name') or row.get('outcome_id')} [{row.get('side_name')}] "
            f"symbol `{row.get('symbol') or 'n/a'}` "
            f"underlying `{row.get('underlying') or 'n/a'}` "
            f"prob `{prob_text}` "
            f"price_source `{row.get('price_source') or 'n/a'}` "
            f"vol24h `{row.get('volume_24h')}` oi `{row.get('open_interest')}`"
        )
    return "\n".join(lines)


def to_float(value: Any) -> float:
    try:
        return float(value) if value is not None else 0.0
    except (TypeError, ValueError):
        return 0.0


def to_float_or_none(value: Any) -> float | None:
    try:
        return float(value) if value is not None else None
    except (TypeError, ValueError):
        return None


def first_float(*values: Any) -> float | None:
    for value in values:
        parsed = to_float_or_none(value)
        if parsed is not None:
            return parsed
    return None


def to_int(value: Any) -> int | None:
    try:
        return int(value) if value is not None and value != "" else None
    except (TypeError, ValueError):
        return None
