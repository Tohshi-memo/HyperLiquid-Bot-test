# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T15:07:29.005632+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0043` n `13`; crypto_alt avg `0.0047` n `238`; crypto_major avg `-0.0053` n `8`; equity avg `0.0484` n `154`; fx avg `-0.0059` n `6`; index avg `0.0458` n `27`; metal avg `0.036` n `20`; unknown avg `0.0735` n `1232`
- 1h: commodity avg `-0.2069` n `13`; crypto_alt avg `0.2947` n `238`; crypto_major avg `0.1832` n `8`; equity avg `0.4728` n `154`; fx avg `-0.0367` n `6`; index avg `0.1278` n `27`; metal avg `0.1589` n `20`; unknown avg `0.4098` n `1228`
- 4h: commodity avg `-0.1279` n `13`; crypto_alt avg `0.3554` n `238`; crypto_major avg `0.5351` n `8`; equity avg `0.9067` n `154`; fx avg `0.0042` n `6`; index avg `0.1043` n `27`; metal avg `0.362` n `20`; unknown avg `0.006` n `1136`
- 24h: commodity avg `-0.4049` n `13`; crypto_alt avg `-0.872` n `237`; crypto_major avg `-0.0712` n `8`; equity avg `0.8653` n `154`; fx avg `-0.0709` n `6`; index avg `0.2655` n `27`; metal avg `0.0232` n `20`; unknown avg `383.004` n `1058`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
