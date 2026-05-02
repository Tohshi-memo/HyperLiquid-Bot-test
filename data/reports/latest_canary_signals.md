# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T06:30:27.448518+00:00`
- Correlation status: `ready`
- Asset price records: `49`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `7`; crypto_alt avg `-0.0988` n `223`; crypto_major avg `-0.1155` n `7`; equity avg `-0.0082` n `42`; fx avg `0.0` n `4`; index avg `-0.0018` n `9`; metal avg `0.0117` n `7`; unknown avg `-0.1316` n `311`
- 1h: commodity avg `0.0058` n `7`; crypto_alt avg `0.0998` n `223`; crypto_major avg `-0.0706` n `7`; equity avg `0.103` n `42`; fx avg `-0.0154` n `4`; index avg `0.0077` n `9`; metal avg `0.0289` n `7`; unknown avg `-0.1731` n `311`
- 4h: commodity avg `0.0038` n `7`; crypto_alt avg `-0.3838` n `223`; crypto_major avg `-0.1425` n `7`; equity avg `-0.0019` n `42`; fx avg `-0.1232` n `4`; index avg `-0.0194` n `9`; metal avg `-0.0019` n `7`; unknown avg `-0.1664` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6506`, n `45`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6278`, n `45`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.576`, n `41`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5646`, n `45`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5586`, n `41`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5307`, n `45`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5045`, n `45`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4925`, n `41`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4873`, n `41`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.483`, n `41`, moderate_sample_signal
