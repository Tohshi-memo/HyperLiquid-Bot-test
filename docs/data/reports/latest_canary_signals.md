# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T02:45:18.877214+00:00`
- Correlation status: `ready`
- Asset price records: `34`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0078` n `7`; crypto_alt avg `0.0136` n `223`; crypto_major avg `0.1432` n `7`; equity avg `0.01` n `42`; fx avg `-0.0032` n `4`; index avg `-0.0042` n `9`; metal avg `-0.0049` n `7`; unknown avg `-0.0031` n `311`
- 1h: commodity avg `-0.0091` n `7`; crypto_alt avg `-0.1019` n `223`; crypto_major avg `-0.0025` n `7`; equity avg `0.1302` n `42`; fx avg `-0.018` n `4`; index avg `0.0088` n `9`; metal avg `-0.0013` n `7`; unknown avg `-0.0025` n `311`
- 4h: commodity avg `0.0369` n `7`; crypto_alt avg `-0.0705` n `223`; crypto_major avg `0.1038` n `7`; equity avg `0.1336` n `42`; fx avg `0.0359` n `4`; index avg `-0.1166` n `9`; metal avg `-0.0022` n `7`; unknown avg `-0.0442` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.67`, n `30`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.646`, n `30`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5321`, n `30`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5314`, n `26`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5181`, n `26`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4985`, n `30`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4979`, n `30`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4852`, n `30`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.4794`, n `30`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4667`, n `26`, moderate_sample_signal
