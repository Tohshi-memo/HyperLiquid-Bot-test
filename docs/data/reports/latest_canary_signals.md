# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T21:24:46.281460+00:00`
- Correlation status: `ready`
- Asset price records: `204`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `7`; crypto_alt avg `-0.0478` n `223`; crypto_major avg `-0.0148` n `7`; equity avg `0.1025` n `42`; fx avg `-0.0308` n `4`; index avg `0.0041` n `9`; metal avg `0.1032` n `7`; unknown avg `0.1471` n `314`
- 1h: commodity avg `-0.5598` n `7`; crypto_alt avg `-0.1747` n `223`; crypto_major avg `-0.0793` n `7`; equity avg `0.1427` n `42`; fx avg `-0.0616` n `4`; index avg `0.0398` n `9`; metal avg `0.164` n `7`; unknown avg `-0.0529` n `314`
- 4h: commodity avg `-0.2533` n `7`; crypto_alt avg `0.2955` n `223`; crypto_major avg `0.1713` n `7`; equity avg `0.2744` n `42`; fx avg `-0.0545` n `4`; index avg `0.0534` n `9`; metal avg `0.1806` n `7`; unknown avg `-0.0475` n `314`
- 24h: commodity avg `-0.6216` n `7`; crypto_alt avg `-0.2294` n `223`; crypto_major avg `0.2053` n `7`; equity avg `0.2802` n `42`; fx avg `0.0058` n `4`; index avg `0.0913` n `9`; metal avg `0.6009` n `7`; unknown avg `-0.0502` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3976`, n `200`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.389`, n `196`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3822`, n `196`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3798`, n `200`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.369`, n `200`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3561`, n `200`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.331`, n `200`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3118`, n `200`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3052`, n `200`, moderate_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.2448`, n `200`, weak_sample_signal
