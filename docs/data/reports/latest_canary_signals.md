# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T03:00:39.534598+00:00`
- Correlation status: `ready`
- Asset price records: `131`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0181` n `7`; crypto_alt avg `-0.0115` n `223`; crypto_major avg `0.0473` n `7`; equity avg `0.011` n `42`; fx avg `-0.0008` n `4`; index avg `-0.0106` n `9`; metal avg `0.0064` n `7`; unknown avg `-0.021` n `313`
- 1h: commodity avg `-0.0503` n `7`; crypto_alt avg `-0.258` n `223`; crypto_major avg `-0.0807` n `7`; equity avg `-0.0243` n `42`; fx avg `0.0104` n `4`; index avg `-0.0229` n `9`; metal avg `0.0154` n `7`; unknown avg `-0.0352` n `313`
- 4h: commodity avg `-0.0189` n `7`; crypto_alt avg `-1.1711` n `223`; crypto_major avg `-0.7235` n `7`; equity avg `-0.0876` n `42`; fx avg `0.0029` n `4`; index avg `-0.0214` n `9`; metal avg `0.0124` n `7`; unknown avg `0.0152` n `313`
- 24h: commodity avg `-0.1874` n `7`; crypto_alt avg `0.7709` n `223`; crypto_major avg `-0.347` n `7`; equity avg `0.55` n `42`; fx avg `0.003` n `4`; index avg `0.0041` n `9`; metal avg `0.0305` n `7`; unknown avg `0.1224` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4499`, n `127`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.4353`, n `127`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4347`, n `127`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.4254`, n `127`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.4249`, n `127`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4136`, n `123`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4111`, n `123`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4052`, n `123`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.404`, n `127`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4002`, n `123`, moderate_sample_signal
