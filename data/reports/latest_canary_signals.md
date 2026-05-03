# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T11:15:26.523987+00:00`
- Correlation status: `ready`
- Asset price records: `164`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0097` n `7`; crypto_alt avg `0.1757` n `223`; crypto_major avg `0.1265` n `7`; equity avg `0.0158` n `42`; fx avg `0.0029` n `4`; index avg `0.0037` n `9`; metal avg `-0.001` n `7`; unknown avg `0.0185` n `313`
- 1h: commodity avg `-0.0419` n `7`; crypto_alt avg `-0.1301` n `223`; crypto_major avg `-0.012` n `7`; equity avg `0.1826` n `42`; fx avg `0.0127` n `4`; index avg `-0.0138` n `9`; metal avg `0.0112` n `7`; unknown avg `-0.1581` n `313`
- 4h: commodity avg `-0.0579` n `7`; crypto_alt avg `0.1766` n `223`; crypto_major avg `0.1484` n `7`; equity avg `0.1352` n `42`; fx avg `0.0247` n `4`; index avg `-0.013` n `9`; metal avg `0.1117` n `7`; unknown avg `-0.2613` n `313`
- 24h: commodity avg `-0.3031` n `7`; crypto_alt avg `1.2536` n `223`; crypto_major avg `0.0561` n `7`; equity avg `0.3751` n `42`; fx avg `0.1532` n `4`; index avg `0.0433` n `9`; metal avg `0.1229` n `7`; unknown avg `-0.0079` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4138`, n `160`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4032`, n `160`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.3992`, n `160`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3854`, n `160`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3836`, n `156`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3788`, n `156`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3635`, n `156`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3555`, n `156`, moderate_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.3343`, n `160`, moderate_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.3256`, n `160`, moderate_sample_signal
