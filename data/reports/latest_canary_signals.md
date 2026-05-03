# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T18:30:24.218402+00:00`
- Correlation status: `ready`
- Asset price records: `193`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0797` n `7`; crypto_alt avg `0.1228` n `223`; crypto_major avg `0.1244` n `7`; equity avg `0.028` n `42`; fx avg `-0.0358` n `4`; index avg `0.0045` n `9`; metal avg `0.0858` n `7`; unknown avg `-0.0504` n `314`
- 1h: commodity avg `0.4188` n `7`; crypto_alt avg `0.0575` n `223`; crypto_major avg `0.0073` n `7`; equity avg `0.0019` n `42`; fx avg `-0.0512` n `4`; index avg `-0.0391` n `9`; metal avg `0.1316` n `7`; unknown avg `-0.097` n `314`
- 4h: commodity avg `0.0359` n `7`; crypto_alt avg `0.2024` n `223`; crypto_major avg `0.0331` n `7`; equity avg `0.1892` n `42`; fx avg `-0.0572` n `4`; index avg `0.0674` n `9`; metal avg `0.3293` n `7`; unknown avg `0.216` n `313`
- 24h: commodity avg `-0.0984` n `7`; crypto_alt avg `-0.056` n `223`; crypto_major avg `0.0678` n `7`; equity avg `0.3872` n `42`; fx avg `0.024` n `4`; index avg `0.0567` n `9`; metal avg `0.5774` n `7`; unknown avg `0.0166` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3984`, n `189`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3805`, n `189`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3803`, n `185`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3768`, n `189`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3731`, n `185`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3634`, n `189`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3264`, n `189`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3073`, n `189`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3045`, n `189`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2662`, n `185`, moderate_sample_signal
