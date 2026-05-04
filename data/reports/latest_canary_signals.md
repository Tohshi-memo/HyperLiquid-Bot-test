# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T13:30:32.210897+00:00`
- Correlation status: `ready`
- Asset price records: `269`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.2748` n `7`; crypto_alt avg `0.1406` n `223`; crypto_major avg `0.0122` n `7`; equity avg `0.1742` n `42`; fx avg `-0.0011` n `4`; index avg `0.0972` n `9`; metal avg `-0.1942` n `7`; unknown avg `0.0317` n `314`
- 1h: commodity avg `0.1283` n `7`; crypto_alt avg `-0.0252` n `223`; crypto_major avg `-0.0742` n `7`; equity avg `0.0876` n `42`; fx avg `0.0043` n `4`; index avg `-0.1058` n `9`; metal avg `-0.2754` n `7`; unknown avg `-0.1692` n `314`
- 4h: commodity avg `0.051` n `7`; crypto_alt avg `-0.7337` n `223`; crypto_major avg `-0.9975` n `7`; equity avg `-0.3917` n `42`; fx avg `-0.0181` n `4`; index avg `-0.1227` n `9`; metal avg `-0.5693` n `7`; unknown avg `-0.3517` n `314`
- 24h: commodity avg `0.7073` n `7`; crypto_alt avg `1.2031` n `223`; crypto_major avg `0.5811` n `7`; equity avg `0.5014` n `42`; fx avg `-0.0781` n `4`; index avg `0.4691` n `9`; metal avg `-1.5605` n `7`; unknown avg `-0.0551` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2673`, n `265`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2592`, n `265`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1813`, n `261`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1703`, n `261`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1664`, n `265`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.166`, n `261`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.165`, n `261`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1625`, n `265`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1614`, n `261`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1578`, n `265`, weak_sample_signal
