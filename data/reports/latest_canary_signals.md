# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T09:18:21.145549+00:00`
- Correlation status: `ready`
- Asset price records: `60`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0019` n `7`; crypto_alt avg `0.1859` n `223`; crypto_major avg `0.1302` n `7`; equity avg `-0.0086` n `42`; fx avg `0.0083` n `4`; index avg `-0.0154` n `9`; metal avg `0.0066` n `7`; unknown avg `0.0904` n `313`
- 1h: commodity avg `0.0052` n `7`; crypto_alt avg `0.3458` n `223`; crypto_major avg `0.1942` n `7`; equity avg `-0.1256` n `42`; fx avg `0.004` n `4`; index avg `-0.0093` n `9`; metal avg `0.0201` n `7`; unknown avg `0.0497` n `313`
- 4h: commodity avg `0.0495` n `7`; crypto_alt avg `0.7232` n `223`; crypto_major avg `0.5492` n `7`; equity avg `0.1555` n `42`; fx avg `-0.0459` n `4`; index avg `-0.0181` n `9`; metal avg `0.091` n `7`; unknown avg `0.2592` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5802`, n `56`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5773`, n `52`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5599`, n `56`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.552`, n `52`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4738`, n `56`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4737`, n `52`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4588`, n `52`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4463`, n `52`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4408`, n `56`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4393`, n `56`, moderate_sample_signal
