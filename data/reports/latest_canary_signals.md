# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T04:15:20.136609+00:00`
- Correlation status: `ready`
- Asset price records: `136`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0135` n `7`; crypto_alt avg `-0.0225` n `223`; crypto_major avg `-0.0034` n `7`; equity avg `-0.0148` n `42`; fx avg `-0.0008` n `4`; index avg `0.0187` n `9`; metal avg `-0.0005` n `7`; unknown avg `-0.0007` n `313`
- 1h: commodity avg `0.0315` n `7`; crypto_alt avg `0.1463` n `223`; crypto_major avg `0.0872` n `7`; equity avg `0.0237` n `42`; fx avg `0.0005` n `4`; index avg `0.0204` n `9`; metal avg `-0.0032` n `7`; unknown avg `0.0083` n `313`
- 4h: commodity avg `0.0512` n `7`; crypto_alt avg `-0.8813` n `223`; crypto_major avg `-0.391` n `7`; equity avg `-0.0474` n `42`; fx avg `0.0037` n `4`; index avg `-0.0129` n `9`; metal avg `0.0108` n `7`; unknown avg `-0.1156` n `313`
- 24h: commodity avg `-0.1029` n `7`; crypto_alt avg `0.8354` n `223`; crypto_major avg `-0.1898` n `7`; equity avg `0.5747` n `42`; fx avg `0.0229` n `4`; index avg `0.0258` n `9`; metal avg `0.0776` n `7`; unknown avg `0.119` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4466`, n `132`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4315`, n `132`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.4133`, n `128`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.4108`, n `128`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.4057`, n `132`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.404`, n `132`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3997`, n `132`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3986`, n `128`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3935`, n `128`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.393`, n `132`, moderate_sample_signal
