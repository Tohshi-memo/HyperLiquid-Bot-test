# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T13:15:19.160087+00:00`
- Correlation status: `ready`
- Asset price records: `268`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4132` n `7`; crypto_alt avg `0.2255` n `223`; crypto_major avg `0.3525` n `7`; equity avg `0.1492` n `42`; fx avg `-0.0052` n `4`; index avg `-0.0164` n `9`; metal avg `0.0978` n `7`; unknown avg `-0.122` n `314`
- 1h: commodity avg `-0.2364` n `7`; crypto_alt avg `0.0081` n `223`; crypto_major avg `0.0636` n `7`; equity avg `-0.0602` n `42`; fx avg `0.0073` n `4`; index avg `-0.0998` n `9`; metal avg `0.2465` n `7`; unknown avg `0.0729` n `314`
- 4h: commodity avg `-0.1035` n `7`; crypto_alt avg `-0.9309` n `223`; crypto_major avg `-1.0991` n `7`; equity avg `-0.5732` n `42`; fx avg `-0.0041` n `4`; index avg `-0.2769` n `9`; metal avg `-0.4049` n `7`; unknown avg `-0.5459` n `314`
- 24h: commodity avg `0.4498` n `7`; crypto_alt avg `0.8772` n `223`; crypto_major avg `0.4322` n `7`; equity avg `0.3436` n `42`; fx avg `-0.0659` n `4`; index avg `0.3378` n `9`; metal avg `-1.3665` n `7`; unknown avg `-0.167` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2675`, n `264`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2593`, n `264`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1819`, n `260`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1704`, n `260`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1689`, n `260`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.168`, n `260`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1649`, n `264`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1624`, n `264`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1622`, n `260`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1581`, n `264`, weak_sample_signal
