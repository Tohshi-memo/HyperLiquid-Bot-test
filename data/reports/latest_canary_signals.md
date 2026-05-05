# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T23:30:30.684133+00:00`
- Correlation status: `ready`
- Asset price records: `402`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `-1.5253` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.041` n `7`; crypto_alt avg `-0.3007` n `223`; crypto_major avg `-0.4039` n `7`; equity avg `-0.1249` n `47`; fx avg `0.0081` n `4`; index avg `-0.0313` n `6`; metal avg `-0.1625` n `7`; unknown avg `-0.2811` n `313`
- 1h: commodity avg `-0.6963` n `7`; crypto_alt avg `-0.5762` n `223`; crypto_major avg `-0.7378` n `7`; equity avg `0.1889` n `47`; fx avg `0.0212` n `4`; index avg `0.1437` n `6`; metal avg `0.7875` n `7`; unknown avg `-0.0986` n `313`
- 4h: commodity avg `-0.6924` n `7`; crypto_alt avg `0.1097` n `223`; crypto_major avg `-0.2395` n `7`; equity avg `0.8825` n `47`; fx avg `0.1241` n `4`; index avg `0.2699` n `6`; metal avg `0.5408` n `7`; unknown avg `-0.1565` n `313`
- 24h: commodity avg `-1.8382` n `7`; crypto_alt avg `2.0037` n `223`; crypto_major avg `2.1417` n `7`; equity avg `2.8996` n `47`; fx avg `0.0882` n `4`; index avg `1.8652` n `6`; metal avg `1.3211` n `7`; unknown avg `1.2657` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1972`, n `398`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1908`, n `398`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1299`, n `398`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1258`, n `398`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1081`, n `398`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1079`, n `394`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.104`, n `398`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `398`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `398`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1002`, n `394`, weak_sample_signal
