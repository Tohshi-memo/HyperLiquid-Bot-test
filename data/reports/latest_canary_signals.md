# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T00:45:21.979665+00:00`
- Correlation status: `ready`
- Asset price records: `218`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1269` n `7`; crypto_alt avg `0.1351` n `223`; crypto_major avg `0.0631` n `7`; equity avg `0.0387` n `42`; fx avg `-0.0021` n `4`; index avg `-0.053` n `9`; metal avg `0.0335` n `7`; unknown avg `0.0119` n `314`
- 1h: commodity avg `-0.0146` n `7`; crypto_alt avg `-0.316` n `223`; crypto_major avg `-0.3227` n `7`; equity avg `0.1858` n `42`; fx avg `0.008` n `4`; index avg `0.2015` n `9`; metal avg `-0.1978` n `7`; unknown avg `-0.0453` n `314`
- 4h: commodity avg `0.4955` n `7`; crypto_alt avg `-0.8699` n `223`; crypto_major avg `-0.752` n `7`; equity avg `-0.1021` n `42`; fx avg `-0.0441` n `4`; index avg `0.0063` n `9`; metal avg `-0.308` n `7`; unknown avg `0.1444` n `314`
- 24h: commodity avg `0.0234` n `7`; crypto_alt avg `-0.6569` n `223`; crypto_major avg `-0.2194` n `7`; equity avg `0.1041` n `42`; fx avg `-0.021` n `4`; index avg `0.1021` n `9`; metal avg `0.1474` n `7`; unknown avg `0.2096` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3862`, n `214`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3698`, n `214`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3148`, n `210`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3138`, n `210`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2897`, n `214`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.279`, n `214`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2613`, n `210`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2561`, n `210`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.2267`, n `214`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.2118`, n `214`, weak_sample_signal
