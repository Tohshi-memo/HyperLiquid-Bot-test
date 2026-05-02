# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T03:15:19.949443+00:00`
- Correlation status: `ready`
- Asset price records: `36`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `7`; crypto_alt avg `-0.0365` n `223`; crypto_major avg `-0.1409` n `7`; equity avg `-0.0936` n `42`; fx avg `-0.0056` n `4`; index avg `0.0024` n `9`; metal avg `-0.0015` n `7`; unknown avg `-0.0242` n `311`
- 1h: commodity avg `-0.009` n `7`; crypto_alt avg `-0.1607` n `223`; crypto_major avg `-0.1012` n `7`; equity avg `-0.0679` n `42`; fx avg `-0.0122` n `4`; index avg `0.0036` n `9`; metal avg `0.0042` n `7`; unknown avg `-0.0568` n `311`
- 4h: commodity avg `-0.0225` n `7`; crypto_alt avg `0.0547` n `223`; crypto_major avg `0.1584` n `7`; equity avg `-0.029` n `42`; fx avg `0.0064` n `4`; index avg `-0.048` n `9`; metal avg `0.0141` n `7`; unknown avg `-0.0266` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6681`, n `32`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6442`, n `32`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.551`, n `32`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5346`, n `28`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5297`, n `28`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5172`, n `32`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5099`, n `32`, strong_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4878`, n `32`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.4819`, n `32`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.481`, n `28`, moderate_sample_signal
