# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T11:00:27.092681+00:00`
- Correlation status: `ready`
- Asset price records: `67`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0255` n `7`; crypto_alt avg `-0.0782` n `223`; crypto_major avg `-0.0541` n `7`; equity avg `-0.0373` n `42`; fx avg `-0.0024` n `4`; index avg `0.0006` n `9`; metal avg `0.0023` n `7`; unknown avg `0.0232` n `313`
- 1h: commodity avg `0.0163` n `7`; crypto_alt avg `-0.0809` n `223`; crypto_major avg `-0.1561` n `7`; equity avg `0.012` n `42`; fx avg `0.0037` n `4`; index avg `0.0045` n `9`; metal avg `-0.0013` n `7`; unknown avg `-0.0725` n `313`
- 4h: commodity avg `0.0416` n `7`; crypto_alt avg `0.2787` n `223`; crypto_major avg `-0.0655` n `7`; equity avg `-0.0782` n `42`; fx avg `0.052` n `4`; index avg `-0.0385` n `9`; metal avg `0.0529` n `7`; unknown avg `0.1419` n `311`
- 24h: crypto_alt avg `0.8077` n `223`; crypto_major avg `0.597` n `7`; metal avg `0.7862` n `1`; unknown avg `1.3757` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5754`, n `63`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5614`, n `59`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5555`, n `63`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5523`, n `59`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4884`, n `63`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.479`, n `59`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4762`, n `59`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4629`, n `59`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4528`, n `63`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4428`, n `63`, moderate_sample_signal
