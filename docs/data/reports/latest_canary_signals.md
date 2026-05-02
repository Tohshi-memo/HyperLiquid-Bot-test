# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T09:15:21.519845+00:00`
- Correlation status: `ready`
- Asset price records: `60`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `7`; crypto_alt avg `0.1904` n `223`; crypto_major avg `0.1192` n `7`; equity avg `-0.0248` n `42`; fx avg `0.0051` n `4`; index avg `-0.0122` n `9`; metal avg `0.0051` n `7`; unknown avg `0.0923` n `313`
- 1h: commodity avg `0.001` n `7`; crypto_alt avg `0.3503` n `223`; crypto_major avg `0.1833` n `7`; equity avg `-0.1416` n `42`; fx avg `0.0008` n `4`; index avg `-0.0061` n `9`; metal avg `0.0186` n `7`; unknown avg `0.052` n `313`
- 4h: commodity avg `0.0454` n `7`; crypto_alt avg `0.7283` n `223`; crypto_major avg `0.5383` n `7`; equity avg `0.1391` n `42`; fx avg `-0.0491` n `4`; index avg `-0.0148` n `9`; metal avg `0.0895` n `7`; unknown avg `0.2618` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5808`, n `56`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.576`, n `52`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5605`, n `56`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5521`, n `52`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4739`, n `52`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4736`, n `56`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4592`, n `52`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4466`, n `52`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4407`, n `56`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4391`, n `56`, moderate_sample_signal
