# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T15:15:36.846443+00:00`
- Correlation status: `ready`
- Asset price records: `180`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1499` n `7`; crypto_alt avg `0.0331` n `223`; crypto_major avg `-0.0678` n `7`; equity avg `0.0151` n `42`; fx avg `0.0093` n `4`; index avg `-0.0032` n `9`; metal avg `0.0077` n `7`; unknown avg `0.1293` n `313`
- 1h: commodity avg `-0.1288` n `7`; crypto_alt avg `0.0683` n `223`; crypto_major avg `-0.0044` n `7`; equity avg `0.0873` n `42`; fx avg `0.004` n `4`; index avg `-0.0061` n `9`; metal avg `0.034` n `7`; unknown avg `0.0575` n `313`
- 4h: commodity avg `-0.2071` n `7`; crypto_alt avg `0.25` n `223`; crypto_major avg `0.3733` n `7`; equity avg `0.0526` n `42`; fx avg `0.012` n `4`; index avg `0.012` n `9`; metal avg `0.1` n `7`; unknown avg `0.0077` n `313`
- 24h: commodity avg `-0.4267` n `7`; crypto_alt avg `0.3421` n `223`; crypto_major avg `0.1322` n `7`; equity avg `0.4164` n `42`; fx avg `0.1296` n `4`; index avg `0.0215` n `9`; metal avg `0.2329` n `7`; unknown avg `-0.0124` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4027`, n `176`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.385`, n `176`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3815`, n `176`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3791`, n `172`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3742`, n `172`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3678`, n `176`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3324`, n `172`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.323`, n `176`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3209`, n `172`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3061`, n `176`, moderate_sample_signal
