# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T23:52:31.801932+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0046` n `13`; crypto_alt avg `0.0389` n `237`; crypto_major avg `-0.0055` n `8`; equity avg `0.106` n `154`; fx avg `0.0079` n `6`; index avg `0.0312` n `27`; metal avg `-0.0174` n `20`; unknown avg `0.115` n `1238`
- 1h: commodity avg `0.0214` n `13`; crypto_alt avg `0.4899` n `237`; crypto_major avg `0.3621` n `8`; equity avg `0.146` n `154`; fx avg `0.0065` n `6`; index avg `0.0566` n `27`; metal avg `-0.0306` n `20`; unknown avg `1.9471` n `1228`
- 4h: commodity avg `-0.0843` n `13`; crypto_alt avg `0.4094` n `237`; crypto_major avg `0.204` n `8`; equity avg `0.4351` n `154`; fx avg `-0.0213` n `6`; index avg `0.0995` n `27`; metal avg `-0.0204` n `20`; unknown avg `9.5923` n `1116`
- 24h: commodity avg `-0.0949` n `13`; crypto_alt avg `0.4289` n `237`; crypto_major avg `0.6356` n `8`; equity avg `1.1931` n `153`; fx avg `-0.0162` n `6`; index avg `0.0661` n `27`; metal avg `-0.0296` n `20`; unknown avg `757.7548` n `972`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2209`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1863`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
