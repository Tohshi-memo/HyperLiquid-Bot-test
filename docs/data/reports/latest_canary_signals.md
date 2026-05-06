# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-06T04:45:25.180231+00:00`
- Correlation status: `ready`
- Asset price records: `423`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0013` n `7`; crypto_alt avg `0.0803` n `223`; crypto_major avg `0.0819` n `7`; equity avg `0.0136` n `47`; fx avg `-0.1449` n `4`; index avg `0.1405` n `6`; metal avg `-0.0649` n `7`; unknown avg `0.0067` n `313`
- 1h: commodity avg `0.016` n `7`; crypto_alt avg `-0.2079` n `223`; crypto_major avg `-0.1829` n `7`; equity avg `0.2395` n `47`; fx avg `-0.3293` n `4`; index avg `0.1567` n `6`; metal avg `0.0706` n `7`; unknown avg `0.0116` n `313`
- 4h: commodity avg `-0.2022` n `7`; crypto_alt avg `1.1499` n `223`; crypto_major avg `0.6056` n `7`; equity avg `0.8328` n `47`; fx avg `-0.301` n `4`; index avg `0.3555` n `6`; metal avg `1.095` n `7`; unknown avg `0.2734` n `313`
- 24h: commodity avg `-1.4218` n `7`; crypto_alt avg `2.4956` n `223`; crypto_major avg `1.8866` n `7`; equity avg `3.2822` n `47`; fx avg `-0.4992` n `4`; index avg `2.3249` n `6`; metal avg `2.332` n `7`; unknown avg `1.2849` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1809`, n `419`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1746`, n `419`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.128`, n `419`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `419`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `419`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1108`, n `419`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1011`, n `415`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0959`, n `419`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0958`, n `415`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0951`, n `419`, weak_sample_signal
