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
- Day/swing research snapshots for BTC, ETH, HYPE, and SOL

Outputs are written to:

```text
data/processed/market_context.json
data/processed/market_context_history.json
data/processed/flow_alert.json
data/processed/flow_alert_history.json
data/processed/day_swing_dataset.json
data/reports/latest_context.md
data/reports/latest_flow_alert.md
data/reports/latest_day_swing.md
```

The private repository reads `market_context.json` and makes the final trading
decision privately.

`day_swing_dataset.json` stores compact public research rows: context scores,
15m/1h/4h technical features, and later 1h/4h/24h/72h forward-return labels.
It is for manual AI analysis and strategy research, not direct trade execution.

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
up to 8,640 rows, flow-alert history keeps up to 8,640 rows, and the day/swing
dataset keeps up to 12,000 15-minute buckets.

The 5-minute flow alert writes aggregate data only. It can read the latest Dune
query result when `DUNE_API_KEY` and `DUNE_LARGE_FLOW_QUERY_ID` are configured,
but it does not trigger a Dune query execution by itself.
