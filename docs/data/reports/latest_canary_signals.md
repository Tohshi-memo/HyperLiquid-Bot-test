# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T13:15:21.888307+00:00`
- Correlation status: `ready`
- Asset price records: `76`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0001` n `7`; crypto_alt avg `0.1273` n `223`; crypto_major avg `0.1753` n `7`; equity avg `0.0199` n `42`; fx avg `-0.0051` n `4`; index avg `0.0052` n `9`; metal avg `-0.0072` n `7`; unknown avg `-0.011` n `313`
- 1h: commodity avg `0.0028` n `7`; crypto_alt avg `0.2138` n `223`; crypto_major avg `0.264` n `7`; equity avg `0.0382` n `42`; fx avg `-0.0104` n `4`; index avg `0.0349` n `9`; metal avg `0.0072` n `7`; unknown avg `0.0307` n `313`
- 4h: commodity avg `-0.0526` n `7`; crypto_alt avg `0.1558` n `223`; crypto_major avg `-0.0776` n `7`; equity avg `0.0809` n `42`; fx avg `-0.0208` n `4`; index avg `0.0508` n `9`; metal avg `0.0269` n `7`; unknown avg `-0.1569` n `313`
- 24h: crypto_alt avg `0.3903` n `223`; crypto_major avg `-0.3133` n `7`; metal avg `0.3904` n `1`; unknown avg `0.826` n `310`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5564`, n `72`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5546`, n `68`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5452`, n `68`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5372`, n `72`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4904`, n `72`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.483`, n `68`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4793`, n `68`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4704`, n `68`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4577`, n `72`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4507`, n `72`, moderate_sample_signal
