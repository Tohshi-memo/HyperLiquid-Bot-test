# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T10:00:27.494086+00:00`
- Correlation status: `ready`
- Asset price records: `63`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.007` n `7`; crypto_alt avg `-0.0809` n `223`; crypto_major avg `-0.0936` n `7`; equity avg `-0.0059` n `42`; fx avg `0.0016` n `4`; index avg `-0.0074` n `9`; metal avg `0.0045` n `7`; unknown avg `0.0015` n `313`
- 1h: commodity avg `-0.0131` n `7`; crypto_alt avg `0.1973` n `223`; crypto_major avg `0.0171` n `7`; equity avg `-0.0133` n `42`; fx avg `-0.0051` n `4`; index avg `-0.0238` n `9`; metal avg `0.0192` n `7`; unknown avg `0.0443` n `313`
- 4h: commodity avg `0.0427` n `7`; crypto_alt avg `0.5838` n `223`; crypto_major avg `0.3387` n `7`; equity avg `0.0363` n `42`; fx avg `0.0195` n `4`; index avg `-0.0442` n `9`; metal avg `0.0976` n `7`; unknown avg `0.257` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5766`, n `59`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5685`, n `55`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5659`, n `55`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5566`, n `59`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4922`, n `55`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.48`, n `55`, moderate_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4686`, n `59`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4667`, n `55`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4412`, n `59`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4359`, n `59`, moderate_sample_signal
