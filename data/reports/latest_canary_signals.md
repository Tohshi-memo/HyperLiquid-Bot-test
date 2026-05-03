# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T15:00:27.149119+00:00`
- Correlation status: `ready`
- Asset price records: `179`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3063` n `7`; crypto_alt avg `0.0971` n `223`; crypto_major avg `0.0882` n `7`; equity avg `-0.0179` n `42`; fx avg `-0.0032` n `4`; index avg `0.0012` n `9`; metal avg `0.0112` n `7`; unknown avg `0.034` n `313`
- 1h: commodity avg `-0.2819` n `7`; crypto_alt avg `0.1538` n `223`; crypto_major avg `0.1856` n `7`; equity avg `0.0358` n `42`; fx avg `-0.0106` n `4`; index avg `-0.0034` n `9`; metal avg `0.0476` n `7`; unknown avg `-0.0221` n `313`
- 4h: commodity avg `-0.3646` n `7`; crypto_alt avg `0.3968` n `223`; crypto_major avg `0.5685` n `7`; equity avg `0.0532` n `42`; fx avg `0.0056` n `4`; index avg `0.019` n `9`; metal avg `0.0914` n `7`; unknown avg `-0.1054` n `313`
- 24h: commodity avg `-0.5777` n `7`; crypto_alt avg `0.378` n `223`; crypto_major avg `0.2319` n `7`; equity avg `0.4284` n `42`; fx avg `0.1235` n `4`; index avg `0.0232` n `9`; metal avg `0.2348` n `7`; unknown avg `-0.1414` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4028`, n `175`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.385`, n `175`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3814`, n `175`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3791`, n `171`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3742`, n `171`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3677`, n `175`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3344`, n `171`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3238`, n `171`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3229`, n `175`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.306`, n `175`, moderate_sample_signal
