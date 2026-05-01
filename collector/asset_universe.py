from __future__ import annotations

import gzip
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
ARCHIVE_DIR = ROOT / "data" / "archive"
LATEST_FILE = PROCESSED_DIR / "asset_universe_latest.json"
HISTORY_FILE = PROCESSED_DIR / "asset_price_history.json"
REPORT_FILE = REPORT_DIR / "latest_asset_universe.md"
HYPERLIQUID_INFO_URL = "https://api.hyperliquid.xyz/info"
DEFAULT_HIP3_DEXS = "xyz"

ASSET_CLASS_ORDER = [
    "equity",
    "index",
    "metal",
    "commodity",
    "fx",
    "crypto_major",
    "crypto_alt",
    "unknown",
]

ASSET_CLASS_LABELS = {
    "equity": "Equity Perps",
    "index": "Index Perps",
    "metal": "Metal Perps",
    "commodity": "Commodity Perps",
    "fx": "FX Perps",
    "crypto_major": "Crypto Majors",
    "crypto_alt": "Crypto Alts",
    "unknown": "Unknown / Unclassified",
}

CRYPTO_MAJOR_SYMBOLS = {
    "BTC",
    "ETH",
    "SOL",
    "HYPE",
    "BNB",
    "XRP",
    "DOGE",
}

METAL_SYMBOLS = {
    "ALUMINIUM",
    "COPPER",
    "GOLD",
    "PALLADIUM",
    "PAXG",
    "PLATINUM",
    "SILVER",
}

SUPPLEMENTAL_CLASS_BY_SYMBOL = {
    "BIRD": "equity",
    "BX": "equity",
    "CBRS": "equity",
    "DKNG": "equity",
    "HIMS": "equity",
    "LITE": "equity",
    "MRVL": "equity",
    "RKLB": "equity",
    "CORN": "commodity",
    "TTF": "commodity",
    "URANIUM": "commodity",
    "WHEAT": "commodity",
    "DRAM": "index",
    "EWZ": "index",
    "VOL": "index",
    "XLE": "index",
    "KRW": "fx",
}

logger = logging.getLogger(__name__)


def update_asset_universe_snapshot(now: datetime) -> dict[str, Any]:
    if os.getenv("ASSET_UNIVERSE_ENABLED", "true").lower() == "false":
        return {"enabled": False, "reason": "ASSET_UNIVERSE_ENABLED=false"}

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    bucket_minutes = int(os.getenv("ASSET_UNIVERSE_BUCKET_MINUTES", "15"))
    max_records = int(os.getenv("ASSET_UNIVERSE_MAX_RECORDS", "2880"))
    top_limit = int(os.getenv("ASSET_UNIVERSE_TOP_LIMIT", "25"))
    class_top_limit = int(os.getenv("ASSET_UNIVERSE_CLASS_TOP_LIMIT", "10"))
    hip3_dexes = parse_csv(os.getenv("ASSET_UNIVERSE_HIP3_DEXS", DEFAULT_HIP3_DEXS))
    bucket = floor_time(now, bucket_minutes)

    rows, collection_meta = collect_asset_rows(hip3_dexes)
    latest = build_latest_snapshot(now, bucket, rows, top_limit, class_top_limit, collection_meta)
    history = update_price_history(now, bucket, rows, max_records)
    summary = {
        "enabled": True,
        "updated_at": now.isoformat(),
        "observed_at": bucket.isoformat(),
        "asset_count": latest["asset_count"],
        "priced_asset_count": latest["priced_asset_count"],
        "history_records": history["record_count"],
        "history_active_records": history["record_count"],
        "history_archived_records_added": history.get("archived_records_added", 0),
        "history_archive_files": history.get("archive_files", []),
        "latest_file": "data/processed/asset_universe_latest.json",
        "history_file": "data/processed/asset_price_history.json",
        "report_file": "data/reports/latest_asset_universe.md",
        "hip3_dexes": latest["hip3_dexes"],
        "asset_class_counts": latest["asset_class_counts"],
        "top_by_volume": latest["top_by_volume"][:5],
        "top_gainers_24h": latest["top_gainers_24h"][:5],
        "top_losers_24h": latest["top_losers_24h"][:5],
        "top_by_asset_class": latest["top_by_asset_class"],
    }

    LATEST_FILE.write_text(json.dumps(latest, indent=2, ensure_ascii=False), encoding="utf-8")
    HISTORY_FILE.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")
    REPORT_FILE.write_text(render_report(summary), encoding="utf-8")
    logger.info("Wrote %s", LATEST_FILE)
    return summary


def collect_asset_rows(hip3_dexes: list[str]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    annotations = fetch_perp_annotations() if hip3_dexes else {}
    perp_dexes = fetch_perp_dexs() if hip3_dexes else []
    dex_by_name = {
        item["name"]: item
        for item in perp_dexes
        if item.get("name")
    }
    requested_dexes = resolve_requested_dexes(hip3_dexes, dex_by_name)
    collection_meta = {
        "requested_hip3_dexes": hip3_dexes,
        "available_hip3_dexes": [
            {
                "name": item.get("name"),
                "full_name": item.get("fullName"),
                "dex_index": item.get("dex_index"),
                "asset_cap_count": len(item.get("assetToStreamingOiCap", [])),
            }
            for item in perp_dexes
        ],
        "hip3_dexes": [],
    }

    meta, asset_ctxs = fetch_meta_and_contexts()
    mids = fetch_all_mids()
    universe = meta.get("universe", []) if isinstance(meta, dict) else []
    rows: dict[str, dict[str, Any]] = {}

    for idx, asset in enumerate(universe):
        if not isinstance(asset, dict):
            continue
        symbol = str(asset.get("name") or "").strip()
        if not symbol:
            continue
        ctx = asset_ctxs[idx] if idx < len(asset_ctxs) and isinstance(asset_ctxs[idx], dict) else {}
        row = build_row(
            symbol,
            asset,
            ctx,
            mids.get(symbol),
            dex="",
            dex_index=0,
            index_in_meta=idx,
            market_type="native_perp",
        )
        rows[symbol] = row

    for symbol, mid in mids.items():
        if symbol not in rows:
            rows[symbol] = build_row(
                symbol,
                {},
                {},
                mid,
                source="allMids_only",
                market_type="spot_or_aux",
            )

    for dex in requested_dexes:
        try:
            dex_rows, dex_summary = collect_hip3_dex_rows(dex, dex_by_name.get(dex), annotations)
        except Exception as e:
            logger.warning("HIP-3 dex %s update failed: %s", dex, e)
            collection_meta["hip3_dexes"].append({"name": dex, "enabled": False, "error": str(e)})
            continue
        collection_meta["hip3_dexes"].append(dex_summary)
        for row in dex_rows:
            rows[row["symbol"]] = row

    return sorted(rows.values(), key=lambda row: row["symbol"]), collection_meta


def collect_hip3_dex_rows(
    dex: str,
    dex_info: dict[str, Any] | None,
    annotations: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    meta, asset_ctxs = fetch_meta_and_contexts(dex=dex)
    universe = meta.get("universe", []) if isinstance(meta, dict) else []
    dex_info = dex_info or {"name": dex}
    dex_index = int(dex_info.get("dex_index") or 0)
    cap_map = tuple_map_to_dict(dex_info.get("assetToStreamingOiCap"))
    funding_multiplier_map = tuple_map_to_dict(dex_info.get("assetToFundingMultiplier"))
    rows = []

    for idx, asset in enumerate(universe):
        if not isinstance(asset, dict):
            continue
        symbol = str(asset.get("name") or "").strip()
        if not symbol:
            continue
        ctx = asset_ctxs[idx] if idx < len(asset_ctxs) and isinstance(asset_ctxs[idx], dict) else {}
        rows.append(
            build_row(
                symbol,
                asset,
                ctx,
                dex=dex,
                dex_index=dex_index,
                dex_full_name=dex_info.get("fullName"),
                index_in_meta=idx,
                market_type="hip3_perp",
                source=f"metaAndAssetCtxs:{dex}",
                annotation=annotations.get(symbol, {}),
                streaming_oi_cap=cap_map.get(symbol),
                funding_multiplier=funding_multiplier_map.get(symbol),
            )
        )

    priced_count = len([row for row in rows if row.get("price") is not None])
    return rows, {
        "name": dex,
        "full_name": dex_info.get("fullName"),
        "dex_index": dex_index,
        "enabled": True,
        "asset_count": len(rows),
        "priced_asset_count": priced_count,
    }


def fetch_meta_and_contexts(dex: str | None = None) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    payload: dict[str, Any] = {"type": "metaAndAssetCtxs"}
    if dex:
        payload["dex"] = dex
    data = post_info(payload, timeout=20)
    if not isinstance(data, list) or len(data) < 2:
        return {}, []
    meta = data[0] if isinstance(data[0], dict) else {}
    contexts = data[1] if isinstance(data[1], list) else []
    return meta, contexts


def fetch_all_mids() -> dict[str, str]:
    data = post_info({"type": "allMids"}, timeout=15)
    return data if isinstance(data, dict) else {}


def fetch_perp_dexs() -> list[dict[str, Any]]:
    try:
        data = post_info({"type": "perpDexs"}, timeout=20)
    except Exception as e:
        logger.warning("perpDexs failed: %s", e)
        return []
    if not isinstance(data, list):
        return []
    items = []
    for dex_index, item in enumerate(data):
        if isinstance(item, dict):
            enriched = dict(item)
            enriched["dex_index"] = dex_index
            items.append(enriched)
    return items


def fetch_perp_annotations() -> dict[str, dict[str, Any]]:
    try:
        data = post_info({"type": "perpConciseAnnotations"}, timeout=20)
    except Exception as e:
        logger.warning("perpConciseAnnotations failed: %s", e)
        return {}
    if not isinstance(data, list):
        return {}
    annotations: dict[str, dict[str, Any]] = {}
    for item in data:
        if (
            isinstance(item, list)
            and len(item) == 2
            and isinstance(item[0], str)
            and isinstance(item[1], dict)
        ):
            annotations[item[0]] = item[1]
    return annotations


def post_info(payload: dict[str, Any], timeout: int) -> Any:
    response = requests.post(
        HYPERLIQUID_INFO_URL,
        json=payload,
        headers={"Content-Type": "application/json"},
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


def build_row(
    symbol: str,
    asset: dict[str, Any],
    ctx: dict[str, Any],
    mid_override: Any = None,
    source: str = "metaAndAssetCtxs",
    market_type: str = "native_perp",
    dex: str = "",
    dex_index: int | None = None,
    dex_full_name: str | None = None,
    index_in_meta: int | None = None,
    annotation: dict[str, Any] | None = None,
    streaming_oi_cap: Any = None,
    funding_multiplier: Any = None,
) -> dict[str, Any]:
    annotation = annotation or {}
    asset_class, classification_source = classify_asset(symbol, market_type, annotation)
    base_symbol = base_symbol_from(symbol)
    mid_px = to_float(mid_override) or to_float(ctx.get("midPx"))
    mark_px = to_float(ctx.get("markPx"))
    oracle_px = to_float(ctx.get("oraclePx"))
    price = first_positive(mid_px, mark_px, oracle_px)
    prev_day = to_float(ctx.get("prevDayPx"))
    return {
        "symbol": symbol,
        "display_name": annotation.get("displayName") or base_symbol,
        "base_symbol": base_symbol,
        "asset_class": asset_class,
        "classification_source": classification_source,
        "annotation_category": annotation.get("category"),
        "annotation_keywords": annotation.get("keywords") if isinstance(annotation.get("keywords"), list) else [],
        "market_type": market_type,
        "dex": dex,
        "dex_full_name": dex_full_name,
        "dex_index": dex_index,
        "index_in_meta": index_in_meta,
        "asset_id": compute_asset_id(market_type, dex_index, index_in_meta),
        "source": source,
        "price": round(price, 8) if price else None,
        "mid_px": round(mid_px, 8) if mid_px else None,
        "mark_px": round(mark_px, 8) if mark_px else None,
        "oracle_px": round(oracle_px, 8) if oracle_px else None,
        "prev_day_px": round(prev_day, 8) if prev_day else None,
        "change_24h_pct": pct_change(price, prev_day) if price and prev_day else None,
        "day_ntl_vlm": round(to_float(ctx.get("dayNtlVlm")), 2),
        "day_base_vlm": round(to_float(ctx.get("dayBaseVlm")), 8),
        "open_interest": round(to_float(ctx.get("openInterest")), 8),
        "funding": round(to_float(ctx.get("funding")), 10) if ctx.get("funding") is not None else None,
        "premium": round(to_float(ctx.get("premium")), 10) if ctx.get("premium") is not None else None,
        "max_leverage": asset.get("maxLeverage"),
        "sz_decimals": asset.get("szDecimals"),
        "margin_table_id": asset.get("marginTableId"),
        "margin_mode": asset.get("marginMode"),
        "only_isolated": asset.get("onlyIsolated"),
        "growth_mode": asset.get("growthMode"),
        "streaming_oi_cap": round(to_float(streaming_oi_cap), 2) if streaming_oi_cap is not None else None,
        "funding_multiplier": to_float(funding_multiplier) if funding_multiplier is not None else None,
    }


def build_latest_snapshot(
    now: datetime,
    bucket: datetime,
    rows: list[dict[str, Any]],
    top_limit: int,
    class_top_limit: int,
    collection_meta: dict[str, Any],
) -> dict[str, Any]:
    priced = [row for row in rows if row.get("price")]
    volume_rows = sorted(
        priced,
        key=lambda row: to_float(row.get("day_ntl_vlm")),
        reverse=True,
    )
    gainers = sorted(
        [row for row in priced if row.get("change_24h_pct") is not None],
        key=lambda row: to_float(row.get("change_24h_pct")),
        reverse=True,
    )
    return {
        "schema_version": 1,
        "updated_at": now.isoformat(),
        "observed_at": bucket.isoformat(),
        "asset_count": len(rows),
        "priced_asset_count": len(priced),
        "hip3_dexes": collection_meta.get("hip3_dexes", []),
        "available_hip3_dexes": collection_meta.get("available_hip3_dexes", []),
        "asset_class_counts": count_asset_classes(rows),
        "top_by_volume": compact_rows(volume_rows[:top_limit]),
        "top_gainers_24h": compact_rows(gainers[:top_limit]),
        "top_losers_24h": compact_rows(list(reversed(gainers[-top_limit:]))),
        "top_by_asset_class": build_class_summaries(priced, class_top_limit),
        "assets": rows,
    }


def update_price_history(
    now: datetime,
    bucket: datetime,
    rows: list[dict[str, Any]],
    max_records: int,
) -> dict[str, Any]:
    active_records = int(os.getenv("ASSET_UNIVERSE_ACTIVE_RECORDS", "672"))
    archive_enabled = os.getenv("ASSET_UNIVERSE_ARCHIVE_ENABLED", "true").lower() != "false"
    history = load_json(HISTORY_FILE, default={})
    records = history.get("records", []) if isinstance(history, dict) else []
    if not isinstance(records, list):
        records = []

    prices = {
        row["symbol"]: row["price"]
        for row in rows
        if row.get("price") is not None
    }
    record = {
        "observed_at": bucket.isoformat(),
        "collected_at": now.isoformat(),
        "asset_count": len(rows),
        "priced_asset_count": len(prices),
        "asset_class_counts": count_asset_classes(rows),
        "prices": prices,
    }
    records = [item for item in records if item.get("observed_at") != record["observed_at"]]
    records.append(record)
    records.sort(key=lambda item: item.get("observed_at", ""))
    if max_records > 0:
        records = records[-max_records:]

    archive_files: list[str] = []
    archived_count = 0
    if archive_enabled and active_records > 0 and len(records) > active_records:
        archive_records = records[:-active_records]
        archive_files = archive_price_records(archive_records)
        archived_count = len(archive_records)
        records = records[-active_records:]
    elif active_records > 0:
        records = records[-active_records:]

    return {
        "schema_version": 1,
        "updated_at": now.isoformat(),
        "max_records": max_records,
        "active_records": active_records,
        "archive_enabled": archive_enabled,
        "archive_files": archive_files,
        "archived_records_added": archived_count,
        "record_count": len(records),
        "records": records,
    }


def archive_price_records(records: list[dict[str, Any]]) -> list[str]:
    by_month: dict[str, list[dict[str, Any]]] = {}
    for record in records:
        observed_at = parse_time(record.get("observed_at"))
        if observed_at is None:
            continue
        by_month.setdefault(observed_at.strftime("%Y-%m"), []).append(record)

    written = []
    for month, month_records in sorted(by_month.items()):
        path = ARCHIVE_DIR / f"asset_price_history_{month}.jsonl.gz"
        merged: dict[str, dict[str, Any]] = {}
        if path.exists():
            try:
                with gzip.open(path, "rt", encoding="utf-8") as fh:
                    for line in fh:
                        try:
                            item = json.loads(line)
                        except Exception:
                            continue
                        if isinstance(item, dict) and item.get("observed_at"):
                            merged[str(item["observed_at"])] = item
            except Exception:
                logger.warning("Could not read archive %s; rewriting from current records", path)
        for record in month_records:
            if record.get("observed_at"):
                merged[str(record["observed_at"])] = record
        ordered = [merged[key] for key in sorted(merged)]
        with gzip.open(path, "wt", encoding="utf-8") as fh:
            for item in ordered:
                fh.write(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n")
        written.append(f"data/archive/{path.name}")
    return written


def compact_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "symbol": row.get("symbol"),
            "display_name": row.get("display_name"),
            "asset_class": row.get("asset_class"),
            "market_type": row.get("market_type"),
            "dex": row.get("dex"),
            "price": row.get("price"),
            "change_24h_pct": row.get("change_24h_pct"),
            "day_ntl_vlm": row.get("day_ntl_vlm"),
            "open_interest": row.get("open_interest"),
            "funding": row.get("funding"),
        }
        for row in rows
    ]


def render_report(summary: dict[str, Any]) -> str:
    top_volume = render_rows(summary.get("top_by_volume", []), "day_ntl_vlm")
    gainers = render_rows(summary.get("top_gainers_24h", []), "change_24h_pct")
    losers = render_rows(summary.get("top_losers_24h", []), "change_24h_pct")
    class_counts = render_class_counts(summary.get("asset_class_counts", {}))
    hip3_dexes = render_hip3_dexes(summary.get("hip3_dexes", []))
    class_sections = render_class_sections(summary.get("top_by_asset_class", {}))
    archive_files = summary.get("history_archive_files", [])
    archive_line = ", ".join(f"`{path}`" for path in archive_files) if archive_files else "`none yet`"
    return (
        "# Latest Asset Universe\n\n"
        f"- Updated: `{summary.get('updated_at')}`\n"
        f"- Observed: `{summary.get('observed_at')}`\n"
        f"- Assets: `{summary.get('asset_count')}`\n"
        f"- Priced assets: `{summary.get('priced_asset_count')}`\n"
        f"- Active history records: `{summary.get('history_active_records')}`\n"
        f"- Archived records added this run: `{summary.get('history_archived_records_added')}`\n"
        f"- Archive files touched: {archive_line}\n"
        f"- Latest file: `{summary.get('latest_file')}`\n"
        f"- History file: `{summary.get('history_file')}`\n\n"
        "## HIP-3 Dexes\n\n"
        f"{hip3_dexes}\n\n"
        "## Asset Classes\n\n"
        f"{class_counts}\n\n"
        "## Top By Volume\n\n"
        f"{top_volume}\n\n"
        "## Top 24h Gainers\n\n"
        f"{gainers}\n\n"
        "## Top 24h Losers\n\n"
        f"{losers}\n\n"
        "## Top By Asset Class\n\n"
        f"{class_sections}\n"
    )


def render_rows(rows: list[dict[str, Any]], metric: str) -> str:
    if not rows:
        return "- No rows."
    return "\n".join(
        f"- {row.get('symbol')}: price `{row.get('price')}`, "
        f"{metric} `{row.get(metric)}`"
        for row in rows
    )


def render_class_counts(counts: dict[str, int]) -> str:
    if not counts:
        return "- No class counts."
    parts = []
    for asset_class in ASSET_CLASS_ORDER:
        if asset_class in counts:
            parts.append(f"- {asset_class}: `{counts[asset_class]}`")
    for asset_class, count in sorted(counts.items()):
        if asset_class not in ASSET_CLASS_ORDER:
            parts.append(f"- {asset_class}: `{count}`")
    return "\n".join(parts)


def render_hip3_dexes(dexes: list[dict[str, Any]]) -> str:
    enabled = [dex for dex in dexes if dex.get("enabled")]
    if not enabled:
        return "- No HIP-3 dexes collected."
    return "\n".join(
        f"- {dex.get('name')}: `{dex.get('asset_count')}` assets, "
        f"`{dex.get('priced_asset_count')}` priced"
        for dex in enabled
    )


def render_class_sections(top_by_class: dict[str, Any]) -> str:
    if not top_by_class:
        return "- No class summaries."
    sections = []
    for asset_class in ASSET_CLASS_ORDER:
        summary = top_by_class.get(asset_class)
        if not summary:
            continue
        label = ASSET_CLASS_LABELS.get(asset_class, asset_class)
        rows = render_rows(summary.get("top_by_volume", []), "day_ntl_vlm")
        sections.append(f"### {label}\n\n{rows}")
    return "\n\n".join(sections) if sections else "- No class summaries."


def build_class_summaries(rows: list[dict[str, Any]], top_limit: int) -> dict[str, Any]:
    summaries: dict[str, Any] = {}
    for asset_class in sorted({str(row.get("asset_class") or "unknown") for row in rows}):
        class_rows = [row for row in rows if row.get("asset_class") == asset_class]
        by_volume = sorted(
            class_rows,
            key=lambda row: to_float(row.get("day_ntl_vlm")),
            reverse=True,
        )
        gainers = sorted(
            [row for row in class_rows if row.get("change_24h_pct") is not None],
            key=lambda row: to_float(row.get("change_24h_pct")),
            reverse=True,
        )
        summaries[asset_class] = {
            "count": len(class_rows),
            "top_by_volume": compact_rows(by_volume[:top_limit]),
            "top_gainers_24h": compact_rows(gainers[:top_limit]),
            "top_losers_24h": compact_rows(list(reversed(gainers[-top_limit:]))),
        }
    return summaries


def count_asset_classes(rows: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        asset_class = str(row.get("asset_class") or "unknown")
        counts[asset_class] = counts.get(asset_class, 0) + 1
    return dict(sorted(counts.items()))


def classify_asset(
    symbol: str,
    market_type: str,
    annotation: dict[str, Any],
) -> tuple[str, str]:
    base_symbol = base_symbol_from(symbol)
    category = str(annotation.get("category") or "").lower()
    keywords = [str(item).lower() for item in annotation.get("keywords", []) if item is not None]

    if category == "stocks":
        return "equity", "perpConciseAnnotations"
    if category == "indices":
        return "index", "perpConciseAnnotations"
    if category == "fx":
        return "fx", "perpConciseAnnotations"
    if category == "preipo":
        return "equity", "perpConciseAnnotations"
    if category == "commodities":
        if base_symbol in METAL_SYMBOLS or "metal" in keywords:
            return "metal", "perpConciseAnnotations"
        return "commodity", "perpConciseAnnotations"
    if category == "crypto":
        return classify_crypto_symbol(base_symbol), "perpConciseAnnotations"

    if base_symbol in METAL_SYMBOLS:
        return "metal", "symbol_rule"
    if base_symbol in SUPPLEMENTAL_CLASS_BY_SYMBOL:
        return SUPPLEMENTAL_CLASS_BY_SYMBOL[base_symbol], "symbol_rule"
    if market_type == "native_perp" and base_symbol:
        return classify_crypto_symbol(base_symbol), "symbol_rule"
    if market_type == "spot_or_aux" and "/" in symbol:
        return "crypto_alt", "symbol_rule"
    return "unknown", "unclassified"


def classify_crypto_symbol(symbol: str) -> str:
    return "crypto_major" if symbol in CRYPTO_MAJOR_SYMBOLS else "crypto_alt"


def compute_asset_id(
    market_type: str,
    dex_index: int | None,
    index_in_meta: int | None,
) -> int | None:
    if index_in_meta is None:
        return None
    if market_type == "native_perp":
        return index_in_meta
    if market_type == "hip3_perp" and dex_index is not None:
        return 100000 + dex_index * 10000 + index_in_meta
    return None


def base_symbol_from(symbol: str) -> str:
    if ":" in symbol:
        return symbol.split(":", 1)[1]
    if "/" in symbol:
        return symbol.split("/", 1)[0]
    return symbol


def tuple_map_to_dict(value: Any) -> dict[str, Any]:
    if not isinstance(value, list):
        return {}
    result = {}
    for item in value:
        if isinstance(item, list) and len(item) == 2 and isinstance(item[0], str):
            result[item[0]] = item[1]
    return result


def resolve_requested_dexes(
    requested: list[str],
    dex_by_name: dict[str, dict[str, Any]],
) -> list[str]:
    if not requested:
        return []
    lowered = {item.lower() for item in requested}
    if "*" in lowered or "all" in lowered:
        return sorted(dex_by_name)
    return requested


def parse_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def floor_time(dt: datetime, bucket_minutes: int) -> datetime:
    bucket = max(1, bucket_minutes)
    minute = (dt.minute // bucket) * bucket
    return dt.astimezone(timezone.utc).replace(minute=minute, second=0, microsecond=0)


def parse_time(value: Any) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
        return parsed.astimezone(timezone.utc) if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def first_positive(*values: float) -> float:
    for value in values:
        if value > 0:
            return value
    return 0.0


def pct_change(new: float, old: float) -> float | None:
    if old == 0:
        return None
    return round((new / old - 1) * 100, 4)


def to_float(value: Any) -> float:
    try:
        return float(value) if value is not None else 0.0
    except (TypeError, ValueError):
        return 0.0
