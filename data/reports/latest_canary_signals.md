# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T11:57:41.389370+00:00`
- Correlation status: `ready`
- Asset price records: `166`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0213` n `7`; crypto_alt avg `0.1581` n `223`; crypto_major avg `0.253` n `7`; equity avg `0.0147` n `42`; fx avg `-0.0066` n `4`; index avg `-0.0278` n `9`; metal avg `-0.0188` n `7`; unknown avg `0.4221` n `313`
- 1h: commodity avg `0.0538` n `7`; crypto_alt avg `0.0207` n `223`; crypto_major avg `0.1845` n `7`; equity avg `0.0872` n `42`; fx avg `0.0037` n `4`; index avg `-0.0039` n `9`; metal avg `0.0038` n `7`; unknown avg `0.2639` n `313`
- 4h: commodity avg `-0.0639` n `7`; crypto_alt avg `0.1412` n `223`; crypto_major avg `0.2858` n `7`; equity avg `0.097` n `42`; fx avg `0.0127` n `4`; index avg `-0.0028` n `9`; metal avg `0.086` n `7`; unknown avg `0.0919` n `313`
- 24h: commodity avg `-0.279` n `7`; crypto_alt avg `1.452` n `223`; crypto_major avg `0.4396` n `7`; equity avg `0.3243` n `42`; fx avg `0.1524` n `4`; index avg `0.0746` n `9`; metal avg `0.1304` n `7`; unknown avg `0.4834` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4119`, n `162`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `162`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3974`, n `162`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3855`, n `162`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3827`, n `158`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3776`, n `158`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3625`, n `158`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3547`, n `158`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3333`, n `162`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.327`, n `162`, moderate_sample_signal
