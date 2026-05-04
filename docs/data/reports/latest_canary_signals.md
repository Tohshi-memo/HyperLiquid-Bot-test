# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T07:30:25.617987+00:00`
- Correlation status: `ready`
- Asset price records: `245`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0336` n `7`; crypto_alt avg `0.0168` n `223`; crypto_major avg `-0.0142` n `7`; equity avg `-0.011` n `42`; fx avg `-0.0053` n `4`; index avg `-0.0154` n `9`; metal avg `0.0291` n `7`; unknown avg `-0.0397` n `314`
- 1h: commodity avg `0.4025` n `7`; crypto_alt avg `0.2543` n `223`; crypto_major avg `0.2953` n `7`; equity avg `0.0927` n `42`; fx avg `-0.0072` n `4`; index avg `-0.0524` n `9`; metal avg `-0.3452` n `7`; unknown avg `-0.0427` n `314`
- 4h: commodity avg `0.3345` n `7`; crypto_alt avg `0.1222` n `223`; crypto_major avg `-0.1748` n `7`; equity avg `-0.2766` n `42`; fx avg `-0.0533` n `4`; index avg `0.1247` n `9`; metal avg `-0.7287` n `7`; unknown avg `-0.4353` n `312`
- 24h: commodity avg `0.4454` n `7`; crypto_alt avg `2.1392` n `223`; crypto_major avg `2.1604` n `7`; equity avg `1.1637` n `42`; fx avg `-0.0422` n `4`; index avg `0.8429` n `9`; metal avg `-0.4331` n `7`; unknown avg `-0.2548` n `311`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.382`, n `237`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3737`, n `237`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.3518`, n `241`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3391`, n `241`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.2063`, n `237`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1967`, n `237`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1776`, n `241`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1717`, n `241`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1656`, n `237`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1608`, n `241`, weak_sample_signal
