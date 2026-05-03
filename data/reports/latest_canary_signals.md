# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T15:30:23.290083+00:00`
- Correlation status: `ready`
- Asset price records: `181`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0452` n `7`; crypto_alt avg `0.0477` n `223`; crypto_major avg `0.0656` n `7`; equity avg `-0.0472` n `42`; fx avg `-0.0003` n `4`; index avg `-0.0007` n `9`; metal avg `0.0142` n `7`; unknown avg `0.1602` n `313`
- 1h: commodity avg `-0.1831` n `7`; crypto_alt avg `0.2077` n `223`; crypto_major avg `0.0708` n `7`; equity avg `-0.0427` n `42`; fx avg `0.0006` n `4`; index avg `-0.0027` n `9`; metal avg `0.0341` n `7`; unknown avg `0.2249` n `313`
- 4h: commodity avg `-0.2293` n `7`; crypto_alt avg `0.3529` n `223`; crypto_major avg `0.4623` n `7`; equity avg `0.0247` n `42`; fx avg `0.0094` n `4`; index avg `-0.0546` n `9`; metal avg `0.0934` n `7`; unknown avg `0.1684` n `313`
- 24h: commodity avg `-0.4701` n `7`; crypto_alt avg `0.3638` n `223`; crypto_major avg `0.185` n `7`; equity avg `0.3642` n `42`; fx avg `0.1286` n `4`; index avg `0.0255` n `9`; metal avg `0.2457` n `7`; unknown avg `0.129` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4026`, n `177`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3849`, n `177`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3811`, n `177`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3791`, n `173`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3742`, n `173`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3674`, n `177`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3278`, n `173`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.321`, n `177`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.318`, n `173`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3046`, n `177`, moderate_sample_signal
