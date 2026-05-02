# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-02T01:45:20.477500+00:00`
- Correlation status: `ready`
- Asset price records: `30`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0189` n `7`; crypto_alt avg `-0.058` n `223`; crypto_major avg `0.0095` n `7`; equity avg `-0.0963` n `42`; fx avg `-0.0021` n `4`; index avg `-0.0302` n `9`; metal avg `0.0071` n `7`; unknown avg `-0.0051` n `311`
- 1h: commodity avg `-0.0436` n `7`; crypto_alt avg `0.1303` n `223`; crypto_major avg `0.0337` n `7`; equity avg `-0.0187` n `42`; fx avg `-0.0011` n `4`; index avg `0.0284` n `9`; metal avg `0.0131` n `7`; unknown avg `0.0426` n `311`
- 4h: commodity avg `0.2055` n `7`; crypto_alt avg `-0.1729` n `223`; crypto_major avg `-0.1266` n `7`; equity avg `0.3315` n `42`; fx avg `0.0233` n `4`; index avg `0.0039` n `9`; metal avg `-0.1169` n `7`; unknown avg `0.0232` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.6732`, n `26`, strong_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.6488`, n `26`, strong_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.5596`, n `26`, strong_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.5427`, n `26`, strong_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.5105`, n `26`, strong_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.4856`, n `26`, moderate_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.4797`, n `26`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.375`, n `26`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3556`, n `26`, moderate_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.2878`, n `26`, moderate_sample_signal
