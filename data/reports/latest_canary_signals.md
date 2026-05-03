# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T16:45:19.873543+00:00`
- Correlation status: `ready`
- Asset price records: `186`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `7`; crypto_alt avg `0.0045` n `223`; crypto_major avg `0.0749` n `7`; equity avg `0.0066` n `42`; fx avg `0.0035` n `4`; index avg `0.0005` n `9`; metal avg `0.0297` n `7`; unknown avg `0.1595` n `313`
- 1h: commodity avg `-0.1697` n `7`; crypto_alt avg `0.0161` n `223`; crypto_major avg `0.0555` n `7`; equity avg `0.1241` n `42`; fx avg `0.0064` n `4`; index avg `0.0511` n `9`; metal avg `0.0878` n `7`; unknown avg `0.3096` n `313`
- 4h: commodity avg `-0.4452` n `7`; crypto_alt avg `-0.2627` n `223`; crypto_major avg `-0.0894` n `7`; equity avg `0.1358` n `42`; fx avg `0.0179` n `4`; index avg `0.0202` n `9`; metal avg `0.1528` n `7`; unknown avg `0.0574` n `313`
- 24h: commodity avg `-0.6632` n `7`; crypto_alt avg `-0.1609` n `223`; crypto_major avg `0.0079` n `7`; equity avg `0.4763` n `42`; fx avg `0.1168` n `4`; index avg `0.1022` n `9`; metal avg `0.3279` n `7`; unknown avg `0.0759` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4014`, n `182`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.384`, n `178`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3836`, n `182`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3805`, n `182`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3778`, n `178`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3669`, n `182`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3252`, n `182`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3247`, n `178`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3116`, n `178`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3069`, n `182`, moderate_sample_signal
