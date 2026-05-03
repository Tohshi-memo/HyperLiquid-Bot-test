# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T16:30:22.231015+00:00`
- Correlation status: `ready`
- Asset price records: `185`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0054` n `7`; crypto_alt avg `0.0689` n `223`; crypto_major avg `0.0358` n `7`; equity avg `0.0021` n `42`; fx avg `-0.0011` n `4`; index avg `0.0082` n `9`; metal avg `0.0026` n `7`; unknown avg `0.0052` n `313`
- 1h: commodity avg `-0.1958` n `7`; crypto_alt avg `-0.1668` n `223`; crypto_major avg `-0.0972` n `7`; equity avg `0.1459` n `42`; fx avg `0.0029` n `4`; index avg `0.0526` n `9`; metal avg `0.0659` n `7`; unknown avg `-0.1098` n `313`
- 4h: commodity avg `-0.4317` n `7`; crypto_alt avg `-0.2566` n `223`; crypto_major avg `-0.1644` n `7`; equity avg `0.1279` n `42`; fx avg `0.0144` n `4`; index avg `0.0624` n `9`; metal avg `0.1246` n `7`; unknown avg `-0.1205` n `313`
- 24h: commodity avg `-0.6468` n `7`; crypto_alt avg `-0.1101` n `223`; crypto_major avg `-0.0501` n `7`; equity avg `0.4832` n `42`; fx avg `0.1184` n `4`; index avg `0.0993` n `9`; metal avg `0.3018` n `7`; unknown avg `-0.032` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4018`, n `181`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3841`, n `181`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3812`, n `177`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3808`, n `181`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3754`, n `177`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3671`, n `181`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3251`, n `181`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3199`, n `177`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3077`, n `177`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3068`, n `181`, moderate_sample_signal
