# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T16:00:25.484718+00:00`
- Correlation status: `ready`
- Asset price records: `183`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.068` n `7`; crypto_alt avg `0.043` n `223`; crypto_major avg `-0.0186` n `7`; equity avg `0.0039` n `42`; fx avg `0.0005` n `4`; index avg `0.0047` n `9`; metal avg `0.0485` n `7`; unknown avg `0.0915` n `313`
- 1h: commodity avg `-0.0037` n `7`; crypto_alt avg `-0.1214` n `223`; crypto_major avg `-0.1861` n `7`; equity avg `0.0206` n `42`; fx avg `0.0072` n `4`; index avg `0.0377` n `9`; metal avg `0.0657` n `7`; unknown avg `0.1042` n `313`
- 4h: commodity avg `-0.3574` n `7`; crypto_alt avg `-0.0098` n `223`; crypto_major avg `-0.026` n `7`; equity avg `0.0505` n `42`; fx avg `0.0152` n `4`; index avg `0.0148` n `9`; metal avg `0.1286` n `7`; unknown avg `-0.3919` n `313`
- 24h: commodity avg `-0.5672` n `7`; crypto_alt avg `-0.0508` n `223`; crypto_major avg `-0.0732` n `7`; equity avg `0.3738` n `42`; fx avg `0.1163` n `4`; index avg `0.0482` n `9`; metal avg `0.2991` n `7`; unknown avg `-0.2025` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4024`, n `179`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3846`, n `179`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3811`, n `179`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3804`, n `175`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3755`, n `175`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3674`, n `179`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3239`, n `175`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3238`, n `179`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3131`, n `175`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3065`, n `179`, moderate_sample_signal
