# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T02:15:37.154079+00:00`
- Correlation status: `ready`
- Asset price records: `224`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `7`; crypto_alt avg `0.0689` n `223`; crypto_major avg `0.0666` n `7`; equity avg `0.1312` n `42`; fx avg `0.0149` n `4`; index avg `0.0193` n `9`; metal avg `-0.1592` n `7`; unknown avg `-0.0739` n `314`
- 1h: commodity avg `-0.0048` n `7`; crypto_alt avg `1.1509` n `223`; crypto_major avg `1.6623` n `7`; equity avg `0.5705` n `42`; fx avg `0.0229` n `4`; index avg `0.285` n `9`; metal avg `0.2504` n `7`; unknown avg `0.1555` n `314`
- 4h: commodity avg `0.2598` n `7`; crypto_alt avg `0.547` n `223`; crypto_major avg `0.9169` n `7`; equity avg `0.5961` n `42`; fx avg `0.0329` n `4`; index avg `0.4477` n `9`; metal avg `-0.1062` n `7`; unknown avg `0.08` n `314`
- 24h: commodity avg `0.0373` n `7`; crypto_alt avg `1.8359` n `223`; crypto_major avg `2.1584` n `7`; equity avg `0.9587` n `42`; fx avg `0.0109` n `4`; index avg `0.5327` n `9`; metal avg `0.248` n `7`; unknown avg `0.5926` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3767`, n `220`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3611`, n `220`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.356`, n `216`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3517`, n `216`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2228`, n `220`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.2154`, n `220`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2104`, n `220`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1802`, n `216`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1714`, n `220`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1651`, n `216`, weak_sample_signal
