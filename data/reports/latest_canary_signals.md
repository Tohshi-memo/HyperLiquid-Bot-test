# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T00:09:32.436610+00:00`
- Correlation status: `ready`
- Asset price records: `404`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1372` n `7`; crypto_alt avg `0.1582` n `223`; crypto_major avg `0.0702` n `7`; equity avg `0.0729` n `47`; fx avg `-0.248` n `4`; index avg `0.0131` n `6`; metal avg `0.0349` n `7`; unknown avg `0.32` n `313`
- 1h: commodity avg `-0.1159` n `7`; crypto_alt avg `-0.0692` n `223`; crypto_major avg `-0.3677` n `7`; equity avg `-0.1498` n `47`; fx avg `-0.2233` n `4`; index avg `-0.0254` n `6`; metal avg `0.3485` n `7`; unknown avg `-0.2749` n `313`
- 4h: commodity avg `-0.6026` n `7`; crypto_alt avg `0.2575` n `223`; crypto_major avg `-0.225` n `7`; equity avg `0.9146` n `47`; fx avg `-0.1199` n `4`; index avg `0.3323` n `6`; metal avg `0.818` n `7`; unknown avg `-0.0682` n `313`
- 24h: commodity avg `-1.7149` n `7`; crypto_alt avg `2.2391` n `223`; crypto_major avg `2.383` n `7`; equity avg `3.0893` n `47`; fx avg `-0.1543` n `4`; index avg `1.8921` n `6`; metal avg `1.4781` n `7`; unknown avg `1.3947` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1926`, n `400`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1863`, n `400`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `400`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `400`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1101`, n `400`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1073`, n `396`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.102`, n `400`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `400`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `400`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0997`, n `396`, weak_sample_signal
