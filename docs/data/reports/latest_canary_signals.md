# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T17:37:36.891413+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `13`; crypto_alt avg `-0.1014` n `237`; crypto_major avg `0.0188` n `8`; equity avg `-0.1947` n `154`; fx avg `-0.0012` n `6`; index avg `-0.0442` n `27`; metal avg `-0.0434` n `20`; unknown avg `0.6438` n `1238`
- 1h: commodity avg `-0.2685` n `13`; crypto_alt avg `0.7855` n `237`; crypto_major avg `0.7936` n `8`; equity avg `0.2589` n `154`; fx avg `-0.0045` n `6`; index avg `0.0204` n `27`; metal avg `0.0263` n `20`; unknown avg `0.2422` n `1238`
- 4h: commodity avg `0.1574` n `13`; crypto_alt avg `0.4828` n `237`; crypto_major avg `0.7474` n `8`; equity avg `1.5215` n `153`; fx avg `0.0242` n `6`; index avg `0.1439` n `27`; metal avg `0.1255` n `20`; unknown avg `593.9845` n `1166`
- 24h: commodity avg `-0.1705` n `13`; crypto_alt avg `-0.2048` n `237`; crypto_major avg `0.1659` n `8`; equity avg `0.8016` n `153`; fx avg `0.0573` n `6`; index avg `-0.0596` n `27`; metal avg `0.1002` n `20`; unknown avg `780.3757` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2228`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.19`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1862`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.121`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.116`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
