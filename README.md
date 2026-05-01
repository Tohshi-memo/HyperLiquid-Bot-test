# Public Crypto Context Feed

Public data collector for the private HyperLiquid swing trader.

This repository gathers public market-context data only. It does not contain
exchange keys, position state, final trade signals, or execution logic.

## What It Collects

- Crypto RSS headlines
- GDELT news context counts
- Polymarket public market probabilities
- Lightweight sentiment and risk scores

Outputs are written to:

```text
data/processed/market_context.json
data/processed/market_context_history.json
data/reports/latest_context.md
```

The private repository reads `market_context.json` and makes the final trading
decision privately.

## Run Locally

```bash
pip install -r requirements.txt
python -m collector.collect_context
```

## Schedule

GitHub Actions runs every two hours. Public repository Actions on standard
GitHub-hosted runners do not consume the private repository's monthly Actions
minutes.
