# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T13:30:21.697936+00:00`
- Correlation status: `ready`
- Asset price records: `77`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `7`; crypto_alt avg `0.0208` n `223`; crypto_major avg `-0.0145` n `7`; equity avg `-0.0016` n `42`; fx avg `-0.0096` n `4`; index avg `0.0006` n `9`; metal avg `-0.0019` n `7`; unknown avg `0.0085` n `313`
- 1h: commodity avg `-0.0045` n `7`; crypto_alt avg `-0.0066` n `223`; crypto_major avg `0.0733` n `7`; equity avg `0.052` n `42`; fx avg `-0.008` n `4`; index avg `0.0075` n `9`; metal avg `0.0113` n `7`; unknown avg `-0.0839` n `313`
- 4h: commodity avg `-0.0565` n `7`; crypto_alt avg `0.2215` n `223`; crypto_major avg `0.0168` n `7`; equity avg `0.0907` n `42`; fx avg `-0.0428` n `4`; index avg `0.0211` n `9`; metal avg `0.0192` n `7`; unknown avg `-0.1047` n `313`
- 24h: crypto_alt avg `0.5089` n `223`; crypto_major avg `-0.076` n `7`; metal avg `0.4759` n `1`; unknown avg `0.86` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.555`, n `73`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5433`, n `69`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5415`, n `69`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5358`, n `73`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4952`, n `73`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4813`, n `69`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4792`, n `69`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4691`, n `69`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4579`, n `73`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4573`, n `73`, moderate_sample_signal
