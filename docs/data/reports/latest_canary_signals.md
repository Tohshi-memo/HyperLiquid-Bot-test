# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T21:15:21.225235+00:00`
- Correlation status: `ready`
- Asset price records: `204`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `7`; crypto_alt avg `0.1236` n `223`; crypto_major avg `0.1315` n `7`; equity avg `0.0637` n `42`; fx avg `-0.0064` n `4`; index avg `0.0146` n `9`; metal avg `0.1117` n `7`; unknown avg `0.1515` n `314`
- 1h: commodity avg `-0.5876` n `7`; crypto_alt avg `-0.0036` n `223`; crypto_major avg `0.0669` n `7`; equity avg `0.1037` n `42`; fx avg `-0.0372` n `4`; index avg `0.0503` n `9`; metal avg `0.1725` n `7`; unknown avg `-0.0479` n `314`
- 4h: commodity avg `-0.2816` n `7`; crypto_alt avg `0.4689` n `223`; crypto_major avg `0.3181` n `7`; equity avg `0.2355` n `42`; fx avg `-0.0301` n `4`; index avg `0.0639` n `9`; metal avg `0.1891` n `7`; unknown avg `-0.0409` n `314`
- 24h: commodity avg `-0.6491` n `7`; crypto_alt avg `-0.056` n `223`; crypto_major avg `0.3518` n `7`; equity avg `0.2413` n `42`; fx avg `0.0302` n `4`; index avg `0.1019` n `9`; metal avg `0.6095` n `7`; unknown avg `-0.0442` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3975`, n `200`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.39`, n `196`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3833`, n `196`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3797`, n `200`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3686`, n `200`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3557`, n `200`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3347`, n `200`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3162`, n `200`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3063`, n `200`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2466`, n `196`, weak_sample_signal
