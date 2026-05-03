# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T07:00:28.118131+00:00`
- Correlation status: `ready`
- Asset price records: `147`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `7`; crypto_alt avg `0.1601` n `223`; crypto_major avg `0.1671` n `7`; equity avg `-0.0207` n `42`; fx avg `0.0019` n `4`; index avg `0.0265` n `9`; metal avg `0.0077` n `7`; unknown avg `0.2436` n `313`
- 1h: commodity avg `-0.0763` n `7`; crypto_alt avg `0.1803` n `223`; crypto_major avg `0.0659` n `7`; equity avg `-0.163` n `42`; fx avg `0.0029` n `4`; index avg `-0.0009` n `9`; metal avg `0.0147` n `7`; unknown avg `0.2044` n `313`
- 4h: commodity avg `-0.0276` n `7`; crypto_alt avg `0.3633` n `223`; crypto_major avg `0.154` n `7`; equity avg `-0.1848` n `42`; fx avg `0.0058` n `4`; index avg `0.009` n `9`; metal avg `0.0389` n `7`; unknown avg `0.2634` n `311`
- 24h: commodity avg `-0.2008` n `7`; crypto_alt avg `1.2105` n `223`; crypto_major avg `-0.2223` n `7`; equity avg `0.1971` n `42`; fx avg `0.1657` n `4`; index avg `0.0191` n `9`; metal avg `0.065` n `7`; unknown avg `0.4345` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4413`, n `143`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4262`, n `143`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4044`, n `143`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3984`, n `139`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3947`, n `139`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3865`, n `143`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3759`, n `139`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3685`, n `139`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3373`, n `139`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3277`, n `143`, moderate_sample_signal
