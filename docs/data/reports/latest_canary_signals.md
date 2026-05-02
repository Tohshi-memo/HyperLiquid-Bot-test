# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T03:30:22.875484+00:00`
- Correlation status: `ready`
- Asset price records: `37`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0071` n `7`; crypto_alt avg `0.1253` n `223`; crypto_major avg `0.1483` n `7`; equity avg `0.0423` n `42`; fx avg `-0.0003` n `4`; index avg `0.003` n `9`; metal avg `-0.0055` n `7`; unknown avg `0.046` n `311`
- 1h: commodity avg `0.0018` n `7`; crypto_alt avg `-0.0023` n `223`; crypto_major avg `0.1665` n `7`; equity avg `-0.0566` n `42`; fx avg `-0.0066` n `4`; index avg `0.0002` n `9`; metal avg `-0.0011` n `7`; unknown avg `0.0177` n `311`
- 4h: commodity avg `-0.0285` n `7`; crypto_alt avg `0.4265` n `223`; crypto_major avg `0.4257` n `7`; equity avg `0.0136` n `42`; fx avg `-0.0109` n `4`; index avg `-0.0121` n `9`; metal avg `0.0142` n `7`; unknown avg `0.1248` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6576`, n `33`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6341`, n `33`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5527`, n `33`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5432`, n `29`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.5363`, n `29`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5171`, n `33`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5124`, n `33`, strong_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.493`, n `29`, moderate_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4878`, n `33`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4841`, n `29`, moderate_sample_signal
