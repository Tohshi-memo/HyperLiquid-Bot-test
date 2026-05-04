# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T11:15:28.909083+00:00`
- Correlation status: `ready`
- Asset price records: `260`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.016` n `7`; crypto_alt avg `0.0803` n `223`; crypto_major avg `0.0044` n `7`; equity avg `0.1726` n `42`; fx avg `-0.0056` n `4`; index avg `0.0844` n `9`; metal avg `-0.0822` n `7`; unknown avg `-0.0429` n `314`
- 1h: commodity avg `-0.6056` n `7`; crypto_alt avg `0.341` n `223`; crypto_major avg `0.4056` n `7`; equity avg `0.6962` n `42`; fx avg `0.0016` n `4`; index avg `0.3165` n `9`; metal avg `0.7061` n `7`; unknown avg `0.4043` n `314`
- 4h: commodity avg `0.4691` n `7`; crypto_alt avg `-0.8905` n `223`; crypto_major avg `-1.2197` n `7`; equity avg `-0.7269` n `42`; fx avg `-0.018` n `4`; index avg `-0.4359` n `9`; metal avg `-1.016` n `7`; unknown avg `0.1675` n `314`
- 24h: commodity avg `1.0224` n `7`; crypto_alt avg `1.0829` n `223`; crypto_major avg `0.8595` n `7`; equity avg `0.3184` n `42`; fx avg `-0.0756` n `4`; index avg `0.4738` n `9`; metal avg `-1.558` n `7`; unknown avg `0.2094` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2817`, n `256`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2739`, n `256`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.2094`, n `252`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2086`, n `252`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1944`, n `252`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1869`, n `256`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1799`, n `252`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1742`, n `252`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1737`, n `256`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1634`, n `256`, weak_sample_signal
