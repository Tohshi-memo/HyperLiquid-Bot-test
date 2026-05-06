# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T06:15:36.049819+00:00`
- Correlation status: `ready`
- Asset price records: `429`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1395` n `7`; crypto_alt avg `-0.2642` n `223`; crypto_major avg `-0.0965` n `7`; equity avg `0.0104` n `47`; fx avg `-0.0397` n `4`; index avg `0.0601` n `6`; metal avg `-0.1423` n `7`; unknown avg `0.1546` n `313`
- 1h: commodity avg `-0.229` n `7`; crypto_alt avg `0.1388` n `223`; crypto_major avg `0.2238` n `7`; equity avg `0.238` n `47`; fx avg `-0.0514` n `4`; index avg `0.1317` n `6`; metal avg `-0.0106` n `7`; unknown avg `0.4305` n `311`
- 4h: commodity avg `0.0365` n `7`; crypto_alt avg `-0.1374` n `223`; crypto_major avg `0.1127` n `7`; equity avg `0.7743` n `47`; fx avg `-0.2494` n `4`; index avg `0.3377` n `6`; metal avg `0.4687` n `7`; unknown avg `0.5835` n `311`
- 24h: commodity avg `-1.6271` n `7`; crypto_alt avg `2.1688` n `223`; crypto_major avg `1.6887` n `7`; equity avg `2.852` n `47`; fx avg `-0.4435` n `4`; index avg `2.3316` n `6`; metal avg `2.1364` n `7`; unknown avg `1.5004` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1808`, n `425`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1745`, n `425`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1277`, n `425`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1264`, n `425`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1225`, n `425`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1106`, n `425`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.102`, n `421`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0969`, n `421`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `425`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0949`, n `425`, weak_sample_signal
