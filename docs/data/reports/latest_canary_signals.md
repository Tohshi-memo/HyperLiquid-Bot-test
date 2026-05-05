# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T18:15:31.855078+00:00`
- Correlation status: `ready`
- Asset price records: `381`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0596` n `7`; crypto_alt avg `0.1124` n `223`; crypto_major avg `0.241` n `7`; equity avg `0.0796` n `47`; fx avg `-0.0322` n `4`; index avg `0.0265` n `6`; metal avg `0.0365` n `7`; unknown avg `1.112` n `313`
- 1h: commodity avg `-0.0448` n `7`; crypto_alt avg `0.1927` n `223`; crypto_major avg `0.542` n `7`; equity avg `0.1128` n `47`; fx avg `-0.0009` n `4`; index avg `0.1232` n `6`; metal avg `0.0924` n `7`; unknown avg `1.1122` n `313`
- 4h: commodity avg `-0.1871` n `7`; crypto_alt avg `-0.0171` n `223`; crypto_major avg `0.4354` n `7`; equity avg `0.1215` n `47`; fx avg `-0.1511` n `4`; index avg `0.43` n `6`; metal avg `-0.5694` n `7`; unknown avg `1.0786` n `313`
- 24h: commodity avg `-1.2256` n `7`; crypto_alt avg `1.208` n `223`; crypto_major avg `1.9182` n `7`; equity avg `1.6943` n `47`; fx avg `-0.048` n `4`; index avg `1.3704` n `6`; metal avg `0.8856` n `7`; unknown avg `1.7966` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.207`, n `377`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2002`, n `377`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1318`, n `377`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1278`, n `377`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.114`, n `373`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1086`, n `377`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1062`, n `373`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1052`, n `377`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1051`, n `377`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1043`, n `377`, weak_sample_signal
