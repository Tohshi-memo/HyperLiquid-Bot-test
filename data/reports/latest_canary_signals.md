# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T22:15:17.284660+00:00`
- Correlation status: `ready`
- Asset price records: `208`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.124` n `7`; crypto_alt avg `0.4213` n `223`; crypto_major avg `0.642` n `7`; equity avg `-0.0291` n `42`; fx avg `-0.0112` n `4`; index avg `0.0484` n `9`; metal avg `0.0885` n `7`; unknown avg `-0.0501` n `314`
- 1h: commodity avg `0.1189` n `7`; crypto_alt avg `0.3334` n `223`; crypto_major avg `0.6113` n `7`; equity avg `0.011` n `42`; fx avg `-0.0149` n `4`; index avg `0.257` n `9`; metal avg `-0.1401` n `7`; unknown avg `0.1049` n `314`
- 4h: commodity avg `-0.3491` n `7`; crypto_alt avg `0.5986` n `223`; crypto_major avg `0.831` n `7`; equity avg `0.2434` n `42`; fx avg `-0.0506` n `4`; index avg `0.3325` n `9`; metal avg `-0.0371` n `7`; unknown avg `0.079` n `314`
- 24h: commodity avg `-0.4855` n `7`; crypto_alt avg `0.1231` n `223`; crypto_major avg `0.7518` n `7`; equity avg `0.2873` n `42`; fx avg `-0.0341` n `4`; index avg `0.3726` n `9`; metal avg `0.4557` n `7`; unknown avg `0.0828` n `311`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4122`, n `200`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4054`, n `200`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3943`, n `204`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3768`, n `204`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3496`, n `204`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3374`, n `204`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3021`, n `204`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2924`, n `204`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.2825`, n `204`, moderate_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.2326`, n `204`, weak_sample_signal
