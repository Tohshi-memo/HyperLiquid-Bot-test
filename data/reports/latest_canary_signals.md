# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T00:45:36.163849+00:00`
- Correlation status: `ready`
- Asset price records: `122`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0033` n `7`; crypto_alt avg `-0.1485` n `223`; crypto_major avg `-0.1312` n `7`; equity avg `-0.0278` n `42`; fx avg `-0.0008` n `4`; index avg `0.0065` n `9`; metal avg `0.0013` n `7`; unknown avg `-0.163` n `313`
- 1h: commodity avg `-0.0121` n `7`; crypto_alt avg `-0.3224` n `223`; crypto_major avg `-0.2374` n `7`; equity avg `-0.0625` n `42`; fx avg `-0.0008` n `4`; index avg `0.0229` n `9`; metal avg `-0.0132` n `7`; unknown avg `-0.082` n `313`
- 4h: commodity avg `0.0829` n `7`; crypto_alt avg `-0.1228` n `223`; crypto_major avg `-0.1613` n `7`; equity avg `0.0935` n `42`; fx avg `0.0263` n `4`; index avg `-0.0012` n `9`; metal avg `0.0047` n `7`; unknown avg `-0.1844` n `313`
- 24h: commodity avg `-0.2004` n `7`; crypto_alt avg `1.7241` n `223`; crypto_major avg `0.2184` n `7`; equity avg `0.7137` n `42`; fx avg `-0.0134` n `4`; index avg `0.0928` n `9`; metal avg `0.0356` n `7`; unknown avg `0.2025` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4761`, n `118`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4596`, n `118`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4188`, n `114`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4167`, n `114`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4059`, n `114`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4035`, n `118`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.401`, n `114`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3856`, n `118`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.3848`, n `114`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3848`, n `114`, moderate_sample_signal
