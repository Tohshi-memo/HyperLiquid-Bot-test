# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-03T06:44:29.130725+00:00`
- Correlation status: `ready`
- Asset price records: `145`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0247` n `7`; crypto_alt avg `0.0983` n `223`; crypto_major avg `-0.016` n `7`; equity avg `-0.186` n `42`; fx avg `0.0005` n `4`; index avg `0.0075` n `9`; metal avg `0.0093` n `7`; unknown avg `0.0215` n `313`
- 1h: commodity avg `-0.0773` n `7`; crypto_alt avg `-0.0165` n `223`; crypto_major avg `-0.1637` n `7`; equity avg `-0.087` n `42`; fx avg `0.0035` n `4`; index avg `0.0459` n `9`; metal avg `0.0092` n `7`; unknown avg `-0.1559` n `311`
- 4h: commodity avg `-0.0264` n `7`; crypto_alt avg `0.2837` n `223`; crypto_major avg `0.0868` n `7`; equity avg `-0.1468` n `42`; fx avg `0.0048` n `4`; index avg `0.014` n `9`; metal avg `0.0395` n `7`; unknown avg `0.0443` n `311`
- 24h: commodity avg `-0.1952` n `7`; crypto_alt avg `1.2645` n `223`; crypto_major avg `-0.0592` n `7`; equity avg `0.3562` n `42`; fx avg `0.1317` n `4`; index avg `0.0426` n `9`; metal avg `0.0696` n `7`; unknown avg `0.3711` n `311`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.4419`, n `141`, moderate_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.4269`, n `141`, moderate_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.4044`, n `141`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.3985`, n `137`, moderate_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.3948`, n `137`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.3865`, n `141`, moderate_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.385`, n `137`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.3788`, n `137`, moderate_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.3558`, n `137`, moderate_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.3393`, n `137`, moderate_sample_signal
