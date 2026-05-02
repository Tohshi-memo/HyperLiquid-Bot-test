# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T09:00:29.226996+00:00`
- Correlation status: `ready`
- Asset price records: `59`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0054` n `7`; crypto_alt avg `0.1044` n `223`; crypto_major avg `-0.0093` n `7`; equity avg `-0.1629` n `42`; fx avg `-0.0178` n `4`; index avg `0.0002` n `9`; metal avg `0.003` n `7`; unknown avg `0.0618` n `313`
- 1h: commodity avg `0.0286` n `7`; crypto_alt avg `0.1349` n `223`; crypto_major avg `0.1677` n `7`; equity avg `-0.0701` n `42`; fx avg `0.0389` n `4`; index avg `0.0227` n `9`; metal avg `0.0128` n `7`; unknown avg `0.1329` n `313`
- 4h: commodity avg `0.0392` n `7`; crypto_alt avg `0.4099` n `223`; crypto_major avg `0.2576` n `7`; equity avg `0.2034` n `42`; fx avg `-0.0802` n `4`; index avg `-0.0085` n `9`; metal avg `0.0769` n `7`; unknown avg `0.1913` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.5873`, n `55`, strong_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.583`, n `51`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.5668`, n `55`, strong_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.5437`, n `51`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.4744`, n `55`, moderate_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.4651`, n `51`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.4482`, n `51`, moderate_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.4403`, n `55`, moderate_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.4394`, n `55`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.4368`, n `51`, moderate_sample_signal
