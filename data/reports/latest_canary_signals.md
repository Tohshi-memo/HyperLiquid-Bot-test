# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T13:00:36.777198+00:00`
- Correlation status: `ready`
- Asset price records: `362`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0178` n `7`; crypto_alt avg `0.0212` n `223`; crypto_major avg `0.0787` n `7`; equity avg `-0.0798` n `47`; fx avg `-0.0013` n `4`; index avg `-0.0543` n `6`; metal avg `-0.1772` n `7`; unknown avg `-0.0911` n `312`
- 1h: commodity avg `-0.0883` n `7`; crypto_alt avg `0.2069` n `223`; crypto_major avg `0.2119` n `7`; equity avg `0.0499` n `47`; fx avg `0.0125` n `4`; index avg `0.2452` n `6`; metal avg `-0.2242` n `7`; unknown avg `-0.0178` n `312`
- 4h: commodity avg `-0.1287` n `7`; crypto_alt avg `0.621` n `223`; crypto_major avg `0.7965` n `7`; equity avg `0.3612` n `47`; fx avg `0.066` n `4`; index avg `0.3959` n `6`; metal avg `0.1191` n `7`; unknown avg `0.182` n `312`
- 24h: commodity avg `0.0647` n `7`; crypto_alt avg `2.8168` n `223`; crypto_major avg `2.7815` n `7`; equity avg `1.0285` n `47`; fx avg `0.0685` n `4`; index avg `0.7142` n `6`; metal avg `0.483` n `7`; unknown avg `-0.4079` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2086`, n `358`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2014`, n `358`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.135`, n `358`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1308`, n `358`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1055`, n `358`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1047`, n `358`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1041`, n `358`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.102`, n `358`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0928`, n `354`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `358`, weak_sample_signal
