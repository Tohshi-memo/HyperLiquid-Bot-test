# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T06:15:17.982690+00:00`
- Correlation status: `ready`
- Asset price records: `144`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0459` n `7`; crypto_alt avg `-0.0895` n `223`; crypto_major avg `-0.0857` n `7`; equity avg `0.0535` n `42`; fx avg `0.0021` n `4`; index avg `0.0068` n `9`; metal avg `-0.0022` n `7`; unknown avg `-0.058` n `313`
- 1h: commodity avg `-0.0641` n `7`; crypto_alt avg `-0.1772` n `223`; crypto_major avg `-0.135` n `7`; equity avg `0.1426` n `42`; fx avg `0.0051` n `4`; index avg `0.0504` n `9`; metal avg `0.0075` n `7`; unknown avg `-0.184` n `311`
- 4h: commodity avg `-0.0068` n `7`; crypto_alt avg `0.0283` n `223`; crypto_major avg `-0.0659` n `7`; equity avg `0.0174` n `42`; fx avg `0.0042` n `4`; index avg `0.0019` n `9`; metal avg `0.0213` n `7`; unknown avg `-0.003` n `311`
- 24h: commodity avg `-0.1735` n `7`; crypto_alt avg `1.0583` n `223`; crypto_major avg `-0.1585` n `7`; equity avg `0.5545` n `42`; fx avg `0.1311` n `4`; index avg `0.0333` n `9`; metal avg `0.072` n `7`; unknown avg `0.171` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4424`, n `140`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4273`, n `140`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4043`, n `140`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4024`, n `136`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3994`, n `136`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3899`, n `136`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3865`, n `140`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3844`, n `136`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3614`, n `136`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.3439`, n `136`, moderate_sample_signal
