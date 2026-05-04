# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-04T16:21:07.400472+00:00`
- Correlation status: `ready`
- Asset price records: `279`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0056` n `7`; crypto_alt avg `0.3849` n `223`; crypto_major avg `0.4383` n `7`; equity avg `-0.1941` n `42`; fx avg `-0.0136` n `4`; index avg `-0.0679` n `9`; metal avg `-0.1002` n `7`; unknown avg `0.3474` n `314`
- 1h: commodity avg `0.3184` n `7`; crypto_alt avg `-0.2054` n `223`; crypto_major avg `-0.2754` n `7`; equity avg `-1.089` n `42`; fx avg `-0.0113` n `4`; index avg `-0.3888` n `9`; metal avg `-0.5831` n `7`; unknown avg `-0.0923` n `314`
- 4h: commodity avg `0.9165` n `7`; crypto_alt avg `0.7641` n `223`; crypto_major avg `0.7667` n `7`; equity avg `-0.2662` n `42`; fx avg `-0.0009` n `4`; index avg `0.1977` n `9`; metal avg `-0.5194` n `7`; unknown avg `-0.3615` n `314`
- 24h: commodity avg `2.0272` n `7`; crypto_alt avg `1.9502` n `223`; crypto_major avg `1.3388` n `7`; equity avg `0.0002` n `42`; fx avg `-0.0894` n `4`; index avg `0.6101` n `9`; metal avg `-2.2336` n `7`; unknown avg `-0.6337` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2412`, n `276`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2354`, n `276`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1562`, n `272`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1559`, n `272`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1522`, n `276`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1516`, n `276`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.149`, n `272`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1484`, n `272`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1466`, n `276`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1424`, n `272`, weak_sample_signal
