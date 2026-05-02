# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T10:45:21.979368+00:00`
- Correlation status: `ready`
- Asset price records: `66`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `7`; crypto_alt avg `0.0151` n `223`; crypto_major avg `-0.0129` n `7`; equity avg `-0.0202` n `42`; fx avg `0.0` n `4`; index avg `0.0004` n `9`; metal avg `-0.0081` n `7`; unknown avg `-0.0261` n `313`
- 1h: commodity avg `-0.0161` n `7`; crypto_alt avg `-0.0832` n `223`; crypto_major avg `-0.1951` n `7`; equity avg `0.0444` n `42`; fx avg `0.0077` n `4`; index avg `-0.0036` n `9`; metal avg `0.0009` n `7`; unknown avg `-0.0889` n `313`
- 4h: commodity avg `0.0107` n `7`; crypto_alt avg `0.5058` n `223`; crypto_major avg `0.1912` n `7`; equity avg `0.0105` n `42`; fx avg `0.0488` n `4`; index avg `-0.0299` n `9`; metal avg `0.056` n `7`; unknown avg `0.1575` n `311`
- 24h: crypto_alt avg `0.8858` n `223`; crypto_major avg `0.6511` n `7`; metal avg `0.784` n `1`; unknown avg `1.3529` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5759`, n `62`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5662`, n `58`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5648`, n `58`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5559`, n `62`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4918`, n `58`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4829`, n `62`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4752`, n `58`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.462`, n `58`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4469`, n `62`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.435`, n `62`, moderate_sample_signal
