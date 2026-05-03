# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T18:34:07.203623+00:00`
- Correlation status: `ready`
- Asset price records: `193`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1089` n `7`; crypto_alt avg `0.1179` n `223`; crypto_major avg `0.0788` n `7`; equity avg `0.0334` n `42`; fx avg `-0.0247` n `4`; index avg `0.0073` n `9`; metal avg `0.0338` n `7`; unknown avg `-0.0536` n `314`
- 1h: commodity avg `0.4483` n `7`; crypto_alt avg `0.0522` n `223`; crypto_major avg `-0.0383` n `7`; equity avg `0.0074` n `42`; fx avg `-0.0401` n `4`; index avg `-0.0362` n `9`; metal avg `0.0795` n `7`; unknown avg `-0.0998` n `314`
- 4h: commodity avg `0.065` n `7`; crypto_alt avg `0.1977` n `223`; crypto_major avg `-0.0125` n `7`; equity avg `0.1947` n `42`; fx avg `-0.0461` n `4`; index avg `0.0702` n `9`; metal avg `0.2767` n `7`; unknown avg `0.2123` n `313`
- 24h: commodity avg `-0.0694` n `7`; crypto_alt avg `-0.0618` n `223`; crypto_major avg `0.0222` n `7`; equity avg `0.3926` n `42`; fx avg `0.0351` n `4`; index avg `0.0595` n `9`; metal avg `0.5247` n `7`; unknown avg `0.0121` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3989`, n `189`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.381`, n `189`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3807`, n `185`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3769`, n `189`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3735`, n `185`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3635`, n `189`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3263`, n `189`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3072`, n `189`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3045`, n `189`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2659`, n `185`, moderate_sample_signal
