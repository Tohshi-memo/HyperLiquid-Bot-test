# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T23:00:39.091397+00:00`
- Correlation status: `ready`
- Asset price records: `400`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4439` n `7`; crypto_alt avg `0.1868` n `223`; crypto_major avg `0.1866` n `7`; equity avg `0.3396` n `47`; fx avg `-0.0026` n `4`; index avg `0.19` n `6`; metal avg `0.5443` n `7`; unknown avg `0.0031` n `313`
- 1h: commodity avg `-0.4934` n `7`; crypto_alt avg `-0.2796` n `223`; crypto_major avg `-0.2634` n `7`; equity avg `0.536` n `47`; fx avg `0.0006` n `4`; index avg `0.2011` n `6`; metal avg `0.4744` n `7`; unknown avg `0.2666` n `313`
- 4h: commodity avg `-0.4738` n `7`; crypto_alt avg `0.5832` n `223`; crypto_major avg `0.2928` n `7`; equity avg `0.9257` n `47`; fx avg `0.1228` n `4`; index avg `0.3202` n `6`; metal avg `0.2724` n `7`; unknown avg `0.265` n `313`
- 24h: commodity avg `-1.5986` n `7`; crypto_alt avg `2.1957` n `223`; crypto_major avg `2.4715` n `7`; equity avg `3.2287` n `47`; fx avg `0.067` n `4`; index avg `1.9221` n `6`; metal avg `1.203` n `7`; unknown avg `2.5308` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2049`, n `396`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1982`, n `396`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1303`, n `396`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1262`, n `396`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1109`, n `396`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1097`, n `392`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1073`, n `396`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1017`, n `392`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1012`, n `396`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1003`, n `396`, weak_sample_signal
