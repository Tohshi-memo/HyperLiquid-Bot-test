# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T04:15:17.749183+00:00`
- Correlation status: `ready`
- Asset price records: `40`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0121` n `7`; crypto_alt avg `-0.21` n `223`; crypto_major avg `-0.153` n `7`; equity avg `0.0215` n `42`; fx avg `-0.0034` n `4`; index avg `-0.0128` n `9`; metal avg `-0.0226` n `7`; unknown avg `-0.035` n `311`
- 1h: commodity avg `0.0093` n `7`; crypto_alt avg `-0.0816` n `223`; crypto_major avg `0.0136` n `7`; equity avg `0.1015` n `42`; fx avg `-0.0117` n `4`; index avg `-0.005` n `9`; metal avg `-0.0343` n `7`; unknown avg `-0.0033` n `311`
- 4h: commodity avg `-0.048` n `7`; crypto_alt avg `-0.0405` n `223`; crypto_major avg `0.0493` n `7`; equity avg `0.051` n `42`; fx avg `-0.0254` n `4`; index avg `-0.008` n `9`; metal avg `-0.0244` n `7`; unknown avg `0.0291` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6545`, n `36`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6312`, n `36`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5704`, n `36`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5401`, n `32`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5379`, n `32`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5367`, n `36`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.52`, n `36`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4932`, n `32`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4874`, n `36`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.484`, n `32`, moderate_sample_signal
