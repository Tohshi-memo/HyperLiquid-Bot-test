# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T09:52:50.710982+00:00`
- Correlation status: `ready`
- Asset price records: `158`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `7`; crypto_alt avg `0.1527` n `223`; crypto_major avg `0.0921` n `7`; equity avg `0.0071` n `42`; fx avg `0.0` n `4`; index avg `0.0003` n `9`; metal avg `0.0105` n `7`; unknown avg `-0.0142` n `313`
- 1h: commodity avg `-0.0242` n `7`; crypto_alt avg `0.107` n `223`; crypto_major avg `0.2367` n `7`; equity avg `0.0902` n `42`; fx avg `0.0005` n `4`; index avg `-0.0282` n `9`; metal avg `0.0251` n `7`; unknown avg `-0.0493` n `313`
- 4h: commodity avg `-0.0691` n `7`; crypto_alt avg `0.6147` n `223`; crypto_major avg `0.4411` n `7`; equity avg `-0.1861` n `42`; fx avg `0.0151` n `4`; index avg `0.01` n `9`; metal avg `0.1271` n `7`; unknown avg `0.0163` n `311`
- 24h: commodity avg `-0.2257` n `7`; crypto_alt avg `1.0993` n `223`; crypto_major avg `-0.0168` n `7`; equity avg `0.2633` n `42`; fx avg `0.1343` n `4`; index avg `0.0599` n `9`; metal avg `0.1184` n `7`; unknown avg `0.1158` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4167`, n `154`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `154`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.402`, n `154`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3899`, n `150`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `154`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3847`, n `150`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3749`, n `150`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3674`, n `150`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.334`, n `154`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3274`, n `154`, moderate_sample_signal
