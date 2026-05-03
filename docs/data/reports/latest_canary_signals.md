# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T14:30:24.539538+00:00`
- Correlation status: `ready`
- Asset price records: `177`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.01` n `7`; crypto_alt avg `-0.1061` n `223`; crypto_major avg `-0.0552` n `7`; equity avg `0.1123` n `42`; fx avg `-0.0016` n `4`; index avg `-0.005` n `9`; metal avg `0.0078` n `7`; unknown avg `0.0434` n `313`
- 1h: commodity avg `-0.0347` n `7`; crypto_alt avg `-0.0044` n `223`; crypto_major avg `0.0412` n `7`; equity avg `0.0605` n `42`; fx avg `-0.0026` n `4`; index avg `-0.0151` n `9`; metal avg `0.0237` n `7`; unknown avg `-0.0058` n `313`
- 4h: commodity avg `-0.0828` n `7`; crypto_alt avg `-0.0157` n `223`; crypto_major avg `0.3141` n `7`; equity avg `0.2045` n `42`; fx avg `0.0152` n `4`; index avg `-0.0279` n `9`; metal avg `0.0764` n `7`; unknown avg `-0.1565` n `313`
- 24h: commodity avg `-0.3028` n `7`; crypto_alt avg `0.4652` n `223`; crypto_major avg `0.1495` n `7`; equity avg `0.457` n `42`; fx avg `0.1591` n `4`; index avg `0.0199` n `9`; metal avg `0.2125` n `7`; unknown avg `-0.0905` n `311`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4031`, n `173`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3853`, n `173`, moderate_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.3844`, n `173`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3793`, n `169`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3744`, n `169`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3707`, n `173`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3557`, n `169`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3463`, n `169`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3224`, n `173`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3057`, n `173`, moderate_sample_signal
