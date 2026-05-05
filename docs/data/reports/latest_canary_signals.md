# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T03:00:28.487109+00:00`
- Correlation status: `ready`
- Asset price records: `322`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0224` n `7`; crypto_alt avg `-0.2042` n `223`; crypto_major avg `-0.3238` n `7`; equity avg `0.0236` n `47`; fx avg `-0.0072` n `4`; index avg `-0.0156` n `6`; metal avg `-0.101` n `7`; unknown avg `0.2475` n `312`
- 1h: commodity avg `-0.1605` n `7`; crypto_alt avg `0.0396` n `223`; crypto_major avg `0.1866` n `7`; equity avg `0.272` n `47`; fx avg `-0.0005` n `4`; index avg `0.0255` n `6`; metal avg `0.1468` n `7`; unknown avg `-0.0531` n `312`
- 4h: commodity avg `-0.3021` n `7`; crypto_alt avg `0.6012` n `223`; crypto_major avg `0.4504` n `7`; equity avg `0.6168` n `47`; fx avg `-0.0133` n `4`; index avg `0.1101` n `6`; metal avg `0.6491` n `7`; unknown avg `0.0525` n `312`
- 24h: commodity avg `0.9503` n `7`; crypto_alt avg `0.6476` n `223`; crypto_major avg `-0.4243` n `7`; equity avg `-0.934` n `47`; fx avg `-0.0701` n `4`; index avg `-0.3056` n `6`; metal avg `-1.734` n `7`; unknown avg `-1.4779` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.227`, n `318`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2204`, n `318`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1508`, n `318`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1451`, n `314`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1426`, n `314`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1424`, n `318`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1375`, n `318`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1286`, n `318`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1259`, n `318`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1224`, n `314`, weak_sample_signal
