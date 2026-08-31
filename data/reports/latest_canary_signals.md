# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T19:22:29.031386+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0146` n `12`; crypto_alt avg `-0.2461` n `232`; crypto_major avg `-0.1935` n `8`; equity avg `0.0434` n `129`; fx avg `-0.0037` n `6`; index avg `0.0193` n `26`; metal avg `0.0282` n `20`; unknown avg `0.4018` n `793`
- 1h: commodity avg `-0.0316` n `12`; crypto_alt avg `-0.0724` n `232`; crypto_major avg `0.0874` n `8`; equity avg `-0.0518` n `129`; fx avg `-0.0026` n `6`; index avg `-0.0249` n `26`; metal avg `0.0171` n `20`; unknown avg `0.2936` n `791`
- 4h: commodity avg `0.0164` n `12`; crypto_alt avg `0.6827` n `232`; crypto_major avg `0.9917` n `8`; equity avg `0.0796` n `129`; fx avg `-0.0141` n `6`; index avg `-0.0322` n `26`; metal avg `-0.0062` n `20`; unknown avg `-0.4574` n `791`
- 24h: commodity avg `0.3876` n `12`; crypto_alt avg `-1.1404` n `231`; crypto_major avg `-1.0577` n `8`; equity avg `-0.4869` n `129`; fx avg `-0.0954` n `6`; index avg `-0.2324` n `26`; metal avg `-0.5502` n `20`; unknown avg `0.3923` n `758`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0934`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0564`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
