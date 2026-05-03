# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T06:00:32.291691+00:00`
- Correlation status: `ready`
- Asset price records: `143`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `7`; crypto_alt avg `0.0704` n `223`; crypto_major avg `-0.0127` n `7`; equity avg `-0.0037` n `42`; fx avg `-0.0032` n `4`; index avg `0.0057` n `9`; metal avg `0.0094` n `7`; unknown avg `-0.1165` n `311`
- 1h: commodity avg `-0.0196` n `7`; crypto_alt avg `0.0478` n `223`; crypto_major avg `0.0289` n `7`; equity avg `0.0667` n `42`; fx avg `-0.0003` n `4`; index avg `0.0181` n `9`; metal avg `0.0137` n `7`; unknown avg `0.0877` n `311`
- 4h: commodity avg `-0.0015` n `7`; crypto_alt avg `-0.0761` n `223`; crypto_major avg `0.0073` n `7`; equity avg `-0.0542` n `42`; fx avg `0.0133` n `4`; index avg `-0.013` n `9`; metal avg `0.0395` n `7`; unknown avg `0.019` n `311`
- 24h: commodity avg `-0.1075` n `7`; crypto_alt avg `1.2446` n `223`; crypto_major avg `-0.0418` n `7`; equity avg `0.5096` n `42`; fx avg `0.1338` n `4`; index avg `0.0187` n `9`; metal avg `0.0937` n `7`; unknown avg `0.2534` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4426`, n `139`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4274`, n `139`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4069`, n `135`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4046`, n `135`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4043`, n `139`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3939`, n `135`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.389`, n `135`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3865`, n `139`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3597`, n `135`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3539`, n `139`, moderate_sample_signal
