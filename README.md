# Public Crypto Context Feed

Public data collector for the private HyperLiquid swing trader.

This repository gathers public market-context data only. It does not contain
exchange keys, position state, final trade signals, or execution logic.

## What It Collects

- Crypto RSS headlines
- GDELT news context counts
- Polymarket public market probabilities
- Lightweight sentiment and risk scores
- Aggregate large-flow alert data for unusual Polymarket-related attention
- Lightweight all-symbol HyperLiquid price snapshots
- HIP-3 builder-deployed perp snapshots, including `xyz` stock, index, metal,
  commodity, and FX markets
- Day/swing research snapshots for BTC, ETH, HYPE, and SOL
- Compact AI context index and canary signals for quota-saving analysis

Outputs are written to:

```text
data/processed/ai_context_index.json
data/processed/canary_signals.json
data/processed/market_context.json
data/processed/market_context_history.json
data/processed/flow_alert.json
data/processed/flow_alert_history.json
data/processed/asset_universe_latest.json
data/processed/asset_price_history.json
data/processed/day_swing_dataset.json
data/processed/ai_analysis_pack.json
data/reports/latest_context.md
data/reports/latest_flow_alert.md
data/reports/latest_ai_context_index.md
data/reports/latest_canary_signals.md
data/reports/latest_asset_universe.md
data/reports/latest_day_swing.md
data/reports/latest_ai_analysis_brief.md
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

`asset_price_history.json` stores lightweight all-symbol HyperLiquid prices from
`metaAndAssetCtxs`/`allMids`. By default it also includes HIP-3
builder-deployed perps from `ASSET_UNIVERSE_HIP3_DEXS=xyz`, such as
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

## Run Locally

```bash
pip install -r requirements.txt
python -m collector.collect_context
COLLECTOR_PROFILE=flow_alert python -m collector.collect_context
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
