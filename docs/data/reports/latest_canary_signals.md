# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T23:10:30.546556+00:00`
- Correlation status: `ready`
- Asset price records: `211`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1272` n `7`; crypto_alt avg `-0.211` n `223`; crypto_major avg `-0.1402` n `7`; equity avg `-0.184` n `42`; fx avg `-0.004` n `4`; index avg `-0.016` n `9`; metal avg `-0.1499` n `7`; unknown avg `-0.108` n `314`
- 1h: commodity avg `0.4924` n `7`; crypto_alt avg `0.2357` n `223`; crypto_major avg `0.4934` n `7`; equity avg `-0.1648` n `42`; fx avg `-0.0064` n `4`; index avg `-0.2783` n `9`; metal avg `0.0526` n `7`; unknown avg `-0.0939` n `314`
- 4h: commodity avg `-0.1317` n `7`; crypto_alt avg `0.2472` n `223`; crypto_major avg `0.5696` n `7`; equity avg `0.0038` n `42`; fx avg `-0.0276` n `4`; index avg `-0.0145` n `9`; metal avg `0.0069` n `7`; unknown avg `-0.0721` n `314`
- 24h: commodity avg `-0.19` n `7`; crypto_alt avg `-0.0052` n `223`; crypto_major avg `0.6081` n `7`; equity avg `0.1455` n `42`; fx avg `-0.0193` n `4`; index avg `0.0566` n `9`; metal avg `0.4155` n `7`; unknown avg `0.0527` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3917`, n `207`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3745`, n `207`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3176`, n `207`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3127`, n `207`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3071`, n `207`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.2967`, n `203`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.2959`, n `203`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.295`, n `207`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.294`, n `207`, moderate_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.2346`, n `207`, weak_sample_signal
