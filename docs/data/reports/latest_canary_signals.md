# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-04T06:11:11.054722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0301` n `12`; crypto_alt avg `0.2164` n `232`; crypto_major avg `0.3026` n `8`; equity avg `0.0601` n `133`; fx avg `-0.0221` n `6`; index avg `-0.0009` n `26`; metal avg `0.0327` n `20`; unknown avg `0.0739` n `757`
- 1h: commodity avg `-0.0184` n `12`; crypto_alt avg `-0.3362` n `232`; crypto_major avg `-0.1238` n `8`; equity avg `-0.0609` n `133`; fx avg `-0.036` n `6`; index avg `0.0047` n `26`; metal avg `-0.0164` n `20`; unknown avg `1.3381` n `757`
- 4h: commodity avg `-0.0816` n `12`; crypto_alt avg `-0.4057` n `232`; crypto_major avg `0.1324` n `8`; equity avg `0.2329` n `133`; fx avg `-0.04` n `6`; index avg `0.0849` n `26`; metal avg `-0.1044` n `20`; unknown avg `1.1668` n `757`
- 24h: commodity avg `-0.0081` n `12`; crypto_alt avg `1.9879` n `232`; crypto_major avg `4.1036` n `8`; equity avg `1.8152` n `133`; fx avg `-0.0897` n `6`; index avg `0.3052` n `26`; metal avg `0.4311` n `20`; unknown avg `2.4938` n `730`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.082`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0686`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
