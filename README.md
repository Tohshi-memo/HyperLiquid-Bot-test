# Public Crypto Context Feed

Public data collector for the private HyperLiquid swing trader.

This repository gathers public market-context data only. It does not contain
exchange keys, position state, final trade signals, or execution logic.

## What It Collects

- Crypto, macro, policy, and commodity RSS headlines
- GDELT crypto and macro news context counts
- Macro indicators from BLS and U.S. Treasury, with optional FRED support
- Polymarket public market probabilities
- Lightweight sentiment and risk scores
- Aggregate large-flow alert data for unusual Polymarket-related attention
- Lightweight all-symbol HyperLiquid price snapshots
- HIP-3 builder-deployed perp snapshots, including `xyz` stock, index, metal,
  commodity, and FX markets
- HIP-4 outcome (prediction) market snapshots: per-outcome implied
  probability, mark/mid prices, 24h volume, and open interest, with a 15m
  history bucket aggregated from the HyperLiquid `outcomeMeta` /
  `allMids` info-endpoint requests, plus asset-context fields when available
- Day/swing research snapshots for BTC, ETH, HYPE, and SOL
- Compact AI context index and canary signals for quota-saving analysis
- Mechanical relationship scans for A/B conditions versus future asset-class returns
- Sector reaction history for event conditions versus delayed sector ETF proxy returns
- Compact individual-asset feature screens for stock, index, metal, commodity,
  FX, and crypto candidates

Outputs are written to:

```text
data/processed/ai_context_index.json
data/processed/canary_signals.json
data/processed/market_context.json
data/processed/market_context_history.json
data/processed/polymarket_outcome_latest.json
data/processed/polymarket_outcome_history.json
data/processed/flow_alert.json
data/processed/flow_alert_history.json
data/processed/macro_indicators_latest.json
data/processed/macro_indicators_history.json
data/processed/asset_universe_latest.json
data/processed/asset_price_history.json
data/processed/asset_features_latest.json
data/processed/day_swing_dataset.json
data/processed/ai_analysis_pack.json
data/processed/hip4_outcome_latest.json
data/processed/hip4_outcome_history.json
data/processed/relationship_scan_latest.json
data/processed/sector_price_history.json
data/processed/sector_reactions_latest.json
data/reports/latest_context.md
data/reports/latest_flow_alert.md
data/reports/latest_macro_indicators.md
data/reports/latest_ai_context_index.md
data/reports/latest_canary_signals.md
data/reports/latest_asset_universe.md
data/reports/latest_asset_features.md
data/reports/latest_day_swing.md
data/reports/latest_ai_analysis_brief.md
data/reports/latest_hip4_outcome.md
data/reports/latest_relationship_scan.md
data/reports/latest_sector_reactions.md
data/archive/asset_price_history_YYYY-MM.jsonl.gz
```

The private repository reads `market_context.json` and makes the final trading
decision privately.

`day_swing_dataset.json` stores compact public research rows: context scores,
15m/1h/4h technical features, and later 1h/4h/24h/72h forward-return labels.
It is for manual AI analysis and strategy research, not direct trade execution.

AI should read `latest_ai_context_index.md`, `ai_context_index.json`,
`latest_canary_signals.md`, `latest_ai_analysis_brief.md`, and
`ai_analysis_pack.json` first. Full JSON files should be loaded only for deeper
validation of a specific candidate rule.

`macro_indicators_latest.json` stores public macro data that can affect
day-to-swing trades: U.S. employment, CPI/core CPI, PPI, and U.S. Treasury
average interest-rate data are collected without an API key. If `FRED_API_KEY`
is configured, the same file also adds U.S. 2Y/10Y yields, 10Y-2Y spread,
Fed Funds, SOFR, broad dollar index, VIX, PCE/core PCE, and selected non-U.S.
10Y yield and unemployment series for Germany, Japan, the United Kingdom,
Canada, and the euro area where available. History is kept in
`macro_indicators_history.json` for lead/lag checks against token, stock-token,
commodity-token, and metal-token moves.

`asset_price_history.json` stores lightweight all-symbol HyperLiquid prices from
`metaAndAssetCtxs`/`allMids`. By default it also includes HIP-3
builder-deployed perps from `ASSET_UNIVERSE_HIP3_DEXS=all`, such as
`xyz:AAPL`, `xyz:TSLA`, `xyz:NVDA`, `xyz:GOLD`, and `xyz:SP500`. It is the
HyperLiquid equivalent of the MEXC scanner's compact market-context record:
broad coverage first, deeper OHLCV features only for selected research symbols.

To avoid making AI read huge files, the active all-symbol price history keeps a
recent analysis window in `asset_price_history.json`. Older rows are preserved as
compressed JSONL archives under `data/archive/`. The compact index points to
archives only when a longer backtest is needed.

`canary_signals.json` precomputes small cross-market checks: news-risk,
Polymarket volume, large-flow aggregates, and asset-class returns for crypto,
equity, index, metal, commodity, and FX perps. These are early-warning research
signals, not direct trade instructions.

`asset_features_latest.json` is the first stop for individual-symbol review. It
keeps a compact screen of recent 15m/1h/4h/24h returns, volume, open interest,
funding, class, and best mechanical relationship candidate. Use this before
loading the heavier all-symbol price history.

Polymarket collection discovers active markets, then keeps watchlist-relevant
ones by text/tag classification: crypto, major macro, commodities, rates,
geopolitical, military/conflict, election, and tariff-related markets. The
5-minute flow job uses a narrower high-impact subset; the 15-minute context
job keeps the broader research set.

`polymarket_outcome_latest.json` stores the latest per-outcome probability rows
for the report site. `polymarket_outcome_history.json` stores the rolling
15-minute context history with `event_slug`, market slug, token ID, outcome
name, probability, liquidity, volume, and a best-effort `subject_name` /
`person_name` parsed from questions such as "Will X win..." so candidate and
person probabilities can be tracked even when the market itself is Yes/No.
Configured event slugs, such as the 2028 Democratic nominee, Republican
nominee, and presidential winner events, are fetched by event so lower-volume
candidates are retained in history even when they are outside the normal top
market limit. The report site shows a searchable, filtered people view instead
of rendering every candidate by default. The active history is capped so normal
GitHub commits stay below the 100MB file limit; older full-depth analysis should
use archived or private storage if needed.

`relationship_scan_latest.json` mechanically compares public conditions such
as news risk, macro risk, risk-on context, Polymarket volume spikes, and flow
alerts against future 1h/4h/24h asset-class returns and selected individual
symbols. It records sample count, baseline probability, conditional
probability, expected return edge, drawdown, loss streak, and split-period
stability. It is a hypothesis generator only; private AI review and private
strategy code must validate any candidate before trade use.

`sector_price_history.json` and `sector_reactions_latest.json` track delayed
sector reactions using no-key daily ETF proxy data by default. The default
provider is Yahoo's chart endpoint, and Stooq CSV can be used when
`STOOQ_API_KEY` is configured. Sector proxies include XLK, SMH, XLF, XLE, XLV,
XLI, XLY, XLP, XLU, XLB, XLRE, XLC,
IWM, IYR, XHB, SPY, and QQQ. The reaction dataset stores event-condition rows
such as news-risk spikes, Polymarket volume spikes, energy strength, defensive
rotation, and broad risk-on moves, then labels each row with 1d, 5d, 20d, 60d,
120d, and 252d forward returns. This is designed for long-horizon questions
like whether a condition from months ago tends to lead a sector later.

`hip4_outcome_latest.json` and `hip4_outcome_history.json` capture HIP-4
outcome markets directly from HyperLiquid. The collector reads market
definitions from `outcomeMeta` and fills each outcome side from the `allMids`
`#<encoding>` price keys, such as `#40` and `#41`. The computed fields include
`symbol`, `encoding`, HyperLiquid `asset_id`, `mark_price`, `mid_price`,
`implied_probability`, and `price_source`. Asset-context endpoints are tried
defensively for 24h volume and open interest, but `allMids` is enough to keep
HIP-4 probabilities usable when those context endpoints are unavailable. A
rolling 15-minute bucket history is stored for cross-market analysis alongside
Polymarket and HIP-3 perp data. Raw payloads are preserved under
`data/raw/YYYY-MM-DD/` for verification.

## Report Site

The `docs/` directory contains a static, AI-free report dashboard for GitHub
Pages. It reads copied compact JSON/Markdown from `docs/data/` and displays
market status, canary signals, data readiness, BTC/ETH/HYPE/SOL stats,
asset-class movement, macro indicators, top movers, top Polymarket markets,
latest headlines, GDELT activity, flow details, relationship candidates, HIP-4
markets, and an Asset Screener page for individual stock, commodity, metal,
index, FX, and crypto assets.

Headlines are saved with a `category` field (`crypto`, `macro`, `policy`,
or `commodity`) so later analysis can compare token prices with general market
news, central-bank policy, energy/commodity stress, and crypto-specific events
without loading every raw RSS file.

The site intentionally does not show private strategy, entries, SL/TP decisions,
wallet data, positions, or execution status.

## Run Locally

```bash
pip install -r requirements.txt
python -m collector.collect_context
COLLECTOR_PROFILE=flow_alert python -m collector.collect_context
python tools/build_report_site_data.py
```

## Schedule

GitHub Actions runs the normal context collector every 15 minutes and the
lightweight flow-alert collector every 5 minutes. Public repository Actions on
standard GitHub-hosted runners do not consume the private repository's monthly
Actions minutes.

Default retention is tuned for strategy research: normal context history keeps
up to 8,640 rows, flow-alert history keeps up to 8,640 rows, the active
all-symbol price window keeps 672 15-minute buckets, older all-symbol rows are
archived, and the day/swing dataset keeps up to 12,000 15-minute buckets.

The 5-minute flow alert writes aggregate data only. It can read the latest Dune
query result when `DUNE_API_KEY` and `DUNE_LARGE_FLOW_QUERY_ID` are configured,
but it does not trigger a Dune query execution by itself.
