# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-07T04:52:30.202798+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `12`; crypto_alt avg `0.0111` n `232`; crypto_major avg `0.0516` n `8`; equity avg `0.023` n `134`; fx avg `-0.0162` n `6`; index avg `0.0087` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.2947` n `794`
- 1h: commodity avg `0.0333` n `12`; crypto_alt avg `0.0058` n `232`; crypto_major avg `-0.0064` n `8`; equity avg `0.1121` n `134`; fx avg `-0.0007` n `6`; index avg `0.0205` n `26`; metal avg `-0.048` n `20`; unknown avg `0.0686` n `786`
- 4h: commodity avg `0.1077` n `12`; crypto_alt avg `-1.0736` n `232`; crypto_major avg `-0.9611` n `8`; equity avg `0.1994` n `134`; fx avg `0.1133` n `6`; index avg `0.011` n `26`; metal avg `-0.1849` n `20`; unknown avg `2.3143` n `758`
- 24h: commodity avg `0.1006` n `12`; crypto_alt avg `-0.0679` n `232`; crypto_major avg `-0.7461` n `8`; equity avg `0.4813` n `134`; fx avg `0.0283` n `6`; index avg `0.0197` n `26`; metal avg `-0.2279` n `20`; unknown avg `73.2172` n `658`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1929`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
