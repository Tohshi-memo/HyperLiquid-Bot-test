# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T05:15:31.170994+00:00`
- Correlation status: `ready`
- Asset price records: `331`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0315` n `7`; crypto_alt avg `0.3238` n `223`; crypto_major avg `0.0917` n `7`; equity avg `0.1818` n `47`; fx avg `0.0011` n `4`; index avg `0.0796` n `6`; metal avg `0.2432` n `7`; unknown avg `-0.2023` n `312`
- 1h: commodity avg `-0.0156` n `7`; crypto_alt avg `0.2276` n `223`; crypto_major avg `0.0565` n `7`; equity avg `0.2927` n `47`; fx avg `-0.0089` n `4`; index avg `0.1217` n `6`; metal avg `0.1641` n `7`; unknown avg `-0.1342` n `312`
- 4h: commodity avg `-0.192` n `7`; crypto_alt avg `0.4666` n `223`; crypto_major avg `0.6469` n `7`; equity avg `0.3847` n `47`; fx avg `-0.0094` n `4`; index avg `0.2701` n `6`; metal avg `0.1536` n `7`; unknown avg `0.2106` n `312`
- 24h: commodity avg `1.1346` n `7`; crypto_alt avg `0.7239` n `223`; crypto_major avg `-0.3934` n `7`; equity avg `-0.6375` n `47`; fx avg `-0.0124` n `4`; index avg `-0.0794` n `6`; metal avg `-1.6017` n `7`; unknown avg `-1.4363` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2265`, n `327`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2201`, n `327`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1512`, n `327`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1408`, n `327`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1361`, n `327`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1345`, n `323`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1317`, n `323`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1296`, n `327`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1221`, n `327`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `327`, weak_sample_signal
