# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T12:45:37.678570+00:00`
- Correlation status: `ready`
- Asset price records: `170`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `7`; crypto_alt avg `0.0098` n `223`; crypto_major avg `-0.0003` n `7`; equity avg `-0.0009` n `42`; fx avg `0.0` n `4`; index avg `0.0428` n `9`; metal avg `0.0014` n `7`; unknown avg `-0.0136` n `313`
- 1h: commodity avg `-0.0133` n `7`; crypto_alt avg `0.2289` n `223`; crypto_major avg `0.1879` n `7`; equity avg `0.0465` n `42`; fx avg `0.0021` n `4`; index avg `0.041` n `9`; metal avg `0.0423` n `7`; unknown avg `-0.1861` n `313`
- 4h: commodity avg `-0.0933` n `7`; crypto_alt avg `0.3696` n `223`; crypto_major avg `0.4913` n `7`; equity avg `0.2733` n `42`; fx avg `0.0112` n `4`; index avg `0.037` n `9`; metal avg `0.0816` n `7`; unknown avg `-0.0554` n `313`
- 24h: commodity avg `-0.2458` n `7`; crypto_alt avg `1.2648` n `223`; crypto_major avg `0.4571` n `7`; equity avg `0.4143` n `42`; fx avg `0.146` n `4`; index avg `0.0782` n `9`; metal avg `0.1572` n `7`; unknown avg `0.2055` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.403`, n `166`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3859`, n `166`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3853`, n `166`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3781`, n `162`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3724`, n `162`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.372`, n `166`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3624`, n `162`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3545`, n `162`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3267`, n `166`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3171`, n `166`, moderate_sample_signal
