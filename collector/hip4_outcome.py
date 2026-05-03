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

logger = logging.getLogger(__name__)


def update_hip4_outcome_snapshot(now: datetime) -> dict[str, Any]:
    if os.getenv("HIP4_OUTCOME_ENABLED", "true").lower() == "false":
        return {"enabled": False, "reason": "HIP4_OUTCOME_ENABLED=false"}

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    info_url = os.getenv("HIP4_INFO_URL", DEFAULT_INFO_URL).strip() or DEFAULT_INFO_URL
    timeout = int(os.getenv("HIP4_REQUEST_TIMEOUT", str(DEFAULT_TIMEOUT)))
    top_limit = int(os.getenv("HIP4_TOP_LIMIT", "25"))
    history_max = int(os.getenv("HIP4_HISTORY_MAX_RECORDS", "2880"))

    meta_payload, meta_error = post_info(info_url, {"type": "outcomeMeta"}, timeout)

    # Try outcomeMetaAndAssetCtxs first; fall back to outcomeAssetCtxs if 422
    ctx_payload, ctx_error = post_info(
        info_url, {"type": "outcomeMetaAndAssetCtxs"}, timeout
    )
    if ctx_error and "422" in str(ctx_error):
        ctx_payload, ctx_error = post_info(
            info_url, {"type": "outcomeAssetCtxs"}, timeout
        )

    save_raw_payload(now, "outcome_meta", meta_payload, meta_error)
    save_raw_payload(now, "outcome_meta_and_ctxs", ctx_payload, ctx_error)

    outcomes = extract_outcomes(meta_payload, ctx_payload)
    asset_ctxs = extract_asset_ctxs(ctx_payload)
    rows = build_rows(outcomes, asset_ctxs)
    aggregates = aggregate_rows(rows)

    latest = {
        "generated_at": now.isoformat(),
        "info_url": info_url,
        "request_errors": [err for err in (meta_error, ctx_error) if err],
        "outcome_count": aggregates["outcome_count"],
        "side_count": len(rows),
        "by_underlying": aggregates["by_underlying"],
        "by_class": aggregates["by_class"],
        "by_status": aggregates["by_status"],
        "rows": rows,
    }

    LATEST_FILE.write_text(json.dumps(latest, indent=2, ensure_ascii=False), encoding="utf-8")
    history_records = append_history(now, latest, history_max)
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
        "latest_file": "data/processed/hip4_outcome_latest.json",
        "history_file": "data/processed/hip4_outcome_history.json",
        "report_file": "data/reports/latest_hip4_outcome.md",
        "by_underlying": latest["by_underlying"],
        "by_class": latest["by_class"],
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
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    asset_index = 0

    for outcome in outcomes:
        outcome_id = outcome.get("outcome")
        if outcome_id is None:
            outcome_id = outcome.get("outcomeId") or outcome.get("id")
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

            mark = to_float(ctx.get("markPx") or ctx.get("mark") or ctx.get("mid"))
            mid = to_float(ctx.get("midPx") or ctx.get("mid"))
            best_bid = to_float(ctx.get("bestBidPx") or ctx.get("bidPx"))
            best_ask = to_float(ctx.get("bestAskPx") or ctx.get("askPx"))
            implied_probability = mark if 0 < mark < 1 else (mid if 0 < mid < 1 else None)

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
                    "asset_id": side.get("assetId") or ctx.get("assetId"),
                    "token_index": side.get("tokenIndex") or side.get("index"),
                    "mark_price": mark or None,
                    "mid_price": mid or None,
                    "best_bid": best_bid or None,
                    "best_ask": best_ask or None,
                    "implied_probability": implied_probability,
                    "volume_24h": to_float(ctx.get("dayNtlVlm") or ctx.get("dayVlm") or ctx.get("volume24h")),
                    "open_interest": to_float(ctx.get("openInterest") or ctx.get("oi")),
                    "raw_side_spec": side,
                    "raw_ctx": ctx,
                }
            )
    return rows


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


def append_history(now: datetime, latest: dict[str, Any], max_records: int) -> int:
    history = load_history()
    bucket_minutes = int(os.getenv("HIP4_BUCKET_MINUTES", "15"))
    bucket = floor_time(now, bucket_minutes).isoformat()

    snapshot_rows = [
        {
            "outcome_id": row.get("outcome_id"),
            "outcome_name": row.get("outcome_name"),
            "side_index": row.get("side_index"),
            "side_name": row.get("side_name"),
            "underlying": row.get("underlying"),
            "outcome_class": row.get("outcome_class"),
            "implied_probability": row.get("implied_probability"),
            "mark_price": row.get("mark_price"),
            "mid_price": row.get("mid_price"),
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
            "rows": snapshot_rows,
        }
    )
    history = history[-max_records:]
    HISTORY_FILE.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")
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
            "underlying": row.get("underlying"),
            "implied_probability": row.get("implied_probability"),
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

    rows = latest.get("rows", [])
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
        "## Top by 24h Volume\n\n"
        f"{render_market_rows(top_volume) or '- No volume data available.'}\n\n"
        "## Top by Open Interest\n\n"
        f"{render_market_rows(top_oi) or '- No open-interest data available.'}\n\n"
        "## Request Errors\n\n"
        f"{error_lines or '- None.'}\n\n"
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
            f"underlying `{row.get('underlying') or 'n/a'}` "
            f"prob `{prob_text}` "
            f"vol24h `{row.get('volume_24h')}` oi `{row.get('open_interest')}`"
        )
    return "\n".join(lines)


def to_float(value: Any) -> float:
    try:
        return float(value) if value is not None else 0.0
    except (TypeError, ValueError):
        return 0.0
