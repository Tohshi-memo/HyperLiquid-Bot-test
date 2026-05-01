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

Outputs are written to:

```text
data/processed/market_context.json
data/processed/market_context_history.json
data/processed/flow_alert.json
data/processed/flow_alert_history.json
data/reports/latest_context.md
data/reports/latest_flow_alert.md
```

The private repository reads `market_context.json` and makes the final trading
decision privately.

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

The 5-minute flow alert writes aggregate data only. It can read the latest Dune
query result when `DUNE_API_KEY` and `DUNE_LARGE_FLOW_QUERY_ID` are configured,
but it does not trigger a Dune query execution by itself.
