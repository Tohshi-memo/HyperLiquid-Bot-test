# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T14:30:30.750641+00:00`
- Correlation status: `ready`
- Asset price records: `273`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0323` n `7`; crypto_alt avg `-0.0985` n `223`; crypto_major avg `-0.1283` n `7`; equity avg `-0.1068` n `42`; fx avg `0.0` n `4`; index avg `-0.0315` n `9`; metal avg `-0.0188` n `7`; unknown avg `-0.0502` n `314`
- 1h: commodity avg `0.0267` n `7`; crypto_alt avg `0.2681` n `223`; crypto_major avg `0.2923` n `7`; equity avg `0.4409` n `42`; fx avg `0.0139` n `4`; index avg `0.4953` n `9`; metal avg `0.4875` n `7`; unknown avg `-0.3306` n `314`
- 4h: commodity avg `-0.7842` n `7`; crypto_alt avg `0.8538` n `223`; crypto_major avg `0.7685` n `7`; equity avg `1.2157` n `42`; fx avg `0.0235` n `4`; index avg `0.7374` n `9`; metal avg `0.9172` n `7`; unknown avg `-0.1737` n `314`
- 24h: commodity avg `0.7697` n `7`; crypto_alt avg `1.4939` n `223`; crypto_major avg `0.7883` n `7`; equity avg `0.9328` n `42`; fx avg `-0.0665` n `4`; index avg `0.9873` n `9`; metal avg `-1.1141` n `7`; unknown avg `-0.3261` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2604`, n `269`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2518`, n `269`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.231`, n `265`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2285`, n `265`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1605`, n `269`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1542`, n `269`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1524`, n `269`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1523`, n `265`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1515`, n `269`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1496`, n `265`, weak_sample_signal
