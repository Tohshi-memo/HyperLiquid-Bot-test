# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T20:45:38.714669+00:00`
- Correlation status: `ready`
- Asset price records: `106`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `7`; crypto_alt avg `-0.107` n `223`; crypto_major avg `0.0139` n `7`; equity avg `0.0445` n `42`; fx avg `-0.004` n `4`; index avg `0.0079` n `9`; metal avg `-0.0021` n `7`; unknown avg `-0.0576` n `313`
- 1h: commodity avg `-0.0112` n `7`; crypto_alt avg `-0.0999` n `223`; crypto_major avg `-0.0737` n `7`; equity avg `0.1293` n `42`; fx avg `0.008` n `4`; index avg `0.0005` n `9`; metal avg `-0.0058` n `7`; unknown avg `-0.011` n `313`
- 4h: commodity avg `-0.1855` n `7`; crypto_alt avg `0.2883` n `223`; crypto_major avg `-0.0188` n `7`; equity avg `0.3513` n `42`; fx avg `0.041` n `4`; index avg `0.056` n `9`; metal avg `-0.0459` n `7`; unknown avg `0.1483` n `313`
- 24h: commodity avg `-0.0352` n `7`; crypto_alt avg `1.5277` n `223`; crypto_major avg `0.2196` n `7`; equity avg `0.9869` n `42`; fx avg `-0.0154` n `4`; index avg `0.0691` n `9`; metal avg `-0.0991` n `7`; unknown avg `0.3016` n `311`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.5283`, n `98`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5096`, n `98`, strong_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5075`, n `102`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4899`, n `102`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.45`, n `98`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4308`, n `98`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.427`, n `98`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4181`, n `98`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4169`, n `98`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4154`, n `102`, moderate_sample_signal
