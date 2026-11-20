# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T06:07:33.382176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0577` n `13`; crypto_alt avg `-0.0644` n `239`; crypto_major avg `-0.1543` n `8`; equity avg `-0.0378` n `165`; fx avg `0.004` n `6`; index avg `-0.0068` n `27`; metal avg `0.138` n `20`; unknown avg `-0.0316` n `1236`
- 1h: commodity avg `-0.14` n `13`; crypto_alt avg `0.8729` n `239`; crypto_major avg `0.8002` n `8`; equity avg `0.173` n `165`; fx avg `0.0215` n `6`; index avg `0.0089` n `27`; metal avg `0.3479` n `20`; unknown avg `0.3361` n `1238`
- 4h: commodity avg `-0.1295` n `13`; crypto_alt avg `0.1662` n `239`; crypto_major avg `0.7104` n `8`; equity avg `-0.2258` n `165`; fx avg `0.0154` n `6`; index avg `-0.0234` n `27`; metal avg `0.1445` n `20`; unknown avg `163.5354` n `1224`
- 24h: commodity avg `-0.2323` n `13`; crypto_alt avg `-2.7189` n `239`; crypto_major avg `-2.32` n `8`; equity avg `-6.2126` n `165`; fx avg `0.0272` n `6`; index avg `-0.5604` n `27`; metal avg `-1.5654` n `20`; unknown avg `253.8184` n `1169`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0791`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
