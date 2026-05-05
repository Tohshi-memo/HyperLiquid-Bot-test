# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T13:15:23.510860+00:00`
- Correlation status: `ready`
- Asset price records: `363`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0966` n `7`; crypto_alt avg `0.2349` n `223`; crypto_major avg `0.3388` n `7`; equity avg `-0.0053` n `47`; fx avg `0.0116` n `4`; index avg `0.005` n `6`; metal avg `0.2542` n `7`; unknown avg `0.2298` n `312`
- 1h: commodity avg `-0.0996` n `7`; crypto_alt avg `0.4468` n `223`; crypto_major avg `0.4911` n `7`; equity avg `-0.0107` n `47`; fx avg `0.0225` n `4`; index avg `0.2114` n `6`; metal avg `-0.0928` n `7`; unknown avg `0.2098` n `312`
- 4h: commodity avg `-0.3713` n `7`; crypto_alt avg `0.8579` n `223`; crypto_major avg `1.166` n `7`; equity avg `0.3703` n `47`; fx avg `0.0545` n `4`; index avg `0.374` n `6`; metal avg `0.3351` n `7`; unknown avg `0.442` n `312`
- 24h: commodity avg `0.3853` n `7`; crypto_alt avg `2.8267` n `223`; crypto_major avg `2.7689` n `7`; equity avg `0.9099` n `47`; fx avg `0.0854` n `4`; index avg `0.6671` n `6`; metal avg `0.6396` n `7`; unknown avg `0.1654` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2087`, n `359`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2015`, n `359`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1343`, n `359`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1302`, n `359`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1064`, n `359`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1041`, n `359`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1036`, n `359`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1029`, n `359`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0915`, n `355`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0901`, n `359`, weak_sample_signal
