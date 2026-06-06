from __future__ import annotations

import json
import logging
import os
import re
import gzip
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import feedparser
import requests
from dateutil import parser as date_parser

from collector.asset_universe import update_asset_universe_snapshot
from collector.asset_features import update_asset_features
from collector.ai_index import update_ai_index
from collector.day_swing import update_day_swing_dataset
from collector.hip4_outcome import update_hip4_outcome_snapshot
from collector.macro_indicators import update_macro_indicators
from collector.relationship_scan import update_relationship_scan
from collector.sector_reactions import update_sector_reactions

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
RAW_DIR = ROOT / "data" / "raw"
REPORT_DIR = ROOT / "data" / "reports"
ARCHIVE_DIR = ROOT / "data" / "archive"
CONTEXT_FILE = PROCESSED_DIR / "market_context.json"
HISTORY_FILE = PROCESSED_DIR / "market_context_history.json"
REPORT_FILE = REPORT_DIR / "latest_context.md"
FLOW_ALERT_FILE = PROCESSED_DIR / "flow_alert.json"
FLOW_ALERT_HISTORY_FILE = PROCESSED_DIR / "flow_alert_history.json"
FLOW_ALERT_REPORT_FILE = REPORT_DIR / "latest_flow_alert.md"
POLYMARKET_OUTCOME_HISTORY_FILE = PROCESSED_DIR / "polymarket_outcome_history.json"
POLYMARKET_OUTCOME_LATEST_FILE = PROCESSED_DIR / "polymarket_outcome_latest.json"
DEFAULT_RSS_FEEDS = (
    "https://cointelegraph.com/rss,"
    "https://www.coindesk.com/arc/outboundfeeds/rss/"
)
DEFAULT_MACRO_RSS_FEEDS = (
    "https://feeds.bbci.co.uk/news/business/rss.xml,"
    "https://feeds.bbci.co.uk/news/world/rss.xml,"
    "https://www.cnbc.com/id/20910258/device/rss/rss.html,"
    "https://www.cnbc.com/id/20409666/device/rss/rss.html,"
    "https://finance.yahoo.com/news/rssindex"
)
DEFAULT_POLICY_RSS_FEEDS = (
    "https://www.federalreserve.gov/feeds/press_all.xml,"
    "https://www.federalreserve.gov/feeds/speeches.xml"
)
DEFAULT_COMMODITY_RSS_FEEDS = "https://www.cnbc.com/id/19836768/device/rss/rss.html"
DEFAULT_GDELT_QUERIES = (
    "bitcoin OR ethereum OR crypto OR stablecoin,"
    "federal reserve OR inflation OR treasury yields OR oil OR gold OR stocks"
)
DEFAULT_POLYMARKET_EVENT_SLUGS = ""
CRYPTO_MARKET_WORDS = {
    "btc", "bitcoin", "eth", "ethereum", "crypto", "stablecoin", "usdt",
    "usdc", "solana", "sol", "xrp", "doge", "hyperliquid", "binance", "megaeth",
}
PUBLIC_HEALTH_MARKET_WORDS = {
    "pandemic", "covid", "covid-19", "coronavirus", "virus", "disease",
    "outbreak", "bird flu", "avian flu", "h5n1", "h5n5", "hantavirus",
    "public health", "world health organization", "who declare", "who declares",
    "who emergency", "who pandemic", "who outbreak", "vaccine", "mpox", "ebola",
}
FLOW_ALERT_PROFILES = {"flow_alert", "flow-alert", "alert", "alerts"}

POSITIVE_WORDS = {
    "approval", "approved", "bullish", "breakout", "inflow", "adoption",
    "partnership", "rally", "surge", "record", "accumulate", "buy",
}
NEGATIVE_WORDS = {
    "hack", "exploit", "lawsuit", "ban", "bearish", "outflow", "liquidation",
    "crash", "probe", "fraud", "selloff", "risk", "regulation",
}
RISK_WORDS = {
    "hack", "exploit", "lawsuit", "sec", "cftc", "ban", "fraud",
    "liquidation", "depeg", "bankruptcy", "sanction", "attack",
}
MACRO_RISK_WORDS = {
    "war", "tariff", "sanction", "inflation", "recession", "default",
    "shutdown", "crisis", "banking", "stress", "unemployment", "layoff",
    "oil", "yield", "treasury", "rate hike", "geopolitical", "conflict",
}
POLICY_WORDS = {
    "federal reserve", "fed", "fomc", "powell", "rate", "rates",
    "monetary policy", "treasury", "central bank", "cpi", "ppi",
}


@dataclass
class Article:
    category: str
    source: str
    title: str
    url: str
    published_at: str | None


def main() -> None:
    setup_logging()
    now = datetime.now(timezone.utc)
    profile = os.getenv("COLLECTOR_PROFILE", "context").strip().lower()

    prepare_directories(now)

    if profile in FLOW_ALERT_PROFILES:
        run_flow_alert(now)
    else:
        run_context(now)


def prepare_directories(now: datetime) -> None:
    (RAW_DIR / now.strftime("%Y-%m-%d")).mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)


def run_context(now: datetime) -> None:
    lookback_hours = int(os.getenv("CONTEXT_LOOKBACK_HOURS", "12"))
    cutoff = now - timedelta(hours=lookback_hours)
    raw_dir = RAW_DIR / now.strftime("%Y-%m-%d")

    articles = collect_rss(cutoff)
    gdelt = collect_gdelt()
    polymarket = collect_polymarket()
    context = build_context(now, lookback_hours, articles, gdelt, polymarket)
    context["macro_indicators"] = collect_macro_indicators_summary(now)
    context["asset_universe"] = collect_asset_universe_summary(now)
    context["hip4_outcome"] = collect_hip4_outcome_summary(now)
    context["day_swing"] = collect_day_swing_summary(now, context)
    context["relationship_scan"] = collect_relationship_scan_summary(now)
    context["sector_reactions"] = collect_sector_reactions_summary(now, context)
    context["asset_features"] = collect_asset_features_summary(now)
    context["ai_index"] = collect_ai_index_summary(now, context)

    (raw_dir / f"rss_{now.strftime('%H%M%S')}.json").write_text(
        json.dumps([asdict(a) for a in articles], indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (raw_dir / f"gdelt_{now.strftime('%H%M%S')}.json").write_text(
        json.dumps(gdelt, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (raw_dir / f"polymarket_{now.strftime('%H%M%S')}.json").write_text(
        json.dumps(polymarket, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    CONTEXT_FILE.write_text(json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8")
    append_history(context)
    append_polymarket_outcome_history(now, polymarket, profile="context")
    REPORT_FILE.write_text(render_report(context), encoding="utf-8")
    logging.info("Wrote %s", CONTEXT_FILE)


def collect_day_swing_summary(now: datetime, context: dict[str, Any]) -> dict[str, Any]:
    try:
        return update_day_swing_dataset(now, context)
    except Exception as e:
        logging.warning("Day/swing dataset update failed: %s", e)
        return {"enabled": True, "error": str(e)}


def collect_ai_index_summary(now: datetime, context: dict[str, Any]) -> dict[str, Any]:
    try:
        return update_ai_index(now, context)
    except Exception as e:
        logging.warning("AI index update failed: %s", e)
        return {"enabled": True, "error": str(e)}


def collect_relationship_scan_summary(now: datetime) -> dict[str, Any]:
    try:
        return update_relationship_scan(now)
    except Exception as e:
        logging.warning("Relationship scan update failed: %s", e)
        return {"enabled": True, "error": str(e)}


def collect_sector_reactions_summary(now: datetime, context: dict[str, Any]) -> dict[str, Any]:
    try:
        return update_sector_reactions(now, context)
    except Exception as e:
        logging.warning("Sector reactions update failed: %s", e)
        return {"enabled": True, "error": str(e)}


def collect_asset_features_summary(now: datetime) -> dict[str, Any]:
    try:
        return update_asset_features(now)
    except Exception as e:
        logging.warning("Asset feature update failed: %s", e)
        return {"enabled": True, "error": str(e)}


def collect_macro_indicators_summary(now: datetime) -> dict[str, Any]:
    try:
        return update_macro_indicators(now)
    except Exception as e:
        logging.warning("Macro indicator update failed: %s", e)
        return {"enabled": True, "error": str(e)}


def collect_asset_universe_summary(now: datetime) -> dict[str, Any]:
    try:
        return update_asset_universe_snapshot(now)
    except Exception as e:
        logging.warning("Asset universe update failed: %s", e)
        return {"enabled": True, "error": str(e)}


def collect_hip4_outcome_summary(now: datetime) -> dict[str, Any]:
    try:
        return update_hip4_outcome_snapshot(now)
    except Exception as e:
        logging.warning("HIP-4 outcome update failed: %s", e)
        return {"enabled": True, "error": str(e)}


def run_flow_alert(now: datetime) -> None:
    lookback_hours = int(os.getenv("FLOW_ALERT_LOOKBACK_HOURS", "24"))
    raw_dir = RAW_DIR / now.strftime("%Y-%m-%d")

    polymarket = collect_polymarket()
    dune_large_flows = collect_dune_large_flows()
    previous_history = load_json(FLOW_ALERT_HISTORY_FILE, default=[])
    if not isinstance(previous_history, list):
        previous_history = []
    alert = build_flow_alert(now, lookback_hours, polymarket, dune_large_flows, previous_history)

    (raw_dir / f"polymarket_alert_{now.strftime('%H%M%S')}.json").write_text(
        json.dumps(polymarket, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (raw_dir / f"dune_large_flows_{now.strftime('%H%M%S')}.json").write_text(
        json.dumps(dune_large_flows, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    FLOW_ALERT_FILE.write_text(json.dumps(alert, indent=2, ensure_ascii=False), encoding="utf-8")
    append_flow_alert_history(alert)
    if os.getenv("POLYMARKET_OUTCOME_HISTORY_FROM_FLOW", "false").lower() == "true":
        append_polymarket_outcome_history(now, polymarket, profile="flow_alert")
    FLOW_ALERT_REPORT_FILE.write_text(render_flow_alert_report(alert), encoding="utf-8")
    logging.info("Wrote %s", FLOW_ALERT_FILE)


def setup_logging() -> None:
    logging.basicConfig(
        level=getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )


def collect_rss(cutoff: datetime) -> list[Article]:
    feed_groups = [
        ("crypto", parse_csv_env("RSS_FEEDS", DEFAULT_RSS_FEEDS)),
        ("macro", parse_csv_env("MACRO_RSS_FEEDS", DEFAULT_MACRO_RSS_FEEDS)),
        ("policy", parse_csv_env("POLICY_RSS_FEEDS", DEFAULT_POLICY_RSS_FEEDS)),
        ("commodity", parse_csv_env("COMMODITY_RSS_FEEDS", DEFAULT_COMMODITY_RSS_FEEDS)),
    ]
    item_limit = int(os.getenv("RSS_ITEMS_PER_FEED", "30"))
    articles: list[Article] = []
    for category, feeds in feed_groups:
        articles.extend(collect_rss_group(category, feeds, cutoff, item_limit))
    articles.sort(key=lambda item: item.published_at or "", reverse=True)
    return articles


def collect_rss_group(
    category: str,
    feeds: list[str],
    cutoff: datetime,
    item_limit: int,
) -> list[Article]:
    articles: list[Article] = []
    for feed_url in feeds:
        try:
            parsed = feedparser.parse(feed_url)
            source = parsed.feed.get("title", feed_url)
            for entry in parsed.entries[:item_limit]:
                published = parse_entry_time(entry)
                if published and published < cutoff:
                    continue
                articles.append(
                    Article(
                        category=category,
                        source=source,
                        title=entry.get("title", "").strip(),
                        url=entry.get("link", "").strip(),
                        published_at=published.isoformat() if published else None,
                    )
                )
        except Exception as e:
            logging.warning("RSS failed for %s: %s", feed_url, e)
    return articles


def collect_gdelt() -> list[dict[str, Any]]:
    queries = [q.strip() for q in os.getenv("GDELT_QUERIES", DEFAULT_GDELT_QUERIES).split(",") if q.strip()]
    rows = []
    for query in queries:
        try:
            response = requests.get(
                "https://api.gdeltproject.org/api/v2/doc/doc",
                params={
                    "query": query,
                    "mode": "timelinevolraw",
                    "format": "json",
                    "timespan": "24h",
                },
                timeout=15,
            )
            response.raise_for_status()
            rows.append({"query": query, "data": response.json()})
        except Exception as e:
            logging.warning("GDELT failed for %s: %s", query, e)
            rows.append({"query": query, "error": str(e)})
    return rows


def collect_polymarket() -> list[dict[str, Any]]:
    query_values = os.getenv("POLYMARKET_QUERIES", os.getenv("POLYMARKET_QUERY", "crypto"))
    queries = [item.strip() for item in query_values.split(",") if item.strip()]
    limit = int(os.getenv("POLYMARKET_MARKET_LIMIT", "80"))
    discovery_limit = int(os.getenv("POLYMARKET_DISCOVERY_LIMIT", str(limit)))
    filter_mode = os.getenv("POLYMARKET_FILTER_MODE", "watch").strip().lower()
    tag_ids = [item.strip() for item in os.getenv("POLYMARKET_TAG_IDS", "").split(",") if item.strip()]
    event_slugs = parse_csv_env("POLYMARKET_EVENT_SLUGS", DEFAULT_POLYMARKET_EVENT_SLUGS)
    keep_event_markets = os.getenv("POLYMARKET_KEEP_EVENT_MARKETS", "true").lower() == "true"
    markets_by_slug: dict[str, dict[str, Any]] = {}
    event_market_slugs: set[str] = set()
    try:
        market_batches = [fetch_polymarket_markets({"limit": discovery_limit})]
        for tag_id in tag_ids:
            market_batches.append(
                fetch_polymarket_markets(
                    {
                        "limit": min(discovery_limit, 100),
                        "tag_id": tag_id,
                        "related_tags": "true",
                    }
                )
            )
        for event_slug in event_slugs:
            event_markets = fetch_polymarket_event_markets(event_slug)
            event_market_slugs.update(
                str(market.get("slug") or market.get("conditionId") or market.get("id") or "")
                for market in event_markets
                if isinstance(market, dict)
            )
            market_batches.append(event_markets)
        for markets in market_batches:
            for market in markets:
                add_polymarket_candidate(markets_by_slug, market, queries, filter_mode)
        rows = list(markets_by_slug.values())
        rows.sort(key=market_rank, reverse=True)
        if keep_event_markets and event_market_slugs:
            top = rows[:limit]
            existing = {str(row.get("slug") or row.get("conditionId") or row.get("id") or "") for row in top}
            event_tail = [
                row for row in rows[limit:]
                if str(row.get("slug") or row.get("conditionId") or row.get("id") or "") in event_market_slugs
                and str(row.get("slug") or row.get("conditionId") or row.get("id") or "") not in existing
            ]
            return top + event_tail
        return rows[:limit]
    except Exception as e:
        logging.warning("Polymarket failed: %s", e)
        return [{"error": str(e)}]


def fetch_polymarket_markets(extra_params: dict[str, Any]) -> list[dict[str, Any]]:
    params: dict[str, Any] = {
        "active": "true",
        "closed": "false",
        "order": "volume24hr",
        "ascending": "false",
        "include_tag": "true",
    }
    params.update(extra_params)
    response = requests.get(
        "https://gamma-api.polymarket.com/markets",
        params=params,
        timeout=15,
    )
    response.raise_for_status()
    data = response.json()
    markets = data if isinstance(data, list) else data.get("markets", [])
    return [market for market in markets if isinstance(market, dict)]


def fetch_polymarket_event_markets(event_slug: str) -> list[dict[str, Any]]:
    response = requests.get(
        "https://gamma-api.polymarket.com/events",
        params={"slug": event_slug},
        timeout=15,
    )
    response.raise_for_status()
    data = response.json()
    events = data if isinstance(data, list) else data.get("events", [])
    if not isinstance(events, list):
        return []

    rows: list[dict[str, Any]] = []
    for event in events:
        if not isinstance(event, dict):
            continue
        event_info = {
            "id": event.get("id"),
            "slug": event.get("slug") or event_slug,
            "title": event.get("title"),
            "ticker": event.get("ticker"),
        }
        markets = event.get("markets", [])
        if not isinstance(markets, list):
            continue
        for market in markets:
            if not isinstance(market, dict):
                continue
            enriched = dict(market)
            enriched.setdefault("events", [event_info])
            enriched.setdefault("eventSlug", event_info["slug"])
            rows.append(enriched)
    return rows


def add_polymarket_candidate(
    markets_by_slug: dict[str, dict[str, Any]],
    market: dict[str, Any],
    watch_terms: list[str],
    filter_mode: str,
) -> None:
    impact_label = classify_polymarket_market(market, watch_terms)
    if filter_mode == "crypto" and impact_label != "crypto":
        return
    if filter_mode in {"watch", "impact"} and impact_label == "other":
        return
    slug = str(market.get("slug") or market.get("conditionId") or market.get("id") or "")
    if not slug:
        return
    enriched = dict(market)
    enriched["query"] = impact_label
    enriched["impact_category"] = impact_label
    existing = markets_by_slug.get(slug)
    if existing is None or market_rank(enriched) > market_rank(existing):
        markets_by_slug[slug] = enriched


def collect_dune_large_flows() -> dict[str, Any]:
    query_id = os.getenv("DUNE_LARGE_FLOW_QUERY_ID", "").strip()
    api_key = os.getenv("DUNE_API_KEY", "").strip()
    result_limit = int(os.getenv("DUNE_RESULT_LIMIT", "100"))
    columns = os.getenv(
        "DUNE_RESULT_COLUMNS",
        "block_time,tx_hash,wallet,usdc_amount,amount,amount_usd",
    ).strip()

    if not query_id:
        return {"enabled": False, "reason": "DUNE_LARGE_FLOW_QUERY_ID is not set", "rows": []}
    if not api_key:
        return {"enabled": False, "query_id": query_id, "reason": "DUNE_API_KEY is not set", "rows": []}

    params: dict[str, Any] = {"limit": result_limit}
    if columns:
        params["columns"] = columns

    try:
        response = requests.get(
            f"https://api.dune.com/api/v1/query/{query_id}/results",
            headers={"X-Dune-Api-Key": api_key},
            params=params,
            timeout=20,
        )
        response.raise_for_status()
        payload = response.json()
        result = payload.get("result", {}) if isinstance(payload, dict) else {}
        return {
            "enabled": True,
            "query_id": query_id,
            "state": payload.get("state") if isinstance(payload, dict) else None,
            "execution_ended_at": payload.get("execution_ended_at") if isinstance(payload, dict) else None,
            "row_count": result.get("metadata", {}).get("row_count"),
            "rows": result.get("rows", []),
        }
    except Exception as e:
        logging.warning("Dune large-flow fetch failed: %s", e)
        return {"enabled": True, "query_id": query_id, "error": str(e), "rows": []}


def build_context(
    now: datetime,
    lookback_hours: int,
    articles: list[Article],
    gdelt: list[dict[str, Any]],
    polymarket: list[dict[str, Any]],
) -> dict[str, Any]:
    titles = [a.title for a in articles]
    category_summaries = summarize_news_categories(articles)
    sentiment = score_words(titles, POSITIVE_WORDS, NEGATIVE_WORDS)
    risk_hits = count_words(titles, RISK_WORDS | MACRO_RISK_WORDS)
    crypto_summary = category_summaries.get("crypto", {})
    crypto_article_count = int(crypto_summary.get("article_count", 0))
    macro_article_count = sum(
        int(summary.get("article_count", 0))
        for category, summary in category_summaries.items()
        if category != "crypto"
    )
    crypto_risk_headlines = crypto_summary.get("risk_headline_count", 0)
    macro_risk_headlines = sum(
        int(summary.get("risk_headline_count", 0))
        for category, summary in category_summaries.items()
        if category != "crypto"
    )
    policy_hits = count_words(titles, POLICY_WORDS)
    policy_headlines = count_texts_with_words(titles, POLICY_WORDS)
    news_count = len(articles)
    crypto_risk_rate = safe_ratio(crypto_risk_headlines, crypto_article_count)
    macro_risk_rate = safe_ratio(macro_risk_headlines, macro_article_count)
    policy_rate = safe_ratio(policy_headlines, news_count)
    news_volume_pressure = clamp(max(0, news_count - 40) * 0.25, 0, 8)
    news_risk_score = clamp(
        18 + crypto_risk_rate * 45 + macro_risk_rate * 30 + policy_rate * 15 + news_volume_pressure,
        0,
        100,
    )
    macro_risk_score = clamp(12 + macro_risk_rate * 60 + policy_rate * 25, 0, 100)
    risk_on_score = clamp(50 + sentiment * 20 - crypto_risk_rate * 30 - macro_risk_rate * 20, 0, 100)
    gdelt_activity = summarize_gdelt(gdelt)
    polymarket_summary = summarize_polymarket(polymarket)

    return {
        "generated_at": now.isoformat(),
        "lookback_hours": lookback_hours,
        "news": {
            "article_count": news_count,
            "sentiment_score": round(sentiment, 4),
            "risk_keyword_hits": risk_hits,
            "risk_headline_count": count_texts_with_words(titles, RISK_WORDS | MACRO_RISK_WORDS),
            "crypto_risk_headline_rate": round(crypto_risk_rate, 4),
            "macro_risk_headline_rate": round(macro_risk_rate, 4),
            "policy_keyword_hits": policy_hits,
            "policy_headline_count": policy_headlines,
            "policy_headline_rate": round(policy_rate, 4),
            "categories": category_summaries,
            "top_headlines": [asdict(a) for a in articles[:20]],
        },
        "gdelt": gdelt_activity,
        "polymarket": polymarket_summary,
        "scores": {
            "news_risk_score": round(news_risk_score, 2),
            "macro_risk_score": round(macro_risk_score, 2),
            "risk_on_score": round(risk_on_score, 2),
            "market_context_score": round(
                (100 - news_risk_score) * 0.38
                + (100 - macro_risk_score) * 0.17
                + risk_on_score * 0.45,
                2,
            ),
        },
        "errors": collect_errors(gdelt, polymarket),
    }


def build_flow_alert(
    now: datetime,
    lookback_hours: int,
    polymarket: list[dict[str, Any]],
    dune_large_flows: dict[str, Any],
    previous_history: list[dict[str, Any]],
) -> dict[str, Any]:
    large_flows = summarize_large_flows(dune_large_flows)
    polymarket_flow = summarize_polymarket_flow(polymarket)

    inflow_values = [
        to_float(item.get("large_flows", {}).get("large_usdc_inflow"))
        for item in previous_history[-2016:]
        if isinstance(item, dict)
    ]
    market_volume_values = [
        to_float(item.get("polymarket", {}).get("volume_24h"))
        for item in previous_history[-2016:]
        if isinstance(item, dict)
    ]
    large_flows["inflow_zscore_7d"] = round(zscore(large_flows["large_usdc_inflow"], inflow_values), 2)
    polymarket_flow["volume_24h_zscore_7d"] = round(zscore(polymarket_flow["volume_24h"], market_volume_values), 2)

    score = score_flow_alert(large_flows, polymarket_flow)
    return {
        "generated_at": now.isoformat(),
        "profile": "flow_alert",
        "lookback_hours": lookback_hours,
        "large_flows": large_flows,
        "polymarket": polymarket_flow,
        "scores": {
            "flow_alert_score": round(score, 2),
            "flow_alert_level": classify_flow_alert(score),
        },
        "errors": collect_flow_errors(dune_large_flows, polymarket),
    }


def parse_entry_time(entry: Any) -> datetime | None:
    for key in ("published", "updated", "created"):
        value = entry.get(key)
        if not value:
            continue
        try:
            parsed = date_parser.parse(value)
            return parsed.astimezone(timezone.utc) if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)
        except Exception:
            continue
    return None


def score_words(texts: list[str], positive: set[str], negative: set[str]) -> float:
    pos = count_words(texts, positive)
    neg = count_words(texts, negative)
    total = pos + neg
    return 0.0 if total == 0 else (pos - neg) / total


def count_words(texts: list[str], words: set[str]) -> int:
    count = 0
    for text in texts:
        lower = text.lower()
        count += sum(1 for word in words if word in lower)
    return count


def count_texts_with_words(texts: list[str], words: set[str]) -> int:
    count = 0
    for text in texts:
        lower = text.lower()
        if any(word in lower for word in words):
            count += 1
    return count


def summarize_gdelt(rows: list[dict[str, Any]]) -> dict[str, Any]:
    summary = []
    for row in rows:
        points = row.get("data", {}).get("timeline", []) if isinstance(row.get("data"), dict) else []
        values = [float(p.get("value", 0)) for p in points if isinstance(p, dict)]
        summary.append({
            "query": row.get("query"),
            "points": len(values),
            "avg_volume": round(sum(values) / len(values), 4) if values else 0.0,
            "latest_volume": round(values[-1], 4) if values else 0.0,
        })
    return {"queries": summary}


def summarize_polymarket(markets: list[dict[str, Any]]) -> dict[str, Any]:
    clean = [m for m in markets if "error" not in m]
    rows = []
    for market in clean[:30]:
        rows.append(polymarket_summary_row(market))
    return {
        "market_count": len(clean),
        "top_markets": rows,
        "health_markets": [row for row in rows if is_public_health_polymarket(row)][:10],
    }


def summarize_news_categories(articles: list[Article]) -> dict[str, Any]:
    grouped: dict[str, list[Article]] = {}
    for article in articles:
        grouped.setdefault(article.category, []).append(article)

    output = {}
    for category, rows in sorted(grouped.items()):
        titles = [row.title for row in rows]
        risk_keyword_hits = count_words(titles, RISK_WORDS | MACRO_RISK_WORDS)
        policy_keyword_hits = count_words(titles, POLICY_WORDS)
        risk_headline_count = count_texts_with_words(titles, RISK_WORDS | MACRO_RISK_WORDS)
        policy_headline_count = count_texts_with_words(titles, POLICY_WORDS)
        output[category] = {
            "article_count": len(rows),
            "sentiment_score": round(score_words(titles, POSITIVE_WORDS, NEGATIVE_WORDS), 4),
            "risk_keyword_hits": risk_keyword_hits,
            "risk_headline_count": risk_headline_count,
            "risk_headline_rate": round(safe_ratio(risk_headline_count, len(rows)), 4),
            "policy_keyword_hits": policy_keyword_hits,
            "policy_headline_count": policy_headline_count,
            "policy_headline_rate": round(safe_ratio(policy_headline_count, len(rows)), 4),
            "top_headlines": [asdict(row) for row in rows[:8]],
        }
    return output


def summarize_large_flows(dune_large_flows: dict[str, Any]) -> dict[str, Any]:
    rows = dune_large_flows.get("rows", [])
    if not isinstance(rows, list):
        rows = []

    amounts = [extract_usdc_amount(row) for row in rows if isinstance(row, dict)]
    amounts = [amount for amount in amounts if amount > 0]
    wallets = {
        str(row.get("wallet") or row.get("from") or row.get("address"))
        for row in rows
        if isinstance(row, dict) and (row.get("wallet") or row.get("from") or row.get("address"))
    }
    latest_time = max(
        (str(row.get("block_time") or row.get("timestamp") or "") for row in rows if isinstance(row, dict)),
        default="",
    )

    return {
        "enabled": bool(dune_large_flows.get("enabled")),
        "query_id": dune_large_flows.get("query_id"),
        "large_usdc_tx_count": len(amounts),
        "large_usdc_inflow": round(sum(amounts), 2),
        "max_large_usdc_transfer": round(max(amounts), 2) if amounts else 0.0,
        "unique_large_wallets": len(wallets),
        "latest_transfer_at": latest_time or None,
        "source_state": dune_large_flows.get("state"),
        "source_execution_ended_at": dune_large_flows.get("execution_ended_at"),
        "source_reason": dune_large_flows.get("reason"),
    }


def summarize_polymarket_flow(markets: list[dict[str, Any]]) -> dict[str, Any]:
    clean = [m for m in markets if "error" not in m]
    rows = []
    for market in clean:
        volume_24h = to_float(market.get("volume24hr") or market.get("volume24hrClob"))
        lifetime_volume = to_float(market.get("volume") or market.get("volumeNum"))
        row = polymarket_summary_row(market)
        row["volume_24h"] = volume_24h
        row["volume"] = lifetime_volume
        rows.append(row)

    rows.sort(key=lambda item: (item["volume_24h"], item["volume"], item["liquidity"]), reverse=True)
    return {
        "market_count": len(clean),
        "volume_24h": round(sum(item["volume_24h"] for item in rows), 2),
        "lifetime_volume": round(sum(item["volume"] for item in rows), 2),
        "liquidity": round(sum(item["liquidity"] for item in rows), 2),
        "top_markets": rows[:10],
        "health_markets": [row for row in rows if is_public_health_polymarket(row)][:10],
    }


def polymarket_summary_row(market: dict[str, Any]) -> dict[str, Any]:
    outcomes = parse_polymarket_outcomes(market)
    yes_probability = find_outcome_probability(outcomes, "yes")
    no_probability = find_outcome_probability(outcomes, "no")
    event_slug = polymarket_event_slug(market)
    market_slug = market.get("slug")
    url = (
        f"https://polymarket.com/event/{event_slug}"
        if event_slug
        else f"https://polymarket.com/market/{market_slug}" if market_slug else None
    )
    return {
        "question": market.get("question") or market.get("title"),
        "slug": market_slug,
        "event_slug": event_slug,
        "url": url,
        "query": market.get("query"),
        "impact_category": market.get("impact_category"),
        "volume_24h": to_float(market.get("volume24hr") or market.get("volume24hrClob") or market.get("volume_24h")),
        "volume": to_float(market.get("volume") or market.get("volumeNum")),
        "liquidity": to_float(market.get("liquidity") or market.get("liquidityNum")),
        "end_date": market.get("endDate") or market.get("endDateIso") or market.get("end_date_iso") or market.get("end_date"),
        "outcomes": outcomes[:6],
        "yes_probability": yes_probability,
        "no_probability": no_probability,
    }


def polymarket_event_slug(market: dict[str, Any]) -> str | None:
    events = market.get("events")
    if isinstance(events, list):
        for event in events:
            if isinstance(event, dict) and event.get("slug"):
                return str(event["slug"])
    for key in ("eventSlug", "event_slug"):
        value = market.get(key)
        if value:
            return str(value)
    return None


def parse_polymarket_outcomes(market: dict[str, Any]) -> list[dict[str, Any]]:
    labels = parse_polymarket_list(market.get("outcomes") or market.get("shortOutcomes"))
    prices = parse_polymarket_list(market.get("outcomePrices") or market.get("outcome_prices"))
    token_ids = parse_polymarket_list(market.get("clobTokenIds") or market.get("clob_token_ids"))
    count = max(len(labels), len(prices), len(token_ids))
    outcomes = []
    for index in range(count):
        label = str(labels[index]) if index < len(labels) and labels[index] is not None else f"Outcome {index + 1}"
        outcomes.append(
            {
                "name": label,
                "probability": to_float_or_none(prices[index]) if index < len(prices) else None,
                "token_id": str(token_ids[index]) if index < len(token_ids) and token_ids[index] is not None else None,
            }
        )
    return outcomes


def parse_polymarket_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    if isinstance(value, str) and value.strip():
        try:
            parsed = json.loads(value)
            return parsed if isinstance(parsed, list) else []
        except Exception:
            return [part.strip() for part in value.split(",") if part.strip()]
    return []


def find_outcome_probability(outcomes: list[dict[str, Any]], label: str) -> float | None:
    for outcome in outcomes:
        name = str(outcome.get("name", "")).strip().lower()
        if name == label:
            return to_float_or_none(outcome.get("probability"))
    return None


def append_polymarket_outcome_history(
    now: datetime,
    markets: list[dict[str, Any]],
    profile: str,
) -> None:
    max_records = int(os.getenv("POLYMARKET_OUTCOME_HISTORY_MAX_RECORDS", "75000"))
    history = load_json(POLYMARKET_OUTCOME_HISTORY_FILE, default=[])
    if not isinstance(history, list):
        history = []

    observed_at = floor_time(now, int(os.getenv("POLYMARKET_OUTCOME_HISTORY_BUCKET_MINUTES", "15"))).isoformat()
    rows = build_polymarket_outcome_history_rows(observed_at, markets, profile)
    if not rows:
        return

    existing_keys = {polymarket_outcome_history_key(row) for row in history}
    for row in rows:
        key = polymarket_outcome_history_key(row)
        if key in existing_keys:
            continue
        history.append(row)
        existing_keys.add(key)

    if len(history) > max_records:
        archive_polymarket_outcome_rows(history[:-max_records])
        history = history[-max_records:]
    POLYMARKET_OUTCOME_HISTORY_FILE.write_text(json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8")
    POLYMARKET_OUTCOME_LATEST_FILE.write_text(
        json.dumps(latest_polymarket_outcome_rows(history), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def archive_polymarket_outcome_rows(rows: list[dict[str, Any]]) -> None:
    if not rows or os.getenv("POLYMARKET_OUTCOME_ARCHIVE_ENABLED", "true").lower() == "false":
        return
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        observed_at = str(row.get("observed_at") or "")
        month = observed_at[:7] if re.match(r"^\d{4}-\d{2}", observed_at) else "unknown"
        grouped.setdefault(month, []).append(row)
    for month, month_rows in grouped.items():
        target = ARCHIVE_DIR / f"polymarket_outcome_history_{month}.jsonl.gz"
        with gzip.open(target, "at", encoding="utf-8") as f:
            for row in month_rows:
                f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def build_polymarket_outcome_history_rows(
    observed_at: str,
    markets: list[dict[str, Any]],
    profile: str,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for market in markets:
        if not isinstance(market, dict) or market.get("error"):
            continue
        summary = polymarket_summary_row(market)
        outcomes = polymarket_outcomes_for_history(market)
        if not isinstance(outcomes, list):
            continue
        subject_name = infer_polymarket_subject_name(summary)
        for outcome in outcomes:
            if not isinstance(outcome, dict):
                continue
            outcome_name = str(outcome.get("name") or "").strip() or None
            probability = to_float_or_none(outcome.get("probability"))
            token_id = str(outcome.get("token_id")) if outcome.get("token_id") else None
            if probability is None and token_id is None:
                continue
            rows.append(
                {
                    "observed_at": observed_at,
                    "profile": profile,
                    "event_slug": summary.get("event_slug"),
                    "market_slug": summary.get("slug"),
                    "question": summary.get("question"),
                    "impact_category": summary.get("impact_category"),
                    "subject_name": subject_name,
                    "person_name": subject_name or non_binary_outcome_name(outcome_name),
                    "outcome_name": outcome_name,
                    "probability": probability,
                    "token_id": token_id,
                    "volume_24h": summary.get("volume_24h"),
                    "volume": summary.get("volume"),
                    "liquidity": summary.get("liquidity"),
                    "end_date": summary.get("end_date"),
                }
            )
    return rows


def polymarket_outcomes_for_history(market: dict[str, Any]) -> list[dict[str, Any]]:
    outcomes = market.get("outcomes")
    if isinstance(outcomes, list) and outcomes and all(isinstance(item, dict) for item in outcomes):
        return outcomes
    return parse_polymarket_outcomes(market)


def polymarket_outcome_history_key(row: dict[str, Any]) -> tuple[Any, ...]:
    return (
        row.get("observed_at"),
        row.get("profile"),
        row.get("market_slug"),
        row.get("token_id"),
        row.get("outcome_name"),
    )


def latest_polymarket_outcome_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    latest: dict[tuple[Any, ...], dict[str, Any]] = {}
    for row in rows:
        key = (
            row.get("event_slug"),
            row.get("market_slug"),
            row.get("token_id"),
            row.get("outcome_name"),
        )
        current = latest.get(key)
        if current is None or str(row.get("observed_at") or "") > str(current.get("observed_at") or ""):
            latest[key] = row
    return sorted(
        latest.values(),
        key=lambda item: (
            str(item.get("event_slug") or ""),
            str(item.get("person_name") or item.get("subject_name") or item.get("outcome_name") or ""),
        ),
    )


def infer_polymarket_subject_name(market: dict[str, Any]) -> str | None:
    question = str(market.get("question") or "").strip()
    patterns = [
        r"^Will\s+(.+?)\s+win\b",
        r"^Will\s+(.+?)\s+be(?:come)?\s+(?:the\s+)?(?:next\s+)?",
        r"^Will\s+(.+?)\s+run\b",
        r"^Will\s+(.+?)\s+announce\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, question, flags=re.IGNORECASE)
        if match:
            return clean_polymarket_subject_name(match.group(1))
    return None


def clean_polymarket_subject_name(value: str) -> str | None:
    cleaned = value.strip(" ?'\"")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned or None


def non_binary_outcome_name(outcome_name: str | None) -> str | None:
    if not outcome_name:
        return None
    if outcome_name.strip().lower() in {"yes", "no"}:
        return None
    return outcome_name


def is_crypto_market(market: dict[str, Any]) -> bool:
    text = " ".join(
        str(market.get(key, ""))
        for key in ("question", "title", "slug")
    ).lower()
    return any(re.search(rf"\b{re.escape(word)}\b", text) for word in CRYPTO_MARKET_WORDS)


def classify_polymarket_market(market: dict[str, Any], watch_terms: list[str]) -> str:
    text = polymarket_search_text(market)
    if any(re.search(rf"\b{re.escape(word.lower())}\b", text) for word in CRYPTO_MARKET_WORDS):
        return "crypto"
    categories = {
        "geopolitics": {
            "war", "military", "conflict", "ceasefire", "invasion", "missile",
            "israel", "iran", "ukraine", "russia", "china", "taiwan", "nato",
        },
        "policy": {
            "election", "president", "congress", "senate", "trump", "tariff",
            "federal government", "supreme court", "law", "regulation",
        },
        "macro": {
            "federal reserve", "fed", "interest", "rates", "inflation", "cpi",
            "recession", "unemployment", "gdp", "ecb", "treasury",
        },
        "health": PUBLIC_HEALTH_MARKET_WORDS,
        "commodity": {"oil", "gold", "gas", "wheat", "corn", "copper"},
        "equity": {"stock", "stocks", "nasdaq", "s&p", "sp500", "dow", "earnings"},
    }
    for label, words in categories.items():
        if any(re.search(rf"\b{re.escape(word)}\b", text) for word in words):
            return label
    for term in watch_terms:
        term = term.lower()
        if term and re.search(rf"\b{re.escape(term)}\b", text):
            return term
    return "other"


def polymarket_search_text(market: dict[str, Any]) -> str:
    parts = [
        str(market.get(key, ""))
        for key in ("question", "title", "slug", "description", "category")
    ]
    for key in ("tags", "categories", "events"):
        value = market.get(key)
        if isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    parts.extend(str(item.get(field, "")) for field in ("label", "slug", "title"))
    return " ".join(parts).lower()


def is_public_health_polymarket(market: dict[str, Any]) -> bool:
    text = polymarket_search_text(market)
    return any(re.search(rf"\b{re.escape(word)}\b", text) for word in PUBLIC_HEALTH_MARKET_WORDS)


def market_rank(market: dict[str, Any]) -> float:
    return (
        to_float(market.get("volume24hr") or market.get("volume24hrClob")) * 10
        + to_float(market.get("volume") or market.get("volumeNum"))
        + to_float(market.get("liquidity") or market.get("liquidityNum")) * 2
    )


def collect_errors(gdelt: list[dict[str, Any]], polymarket: list[dict[str, Any]]) -> list[str]:
    errors = [f"GDELT {row.get('query')}: {row['error']}" for row in gdelt if row.get("error")]
    errors.extend(f"Polymarket: {row['error']}" for row in polymarket if row.get("error"))
    return errors


def collect_flow_errors(dune_large_flows: dict[str, Any], polymarket: list[dict[str, Any]]) -> list[str]:
    errors = [f"Polymarket: {row['error']}" for row in polymarket if row.get("error")]
    if dune_large_flows.get("error"):
        errors.append(f"Dune large flows: {dune_large_flows['error']}")
    return errors


def append_history(context: dict[str, Any]) -> None:
    max_records = int(os.getenv("HISTORY_MAX_RECORDS", "720"))
    if HISTORY_FILE.exists():
        try:
            history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        except Exception:
            history = []
    else:
        history = []
    if not isinstance(history, list):
        history = []
    history.append({
        "generated_at": context["generated_at"],
        "scores": context["scores"],
        "news": {
            "article_count": context["news"]["article_count"],
            "sentiment_score": context["news"]["sentiment_score"],
            "risk_keyword_hits": context["news"]["risk_keyword_hits"],
            "risk_headline_count": context["news"].get("risk_headline_count", 0),
            "crypto_risk_headline_rate": context["news"].get("crypto_risk_headline_rate", 0),
            "macro_risk_headline_rate": context["news"].get("macro_risk_headline_rate", 0),
            "policy_keyword_hits": context["news"].get("policy_keyword_hits", 0),
            "policy_headline_count": context["news"].get("policy_headline_count", 0),
            "policy_headline_rate": context["news"].get("policy_headline_rate", 0),
            "category_counts": {
                category: summary.get("article_count", 0)
                for category, summary in context["news"].get("categories", {}).items()
                if isinstance(summary, dict)
            },
            "category_risk_keyword_hits": {
                category: summary.get("risk_keyword_hits", 0)
                for category, summary in context["news"].get("categories", {}).items()
                if isinstance(summary, dict)
            },
        },
        "polymarket_market_count": context["polymarket"]["market_count"],
    })
    HISTORY_FILE.write_text(json.dumps(history[-max_records:], indent=2), encoding="utf-8")


def append_flow_alert_history(alert: dict[str, Any]) -> None:
    max_records = int(os.getenv("FLOW_ALERT_HISTORY_MAX_RECORDS", "2016"))
    history = load_json(FLOW_ALERT_HISTORY_FILE, default=[])
    if not isinstance(history, list):
        history = []
    history.append({
        "generated_at": alert["generated_at"],
        "scores": alert["scores"],
        "large_flows": {
            "large_usdc_tx_count": alert["large_flows"]["large_usdc_tx_count"],
            "large_usdc_inflow": alert["large_flows"]["large_usdc_inflow"],
            "max_large_usdc_transfer": alert["large_flows"]["max_large_usdc_transfer"],
            "unique_large_wallets": alert["large_flows"]["unique_large_wallets"],
        },
        "polymarket": {
            "market_count": alert["polymarket"]["market_count"],
            "volume_24h": alert["polymarket"]["volume_24h"],
            "lifetime_volume": alert["polymarket"]["lifetime_volume"],
        },
    })
    FLOW_ALERT_HISTORY_FILE.write_text(json.dumps(history[-max_records:], indent=2), encoding="utf-8")


def render_report(context: dict[str, Any]) -> str:
    headlines = "\n".join(
        f"- [{item.get('category', 'news')}] {item['title']} ({item['source']})"
        for item in context["news"]["top_headlines"][:10]
    )
    category_lines = render_news_categories(context.get("news", {}).get("categories", {}))
    day_swing = context.get("day_swing", {})
    day_swing_lines = ""
    if isinstance(day_swing, dict) and day_swing.get("enabled"):
        day_swing_lines = (
            f"- Day/swing records: `{day_swing.get('record_count')}`\n"
            f"- Day/swing latest: `{day_swing.get('latest_observed_at')}`\n\n"
        )
    asset_universe = context.get("asset_universe", {})
    asset_universe_lines = ""
    if isinstance(asset_universe, dict) and asset_universe.get("enabled"):
        class_counts = asset_universe.get("asset_class_counts", {})
        class_summary = ""
        if isinstance(class_counts, dict) and class_counts:
            class_summary = ", ".join(
                f"{asset_class}:{count}"
                for asset_class, count in sorted(class_counts.items())
            )
        hip3_dexes = asset_universe.get("hip3_dexes", [])
        hip3_summary = ""
        if isinstance(hip3_dexes, list) and hip3_dexes:
            hip3_summary = ", ".join(
                str(dex.get("name"))
                for dex in hip3_dexes
                if isinstance(dex, dict) and dex.get("enabled")
            )
        asset_universe_lines = (
            f"- Asset universe count: `{asset_universe.get('asset_count')}`\n"
            f"- Asset price history records: `{asset_universe.get('history_records')}`\n\n"
            f"- Asset classes: `{class_summary}`\n"
            f"- HIP-3 dexes: `{hip3_summary}`\n\n"
        )
    macro_indicators = context.get("macro_indicators", {})
    macro_lines = ""
    if isinstance(macro_indicators, dict) and macro_indicators.get("enabled"):
        macro_lines = (
            f"- Macro indicators: `{macro_indicators.get('indicator_count')}`\n"
            f"- Macro indicators file: `{macro_indicators.get('latest_file')}`\n\n"
        )
    sector_reactions = context.get("sector_reactions", {})
    sector_lines = ""
    if isinstance(sector_reactions, dict) and sector_reactions.get("enabled"):
        sector_lines = (
            f"- Sector reaction price records: `{sector_reactions.get('price_record_count')}`\n"
            f"- Sector reaction patterns: `{sector_reactions.get('pattern_count')}`\n\n"
        )
    return (
        "# Latest Crypto Context\n\n"
        f"- Generated: `{context['generated_at']}`\n"
        f"- Market context score: `{context['scores']['market_context_score']}`\n"
        f"- News risk score: `{context['scores']['news_risk_score']}`\n"
        f"- Macro risk score: `{context['scores'].get('macro_risk_score')}`\n"
        f"- Risk-on score: `{context['scores']['risk_on_score']}`\n"
        f"- Articles: `{context['news']['article_count']}`\n"
        f"- Polymarket markets: `{context['polymarket']['market_count']}`\n\n"
        f"{macro_lines}"
        f"{sector_lines}"
        f"{asset_universe_lines}"
        f"{day_swing_lines}"
        "## News Categories\n\n"
        f"{category_lines}\n\n"
        "## Headlines\n\n"
        f"{headlines or '- No recent headlines collected.'}\n"
    )


def render_flow_alert_report(alert: dict[str, Any]) -> str:
    markets = "\n".join(
        f"- {item['question']} | 24h volume: `{item['volume_24h']}` | liquidity: `{item['liquidity']}`"
        for item in alert["polymarket"]["top_markets"][:8]
    )
    return (
        "# Latest Flow Alert\n\n"
        f"- Generated: `{alert['generated_at']}`\n"
        f"- Flow alert score: `{alert['scores']['flow_alert_score']}`\n"
        f"- Flow alert level: `{alert['scores']['flow_alert_level']}`\n"
        f"- Large USDC inflow: `{alert['large_flows']['large_usdc_inflow']}`\n"
        f"- Large USDC tx count: `{alert['large_flows']['large_usdc_tx_count']}`\n"
        f"- Max transfer: `{alert['large_flows']['max_large_usdc_transfer']}`\n"
        f"- Unique wallets: `{alert['large_flows']['unique_large_wallets']}`\n"
        f"- Inflow z-score: `{alert['large_flows']['inflow_zscore_7d']}`\n"
        f"- Polymarket 24h volume: `{alert['polymarket']['volume_24h']}`\n"
        f"- Polymarket volume z-score: `{alert['polymarket']['volume_24h_zscore_7d']}`\n\n"
        "## Top Polymarket Markets\n\n"
        f"{markets or '- No active crypto markets collected.'}\n\n"
        "Public output stores aggregate flow data only. It is an attention signal, not proof of insider activity.\n"
    )


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def parse_csv_env(name: str, default: str) -> list[str]:
    value = os.getenv(name)
    if value is None:
        value = default
    return [item.strip() for item in value.split(",") if item.strip()]


def render_news_categories(categories: dict[str, Any]) -> str:
    if not isinstance(categories, dict) or not categories:
        return "- No category summary."
    rows = []
    for category, summary in sorted(categories.items()):
        if not isinstance(summary, dict):
            continue
        rows.append(
            f"- {category}: articles `{summary.get('article_count')}`, "
            f"risk hits `{summary.get('risk_keyword_hits')}`, "
            f"risk headline rate `{summary.get('risk_headline_rate')}`, "
            f"policy hits `{summary.get('policy_keyword_hits')}`"
        )
    return "\n".join(rows) if rows else "- No category summary."


def extract_usdc_amount(row: dict[str, Any]) -> float:
    for key in ("usdc_amount", "amount", "amount_usd", "value_usd", "value"):
        amount = to_float(row.get(key))
        if amount > 0:
            return amount
    return 0.0


def score_flow_alert(large_flows: dict[str, Any], polymarket_flow: dict[str, Any]) -> float:
    score = 0.0
    if large_flows.get("enabled"):
        score += min(35.0, large_flows["large_usdc_inflow"] / 25000)
        score += min(25.0, large_flows["large_usdc_tx_count"] * 5)
        score += min(20.0, large_flows["max_large_usdc_transfer"] / 10000)
        score += min(20.0, max(0.0, large_flows["inflow_zscore_7d"]) * 8)
    else:
        score += 5.0

    score += min(12.0, polymarket_flow["volume_24h"] / 50000)
    score += min(8.0, max(0.0, polymarket_flow["volume_24h_zscore_7d"]) * 4)
    return clamp(score, 0, 100)


def classify_flow_alert(score: float) -> str:
    if score >= 80:
        return "critical"
    if score >= 60:
        return "high"
    if score >= 35:
        return "elevated"
    return "baseline"


def zscore(current: float, previous_values: list[float]) -> float:
    values = [value for value in previous_values if value > 0]
    if len(values) < 12:
        return 0.0
    avg = sum(values) / len(values)
    variance = sum((value - avg) ** 2 for value in values) / len(values)
    stddev = variance ** 0.5
    if stddev == 0:
        return 0.0
    return (current - avg) / stddev


def safe_ratio(numerator: Any, denominator: Any) -> float:
    top = to_float(numerator)
    bottom = to_float(denominator)
    if bottom <= 0:
        return 0.0
    return top / bottom


def floor_time(dt: datetime, bucket_minutes: int) -> datetime:
    bucket = max(1, bucket_minutes)
    minute = (dt.minute // bucket) * bucket
    return dt.astimezone(timezone.utc).replace(minute=minute, second=0, microsecond=0)


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def to_float(value: Any) -> float:
    try:
        return float(value) if value is not None else 0.0
    except (TypeError, ValueError):
        return 0.0


def to_float_or_none(value: Any) -> float | None:
    try:
        return float(value) if value not in {None, ""} else None
    except (TypeError, ValueError):
        return None


if __name__ == "__main__":
    main()
