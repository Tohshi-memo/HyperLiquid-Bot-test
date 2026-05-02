# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T04:45:20.105454+00:00`
- Correlation status: `ready`
- Asset price records: `42`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0048` n `7`; crypto_alt avg `-0.0524` n `223`; crypto_major avg `-0.0074` n `7`; equity avg `-0.0034` n `42`; fx avg `-0.005` n `4`; index avg `-0.0051` n `9`; metal avg `-0.0035` n `7`; unknown avg `0.0253` n `311`
- 1h: commodity avg `0.0087` n `7`; crypto_alt avg `-0.1845` n `223`; crypto_major avg `-0.0673` n `7`; equity avg `-0.1322` n `42`; fx avg `-0.0252` n `4`; index avg `-0.035` n `9`; metal avg `-0.0244` n `7`; unknown avg `0.2008` n `311`
- 4h: commodity avg `-0.0509` n `7`; crypto_alt avg `-0.2743` n `223`; crypto_major avg `-0.0508` n `7`; equity avg `0.0063` n `42`; fx avg `-0.0514` n `4`; index avg `0.0157` n `9`; metal avg `-0.0157` n `7`; unknown avg `0.0325` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6559`, n `38`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6326`, n `38`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5704`, n `34`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5621`, n `34`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.547`, n `38`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.5139`, n `34`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.5133`, n `34`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5087`, n `38`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5071`, n `38`, strong_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.5053`, n `34`, strong_sample_signal
