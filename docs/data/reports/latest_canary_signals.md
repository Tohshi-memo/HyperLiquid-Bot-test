# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T00:00:31.381696+00:00`
- Correlation status: `ready`
- Asset price records: `119`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `7`; crypto_alt avg `-0.0137` n `223`; crypto_major avg `-0.0454` n `7`; equity avg `-0.0605` n `42`; fx avg `0.0021` n `4`; index avg `0.0003` n `9`; metal avg `-0.0049` n `7`; unknown avg `0.1256` n `313`
- 1h: commodity avg `0.0079` n `7`; crypto_alt avg `0.1234` n `223`; crypto_major avg `-0.0151` n `7`; equity avg `-0.0234` n `42`; fx avg `0.0061` n `4`; index avg `0.0084` n `9`; metal avg `0.0033` n `7`; unknown avg `0.0018` n `313`
- 4h: commodity avg `0.0725` n `7`; crypto_alt avg `0.0741` n `223`; crypto_major avg `-0.0022` n `7`; equity avg `0.2069` n `42`; fx avg `0.034` n `4`; index avg `-0.0165` n `9`; metal avg `0.0071` n `7`; unknown avg `0.1246` n `313`
- 24h: commodity avg `-0.1896` n `7`; crypto_alt avg `2.2081` n `223`; crypto_major avg `0.5066` n `7`; equity avg `0.7915` n `42`; fx avg `0.0001` n `4`; index avg `0.0326` n `9`; metal avg `0.032` n `7`; unknown avg `0.3895` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4845`, n `115`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4677`, n `115`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.4398`, n `111`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4167`, n `111`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4146`, n `111`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.407`, n `111`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4033`, n `115`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4017`, n `111`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `115`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3823`, n `111`, moderate_sample_signal
