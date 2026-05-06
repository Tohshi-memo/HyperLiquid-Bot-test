# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T07:15:27.422649+00:00`
- Correlation status: `ready`
- Asset price records: `433`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0599` n `7`; crypto_alt avg `-0.0306` n `223`; crypto_major avg `-0.0708` n `7`; equity avg `0.0781` n `47`; fx avg `0.0036` n `4`; index avg `0.0027` n `6`; metal avg `-0.0316` n `7`; unknown avg `-0.0093` n `313`
- 1h: commodity avg `0.0937` n `7`; crypto_alt avg `0.7444` n `223`; crypto_major avg `0.3402` n `7`; equity avg `-0.0816` n `47`; fx avg `0.1006` n `4`; index avg `-0.1857` n `6`; metal avg `-0.0366` n `7`; unknown avg `0.438` n `313`
- 4h: commodity avg `0.0088` n `7`; crypto_alt avg `0.6928` n `223`; crypto_major avg `0.4726` n `7`; equity avg `0.4847` n `47`; fx avg `-0.1641` n `4`; index avg `0.2083` n `6`; metal avg `-0.0283` n `7`; unknown avg `0.9559` n `311`
- 24h: commodity avg `-1.4101` n `7`; crypto_alt avg `2.9488` n `223`; crypto_major avg `1.7963` n `7`; equity avg `2.4085` n `47`; fx avg `-0.3383` n `4`; index avg `1.93` n `6`; metal avg `1.7456` n `7`; unknown avg `2.0264` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1806`, n `429`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1743`, n `429`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `429`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1256`, n `429`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1218`, n `429`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `429`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1002`, n `425`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0951`, n `425`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0941`, n `429`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0934`, n `429`, weak_sample_signal
