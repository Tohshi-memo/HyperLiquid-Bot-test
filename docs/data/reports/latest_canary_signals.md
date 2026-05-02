# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T12:45:17.053768+00:00`
- Correlation status: `ready`
- Asset price records: `74`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0041` n `7`; crypto_alt avg `-0.0055` n `223`; crypto_major avg `-0.073` n `7`; equity avg `0.0053` n `42`; fx avg `0.0064` n `4`; index avg `0.002` n `9`; metal avg `0.0123` n `7`; unknown avg `-0.0444` n `313`
- 1h: commodity avg `-0.0465` n `7`; crypto_alt avg `0.4237` n `223`; crypto_major avg `0.1703` n `7`; equity avg `-0.0396` n `42`; fx avg `0.0085` n `4`; index avg `0.0372` n `9`; metal avg `0.0156` n `7`; unknown avg `0.058` n `313`
- 4h: commodity avg `-0.0494` n `7`; crypto_alt avg `0.4701` n `223`; crypto_major avg `-0.1183` n `7`; equity avg `-0.14` n `42`; fx avg `-0.0255` n `4`; index avg `0.0307` n `9`; metal avg `0.0356` n `7`; unknown avg `0.0728` n `313`
- 24h: crypto_alt avg `1.0646` n `223`; crypto_major avg `0.6265` n `7`; metal avg `0.7928` n `1`; unknown avg `1.3736` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5679`, n `70`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5559`, n `66`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5483`, n `70`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5459`, n `66`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4922`, n `70`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4821`, n `66`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4787`, n `66`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4695`, n `66`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4584`, n `70`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4525`, n `70`, moderate_sample_signal
