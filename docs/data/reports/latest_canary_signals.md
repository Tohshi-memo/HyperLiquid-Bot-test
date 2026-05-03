# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T08:45:31.502887+00:00`
- Correlation status: `ready`
- Asset price records: `154`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0154` n `7`; crypto_alt avg `-0.0656` n `223`; crypto_major avg `0.0489` n `7`; equity avg `-0.1244` n `42`; fx avg `-0.0016` n `4`; index avg `0.002` n `9`; metal avg `0.0081` n `7`; unknown avg `0.0797` n `313`
- 1h: commodity avg `0.0161` n `7`; crypto_alt avg `-0.0078` n `223`; crypto_major avg `-0.0171` n `7`; equity avg `-0.1252` n `42`; fx avg `0.0037` n `4`; index avg `0.0011` n `9`; metal avg `0.0466` n `7`; unknown avg `-0.0813` n `313`
- 4h: commodity avg `-0.0658` n `7`; crypto_alt avg `0.4254` n `223`; crypto_major avg `0.2228` n `7`; equity avg `-0.2939` n `42`; fx avg `0.022` n `4`; index avg `0.0218` n `9`; metal avg `0.1086` n `7`; unknown avg `0.2732` n `311`
- 24h: commodity avg `-0.2025` n `7`; crypto_alt avg `1.4125` n `223`; crypto_major avg `-0.1508` n `7`; equity avg `0.0027` n `42`; fx avg `0.1091` n `4`; index avg `0.0718` n `9`; metal avg `0.1111` n `7`; unknown avg `0.1996` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.425`, n `150`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4102`, n `150`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4035`, n `150`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3881`, n `146`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3857`, n `150`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3827`, n `146`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3759`, n `146`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3683`, n `146`, moderate_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.3501`, n `150`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3477`, n `150`, moderate_sample_signal
