# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T10:45:39.524552+00:00`
- Correlation status: `ready`
- Asset price records: `162`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0696` n `7`; crypto_alt avg `-0.0068` n `223`; crypto_major avg `0.038` n `7`; equity avg `0.0345` n `42`; fx avg `0.0008` n `4`; index avg `0.0011` n `9`; metal avg `0.0008` n `7`; unknown avg `-0.0019` n `313`
- 1h: commodity avg `-0.1095` n `7`; crypto_alt avg `0.0121` n `223`; crypto_major avg `-0.118` n `7`; equity avg `0.0477` n `42`; fx avg `0.0048` n `4`; index avg `0.0284` n `9`; metal avg `0.0105` n `7`; unknown avg `-0.0383` n `313`
- 4h: commodity avg `-0.1049` n `7`; crypto_alt avg `0.5514` n `223`; crypto_major avg `0.4368` n `7`; equity avg `0.0073` n `42`; fx avg `0.022` n `4`; index avg `0.06` n `9`; metal avg `0.1212` n `7`; unknown avg `0.1324` n `313`
- 24h: commodity avg `-0.3183` n `7`; crypto_alt avg `1.1937` n `223`; crypto_major avg `0.0589` n `7`; equity avg `0.2658` n `42`; fx avg `0.1313` n `4`; index avg `0.0917` n `9`; metal avg `0.128` n `7`; unknown avg `0.1904` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4151`, n `158`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `158`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4004`, n `158`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `158`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3834`, n `154`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3784`, n `154`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3649`, n `154`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3576`, n `154`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3377`, n `158`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3272`, n `158`, moderate_sample_signal
