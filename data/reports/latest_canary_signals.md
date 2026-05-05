# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-05T16:30:33.395055+00:00`
- Correlation status: `ready`
- Asset price records: `374`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0907` n `7`; crypto_alt avg `-0.0082` n `223`; crypto_major avg `-0.1156` n `7`; equity avg `-0.083` n `47`; fx avg `-0.0071` n `4`; index avg `-0.0177` n `6`; metal avg `-0.1785` n `7`; unknown avg `-0.252` n `313`
- 1h: commodity avg `0.1651` n `7`; crypto_alt avg `0.0315` n `223`; crypto_major avg `-0.2819` n `7`; equity avg `-0.2605` n `47`; fx avg `0.001` n `4`; index avg `0.026` n `6`; metal avg `-0.4754` n `7`; unknown avg `0.1484` n `313`
- 4h: commodity avg `-0.4152` n `7`; crypto_alt avg `-0.2303` n `223`; crypto_major avg `0.074` n `7`; equity avg `0.2387` n `47`; fx avg `-0.1352` n `4`; index avg `0.7232` n `6`; metal avg `-0.6631` n `7`; unknown avg `0.075` n `312`
- 24h: commodity avg `-1.3476` n `7`; crypto_alt avg `1.6523` n `223`; crypto_major avg `1.8821` n `7`; equity avg `1.3985` n `47`; fx avg `-0.0511` n `4`; index avg `1.1891` n `6`; metal avg `0.9817` n `7`; unknown avg `0.7823` n `310`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2073`, n `370`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2003`, n `370`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1335`, n `370`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1294`, n `370`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1076`, n `366`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `370`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1052`, n `370`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `370`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `370`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0993`, n `366`, weak_sample_signal
