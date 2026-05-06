# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T01:00:35.886843+00:00`
- Correlation status: `ready`
- Asset price records: `408`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.6422` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.2554` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1119` n `7`; crypto_alt avg `0.2122` n `223`; crypto_major avg `0.0232` n `7`; equity avg `0.061` n `47`; fx avg `0.0015` n `4`; index avg `0.1283` n `6`; metal avg `0.1812` n `7`; unknown avg `0.0255` n `313`
- 1h: commodity avg `0.0789` n `7`; crypto_alt avg `0.089` n `223`; crypto_major avg `-0.0794` n `7`; equity avg `-0.0097` n `47`; fx avg `-0.0529` n `4`; index avg `0.4701` n `6`; metal avg `0.3182` n `7`; unknown avg `-0.0224` n `313`
- 4h: commodity avg `-0.518` n `7`; crypto_alt avg `-0.3962` n `223`; crypto_major avg `-0.5613` n `7`; equity avg `0.7125` n `47`; fx avg `-0.1632` n `4`; index avg `0.6941` n `6`; metal avg `1.0809` n `7`; unknown avg `0.037` n `313`
- 24h: commodity avg `-1.6082` n `7`; crypto_alt avg `2.0639` n `223`; crypto_major avg `1.9025` n `7`; equity avg `2.7194` n `47`; fx avg `-0.2006` n `4`; index avg `2.3558` n `6`; metal avg `1.5869` n `7`; unknown avg `1.3701` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1915`, n `404`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1852`, n `404`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.13`, n `404`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.126`, n `404`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `404`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1033`, n `400`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1021`, n `404`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1011`, n `404`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `404`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0961`, n `400`, weak_sample_signal
