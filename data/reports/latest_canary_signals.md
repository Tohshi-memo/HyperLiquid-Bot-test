# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T22:30:34.652413+00:00`
- Correlation status: `ready`
- Asset price records: `398`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `7`; crypto_alt avg `0.0483` n `223`; crypto_major avg `0.1214` n `7`; equity avg `0.1822` n `47`; fx avg `0.0034` n `4`; index avg `0.0209` n `6`; metal avg `-0.0947` n `7`; unknown avg `0.025` n `313`
- 1h: commodity avg `-0.0777` n `7`; crypto_alt avg `-0.0394` n `223`; crypto_major avg `0.3924` n `7`; equity avg `0.2885` n `47`; fx avg `0.0524` n `4`; index avg `-0.0032` n `6`; metal avg `-0.2294` n `7`; unknown avg `-0.0177` n `313`
- 4h: commodity avg `0.0231` n `7`; crypto_alt avg `1.0175` n `223`; crypto_major avg `0.6756` n `7`; equity avg `0.5838` n `47`; fx avg `0.1188` n `4`; index avg `0.2477` n `6`; metal avg `-0.4136` n `7`; unknown avg `0.3166` n `313`
- 24h: commodity avg `-1.1351` n `7`; crypto_alt avg `2.227` n `223`; crypto_major avg `2.6168` n `7`; equity avg `2.4426` n `47`; fx avg `0.0705` n `4`; index avg `1.6946` n `6`; metal avg `0.4723` n `7`; unknown avg `1.4285` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2065`, n `394`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1997`, n `394`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `394`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `394`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1118`, n `394`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1109`, n `390`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.107`, n `394`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1026`, n `390`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `394`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `394`, weak_sample_signal
