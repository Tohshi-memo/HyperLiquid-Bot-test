# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T14:00:25.356790+00:00`
- Correlation status: `ready`
- Asset price records: `175`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.05` n `7`; crypto_alt avg `0.0042` n `223`; crypto_major avg `0.0589` n `7`; equity avg `-0.006` n `42`; fx avg `0.0` n `4`; index avg `-0.0003` n `9`; metal avg `0.0039` n `7`; unknown avg `0.0282` n `313`
- 1h: commodity avg `-0.0371` n `7`; crypto_alt avg `-0.1146` n `223`; crypto_major avg `-0.0855` n `7`; equity avg `-0.0579` n `42`; fx avg `0.0154` n `4`; index avg `-0.0371` n `9`; metal avg `-0.008` n `7`; unknown avg `-0.1118` n `313`
- 4h: commodity avg `-0.1131` n `7`; crypto_alt avg `-0.036` n `223`; crypto_major avg `0.145` n `7`; equity avg `0.1557` n `42`; fx avg `0.026` n `4`; index avg `0.0048` n `9`; metal avg `0.058` n `7`; unknown avg `-0.2712` n `313`
- 24h: commodity avg `-0.3057` n `7`; crypto_alt avg `0.7688` n `223`; crypto_major avg `0.0481` n `7`; equity avg `0.2762` n `42`; fx avg `0.1802` n `4`; index avg `0.0188` n `9`; metal avg `0.1799` n `7`; unknown avg `-0.1106` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4031`, n `171`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3853`, n `171`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3845`, n `171`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3783`, n `167`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3731`, n `167`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3708`, n `171`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3579`, n `167`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3487`, n `167`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3224`, n `171`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3065`, n `171`, moderate_sample_signal
