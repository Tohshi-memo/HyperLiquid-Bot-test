# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T21:45:26.787364+00:00`
- Correlation status: `ready`
- Asset price records: `206`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1593` n `7`; crypto_alt avg `-0.3397` n `223`; crypto_major avg `-0.3625` n `7`; equity avg `-0.0415` n `42`; fx avg `-0.0011` n `4`; index avg `0.0194` n `9`; metal avg `-0.023` n `7`; unknown avg `-0.008` n `314`
- 1h: commodity avg `-0.2165` n `7`; crypto_alt avg `-0.6366` n `223`; crypto_major avg `-0.6057` n `7`; equity avg `0.0788` n `42`; fx avg `-0.0353` n `4`; index avg `0.0218` n `9`; metal avg `0.1311` n `7`; unknown avg `-0.0884` n `314`
- 4h: commodity avg `-0.2709` n `7`; crypto_alt avg `-0.2401` n `223`; crypto_major avg `-0.3677` n `7`; equity avg `0.1446` n `42`; fx avg `-0.051` n `4`; index avg `0.0576` n `9`; metal avg `0.1276` n `7`; unknown avg `-0.1211` n `314`
- 24h: commodity avg `-0.6186` n `7`; crypto_alt avg `-0.9908` n `223`; crypto_major avg `-0.5875` n `7`; equity avg `0.2508` n `42`; fx avg `-0.0096` n `4`; index avg `0.1233` n `9`; metal avg `0.5892` n `7`; unknown avg `-0.2148` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3951`, n `202`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3939`, n `198`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3871`, n `198`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3773`, n `202`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3608`, n `202`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.348`, n `202`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3018`, n `202`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2918`, n `202`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.2822`, n `202`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.2443`, n `198`, weak_sample_signal
