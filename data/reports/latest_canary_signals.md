# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T00:30:21.912509+00:00`
- Correlation status: `ready`
- Asset price records: `121`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `7`; crypto_alt avg `0.315` n `223`; crypto_major avg `0.2286` n `7`; equity avg `0.0185` n `42`; fx avg `0.0021` n `4`; index avg `0.0139` n `9`; metal avg `-0.0193` n `7`; unknown avg `-0.0527` n `313`
- 1h: commodity avg `0.0141` n `7`; crypto_alt avg `-0.1522` n `223`; crypto_major avg `-0.225` n `7`; equity avg `0.0012` n `42`; fx avg `-0.0021` n `4`; index avg `0.0227` n `9`; metal avg `-0.0155` n `7`; unknown avg `0.1787` n `313`
- 4h: commodity avg `0.1095` n `7`; crypto_alt avg `-0.0798` n `223`; crypto_major avg `-0.0163` n `7`; equity avg `0.1674` n `42`; fx avg `0.0231` n `4`; index avg `0.0001` n `9`; metal avg `0.0013` n `7`; unknown avg `-0.0858` n `313`
- 24h: commodity avg `-0.1681` n `7`; crypto_alt avg `2.0291` n `223`; crypto_major avg `0.4528` n `7`; equity avg `0.7761` n `42`; fx avg `-0.0137` n `4`; index avg `0.0548` n `9`; metal avg `0.017` n `7`; unknown avg `0.3323` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4782`, n `117`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4616`, n `117`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4183`, n `113`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.416`, n `113`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.4074`, n `113`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.4057`, n `113`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4034`, n `117`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.4007`, n `113`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3855`, n `117`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3838`, n `113`, moderate_sample_signal
