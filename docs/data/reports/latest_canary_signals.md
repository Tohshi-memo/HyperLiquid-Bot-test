# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T02:15:19.452722+00:00`
- Correlation status: `ready`
- Asset price records: `32`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0065` n `7`; crypto_alt avg `-0.1238` n `223`; crypto_major avg `0.003` n `7`; equity avg `0.0316` n `42`; fx avg `-0.0103` n `4`; index avg `0.0151` n `9`; metal avg `-0.0002` n `7`; unknown avg `-0.0093` n `311`
- 1h: commodity avg `-0.0313` n `7`; crypto_alt avg `-0.0864` n `223`; crypto_major avg `-0.0472` n `7`; equity avg `0.105` n `42`; fx avg `-0.0111` n `4`; index avg `-0.022` n `9`; metal avg `0.0131` n `7`; unknown avg `0.0174` n `311`
- 4h: commodity avg `0.0463` n `7`; crypto_alt avg `-0.2597` n `223`; crypto_major avg `-0.1515` n `7`; equity avg `0.1571` n `42`; fx avg `0.0454` n `4`; index avg `-0.0928` n `9`; metal avg `-0.0029` n `7`; unknown avg `-0.0544` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6698`, n `28`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6457`, n `28`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5699`, n `24`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5539`, n `24`, strong_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.5482`, n `24`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5333`, n `28`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5261`, n `28`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4845`, n `28`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.481`, n `28`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.4752`, n `28`, moderate_sample_signal
