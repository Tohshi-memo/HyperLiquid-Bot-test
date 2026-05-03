# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T06:45:20.414738+00:00`
- Correlation status: `ready`
- Asset price records: `146`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.003` n `7`; crypto_alt avg `0.0128` n `223`; crypto_major avg `0.0008` n `7`; equity avg `-0.0111` n `42`; fx avg `-0.0016` n `4`; index avg `-0.0416` n `9`; metal avg `-0.0001` n `7`; unknown avg `0.0021` n `313`
- 1h: commodity avg `-0.0736` n `7`; crypto_alt avg `0.0905` n `223`; crypto_major avg `-0.1136` n `7`; equity avg `-0.145` n `42`; fx avg `-0.0021` n `4`; index avg `-0.0216` n `9`; metal avg `0.0164` n `7`; unknown avg `-0.1525` n `311`
- 4h: commodity avg `-0.0429` n `7`; crypto_alt avg `0.1948` n `223`; crypto_major avg `0.0344` n `7`; equity avg `-0.1561` n `42`; fx avg `0.0032` n `4`; index avg `-0.0281` n `9`; metal avg `0.0376` n `7`; unknown avg `0.0011` n `311`
- 24h: commodity avg `-0.2034` n `7`; crypto_alt avg `1.1857` n `223`; crypto_major avg `-0.1867` n `7`; equity avg `0.2692` n `42`; fx avg `0.1582` n `4`; index avg `0.0019` n `9`; metal avg `0.0627` n `7`; unknown avg `0.2318` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4419`, n `142`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4268`, n `142`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4044`, n `142`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3989`, n `138`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3953`, n `138`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3865`, n `142`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.3805`, n `138`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3737`, n `138`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.347`, n `138`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.3315`, n `138`, moderate_sample_signal
