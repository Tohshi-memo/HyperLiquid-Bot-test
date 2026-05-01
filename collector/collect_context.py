from __future__ import annotations

import json
import logging
import os
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import feedparser
import requests
from dateutil import parser as date_parser

ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = ROOT / "data" / "processed"
RAW_DIR = ROOT / "data" / "raw"
REPORT_DIR = ROOT / "data" / "reports"
CONTEXT_FILE = PROCESSED_DIR / "market_context.json"
HISTORY_FILE = PROCESSED_DIR / "market_context_history.json"
REPORT_FILE = REPORT_DIR / "latest_context.md"
DEFAULT_RSS_FEEDS = (
    "https://cointelegraph.com/rss,"
    "https://www.coindesk.com/arc/outboundfeeds/rss/"
)
DEFAULT_GDELT_QUERIES = "bitcoin OR ethereum OR crypto OR stablecoin"
CRYPTO_MARKET_WORDS = {
    "btc", "bitcoin", "eth", "ethereum", "crypto", "stablecoin", "usdt",
    "usdc", "solana", "sol", "xrp", "doge", "hyperliquid", "binance", "megaeth",
}

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


@dataclass
class Article:
    source: str
    title: str
    url: str
    published_at: str | None


def main() -> None:
    setup_logging()
    now = datetime.now(timezone.utc)
    lookback_hours = int(os.getenv("CONTEXT_LOOKBACK_HOURS", "12"))
    cutoff = now - timedelta(hours=lookback_hours)

    raw_dir = RAW_DIR / now.strftime("%Y-%m-%d")
    raw_dir.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    articles = collect_rss(cutoff)
    gdelt = collect_gdelt()
    polymarket = collect_polymarket()
    context = build_context(now, lookback_hours, articles, gdelt, polymarket)

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
    REPORT_FILE.write_text(render_report(context), encoding="utf-8")
    logging.info("Wrote %s", CONTEXT_FILE)


def setup_logging() -> None:
    logging.basicConfig(
        level=getattr(logging, os.getenv("LOG_LEVEL", "INFO").upper(), logging.INFO),
        format="%(asctime)s [%(levelname)s] %(message)s",
    )


def collect_rss(cutoff: datetime) -> list[Article]:
    feeds = [x.strip() for x in os.getenv("RSS_FEEDS", DEFAULT_RSS_FEEDS).split(",") if x.strip()]
    articles: list[Article] = []
    for feed_url in feeds:
        try:
            parsed = feedparser.parse(feed_url)
            source = parsed.feed.get("title", feed_url)
            for entry in parsed.entries:
                published = parse_entry_time(entry)
                if published and published < cutoff:
                    continue
                articles.append(
                    Article(
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
    query = os.getenv("POLYMARKET_QUERY", "crypto")
    limit = int(os.getenv("POLYMARKET_MARKET_LIMIT", "80"))
    try:
        response = requests.get(
            "https://gamma-api.polymarket.com/markets",
            params={"active": "true", "closed": "false", "limit": limit, "q": query},
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()
        markets = data if isinstance(data, list) else data.get("markets", [])
        return [m for m in markets if is_crypto_market(m)]
    except Exception as e:
        logging.warning("Polymarket failed: %s", e)
        return [{"error": str(e)}]


def build_context(
    now: datetime,
    lookback_hours: int,
    articles: list[Article],
    gdelt: list[dict[str, Any]],
    polymarket: list[dict[str, Any]],
) -> dict[str, Any]:
    titles = [a.title for a in articles]
    sentiment = score_words(titles, POSITIVE_WORDS, NEGATIVE_WORDS)
    risk_hits = count_words(titles, RISK_WORDS)
    news_count = len(articles)
    news_risk_score = clamp(20 + risk_hits * 8 + max(0, news_count - 20), 0, 100)
    risk_on_score = clamp(50 + sentiment * 20 - risk_hits * 4, 0, 100)
    gdelt_activity = summarize_gdelt(gdelt)
    polymarket_summary = summarize_polymarket(polymarket)

    return {
        "generated_at": now.isoformat(),
        "lookback_hours": lookback_hours,
        "news": {
            "article_count": news_count,
            "sentiment_score": round(sentiment, 4),
            "risk_keyword_hits": risk_hits,
            "top_headlines": [asdict(a) for a in articles[:20]],
        },
        "gdelt": gdelt_activity,
        "polymarket": polymarket_summary,
        "scores": {
            "news_risk_score": round(news_risk_score, 2),
            "risk_on_score": round(risk_on_score, 2),
            "market_context_score": round((100 - news_risk_score) * 0.45 + risk_on_score * 0.55, 2),
        },
        "errors": collect_errors(gdelt, polymarket),
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
        rows.append({
            "question": market.get("question") or market.get("title"),
            "slug": market.get("slug"),
            "volume": to_float(market.get("volume")),
            "liquidity": to_float(market.get("liquidity")),
            "end_date": market.get("endDate") or market.get("end_date_iso"),
        })
    return {"market_count": len(clean), "top_markets": rows}


def is_crypto_market(market: dict[str, Any]) -> bool:
    text = " ".join(
        str(market.get(key, ""))
        for key in ("question", "title", "slug")
    ).lower()
    return any(re.search(rf"\b{re.escape(word)}\b", text) for word in CRYPTO_MARKET_WORDS)


def collect_errors(gdelt: list[dict[str, Any]], polymarket: list[dict[str, Any]]) -> list[str]:
    errors = [f"GDELT {row.get('query')}: {row['error']}" for row in gdelt if row.get("error")]
    errors.extend(f"Polymarket: {row['error']}" for row in polymarket if row.get("error"))
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
    history.append({
        "generated_at": context["generated_at"],
        "scores": context["scores"],
        "news": {
            "article_count": context["news"]["article_count"],
            "sentiment_score": context["news"]["sentiment_score"],
            "risk_keyword_hits": context["news"]["risk_keyword_hits"],
        },
        "polymarket_market_count": context["polymarket"]["market_count"],
    })
    HISTORY_FILE.write_text(json.dumps(history[-max_records:], indent=2), encoding="utf-8")


def render_report(context: dict[str, Any]) -> str:
    headlines = "\n".join(
        f"- {item['title']} ({item['source']})"
        for item in context["news"]["top_headlines"][:10]
    )
    return (
        "# Latest Crypto Context\n\n"
        f"- Generated: `{context['generated_at']}`\n"
        f"- Market context score: `{context['scores']['market_context_score']}`\n"
        f"- News risk score: `{context['scores']['news_risk_score']}`\n"
        f"- Risk-on score: `{context['scores']['risk_on_score']}`\n"
        f"- Articles: `{context['news']['article_count']}`\n"
        f"- Polymarket markets: `{context['polymarket']['market_count']}`\n\n"
        "## Headlines\n\n"
        f"{headlines or '- No recent headlines collected.'}\n"
    )


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def to_float(value: Any) -> float:
    try:
        return float(value) if value is not None else 0.0
    except (TypeError, ValueError):
        return 0.0


if __name__ == "__main__":
    main()
