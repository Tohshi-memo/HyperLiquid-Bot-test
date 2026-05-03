# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T15:45:26.734482+00:00`
- Correlation status: `ready`
- Asset price records: `182`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0468` n `7`; crypto_alt avg `-0.1772` n `223`; crypto_major avg `-0.0778` n `7`; equity avg `0.0281` n `42`; fx avg `0.0` n `4`; index avg `0.0021` n `9`; metal avg `0.0078` n `7`; unknown avg `-0.1162` n `313`
- 1h: commodity avg `-0.2428` n `7`; crypto_alt avg `-0.0704` n `223`; crypto_major avg `-0.0795` n `7`; equity avg `-0.0011` n `42`; fx avg `0.0035` n `4`; index avg `0.0342` n `9`; metal avg `0.0284` n `7`; unknown avg `0.1816` n `313`
- 4h: commodity avg `-0.29` n `7`; crypto_alt avg `-0.0518` n `223`; crypto_major avg `0.0429` n `7`; equity avg `0.0577` n `42`; fx avg `0.0136` n `4`; index avg `0.0101` n `9`; metal avg `0.1075` n `7`; unknown avg `-0.2245` n `313`
- 24h: commodity avg `-0.5078` n `7`; crypto_alt avg `-0.001` n `223`; crypto_major avg `0.0005` n `7`; equity avg `0.3969` n `42`; fx avg `0.1158` n `4`; index avg `0.0537` n `9`; metal avg `0.247` n `7`; unknown avg `0.0227` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4026`, n `178`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3849`, n `178`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3816`, n `178`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3797`, n `174`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.375`, n `174`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3679`, n `178`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3241`, n `174`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3228`, n `178`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3133`, n `174`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3059`, n `178`, moderate_sample_signal
