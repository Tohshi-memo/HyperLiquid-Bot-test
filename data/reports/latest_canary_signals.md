# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T11:45:33.182883+00:00`
- Correlation status: `ready`
- Asset price records: `166`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0232` n `7`; crypto_alt avg `0.3008` n `223`; crypto_major avg `0.3119` n `7`; equity avg `0.0051` n `42`; fx avg `-0.0053` n `4`; index avg `-0.0267` n `9`; metal avg `-0.0072` n `7`; unknown avg `0.0884` n `313`
- 1h: commodity avg `0.0557` n `7`; crypto_alt avg `0.161` n `223`; crypto_major avg `0.2435` n `7`; equity avg `0.0775` n `42`; fx avg `0.005` n `4`; index avg `-0.0028` n `9`; metal avg `0.0154` n `7`; unknown avg `-0.0684` n `313`
- 4h: commodity avg `-0.0621` n `7`; crypto_alt avg `0.2915` n `223`; crypto_major avg `0.3448` n `7`; equity avg `0.0877` n `42`; fx avg `0.0141` n `4`; index avg `-0.0017` n `9`; metal avg `0.0976` n `7`; unknown avg `-0.2388` n `313`
- 24h: commodity avg `-0.2771` n `7`; crypto_alt avg `1.5999` n `223`; crypto_major avg `0.4984` n `7`; equity avg `0.3151` n `42`; fx avg `0.1538` n `4`; index avg `0.0757` n `9`; metal avg `0.1421` n `7`; unknown avg `0.1599` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4107`, n `162`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `162`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3962`, n `162`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `162`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3826`, n `158`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3776`, n `158`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3625`, n `158`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3547`, n `158`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3328`, n `162`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3246`, n `162`, moderate_sample_signal
