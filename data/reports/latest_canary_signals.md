# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T03:15:33.220131+00:00`
- Correlation status: `ready`
- Asset price records: `323`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0536` n `7`; crypto_alt avg `0.0295` n `223`; crypto_major avg `0.1772` n `7`; equity avg `0.0969` n `47`; fx avg `-0.0011` n `4`; index avg `0.0458` n `6`; metal avg `0.0328` n `7`; unknown avg `-0.0662` n `312`
- 1h: commodity avg `-0.0563` n `7`; crypto_alt avg `-0.0323` n `223`; crypto_major avg `0.1628` n `7`; equity avg `0.2823` n `47`; fx avg `0.0005` n `4`; index avg `0.0682` n `6`; metal avg `0.1027` n `7`; unknown avg `-0.0986` n `312`
- 4h: commodity avg `-0.2671` n `7`; crypto_alt avg `0.7874` n `223`; crypto_major avg `0.7465` n `7`; equity avg `0.7512` n `47`; fx avg `-0.0139` n `4`; index avg `0.1391` n `6`; metal avg `0.6084` n `7`; unknown avg `0.0701` n `312`
- 24h: commodity avg `1.003` n `7`; crypto_alt avg `0.6416` n `223`; crypto_major avg `-0.4498` n `7`; equity avg `-0.9228` n `47`; fx avg `-0.0834` n `4`; index avg `-0.2456` n `6`; metal avg `-1.7893` n `7`; unknown avg `-1.4536` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2268`, n `319`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2201`, n `319`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1503`, n `319`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1422`, n `319`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1402`, n `315`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1375`, n `315`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1374`, n `319`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `319`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1261`, n `319`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1209`, n `315`, weak_sample_signal
