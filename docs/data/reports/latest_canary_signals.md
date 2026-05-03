# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T10:30:24.137635+00:00`
- Correlation status: `ready`
- Asset price records: `161`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0277` n `7`; crypto_alt avg `-0.0402` n `223`; crypto_major avg `-0.0045` n `7`; equity avg `0.0553` n `42`; fx avg `0.004` n `4`; index avg `0.0272` n `9`; metal avg `0.0087` n `7`; unknown avg `-0.0218` n `313`
- 1h: commodity avg `-0.0489` n `7`; crypto_alt avg `0.1646` n `223`; crypto_major avg `-0.064` n `7`; equity avg `0.0203` n `42`; fx avg `0.004` n `4`; index avg `0.0275` n `9`; metal avg `0.0203` n `7`; unknown avg `-0.0507` n `313`
- 4h: commodity avg `-0.0385` n `7`; crypto_alt avg `0.5607` n `223`; crypto_major avg `0.3994` n `7`; equity avg `-0.0375` n `42`; fx avg `0.0196` n `4`; index avg `0.0171` n `9`; metal avg `0.1204` n `7`; unknown avg `0.1408` n `313`
- 24h: commodity avg `-0.2547` n `7`; crypto_alt avg `1.2066` n `223`; crypto_major avg `0.0087` n `7`; equity avg `0.2117` n `42`; fx avg `0.1305` n `4`; index avg `0.091` n `9`; metal avg `0.1191` n `7`; unknown avg `0.1761` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4152`, n `157`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `157`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4005`, n `157`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `157`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3844`, n `153`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3796`, n `153`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3694`, n `153`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3623`, n `153`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3401`, n `157`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.333`, n `157`, moderate_sample_signal
