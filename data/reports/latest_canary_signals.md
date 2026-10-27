# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T14:37:31.090283+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1474` n `13`; crypto_alt avg `0.3398` n `238`; crypto_major avg `0.3498` n `8`; equity avg `0.3442` n `154`; fx avg `-0.0166` n `6`; index avg `0.0687` n `27`; metal avg `0.0713` n `20`; unknown avg `0.0133` n `1238`
- 1h: commodity avg `-0.1636` n `13`; crypto_alt avg `0.27` n `238`; crypto_major avg `0.1358` n `8`; equity avg `0.2599` n `154`; fx avg `0.002` n `6`; index avg `0.023` n `27`; metal avg `0.1425` n `20`; unknown avg `0.0814` n `1164`
- 4h: commodity avg `-0.4398` n `13`; crypto_alt avg `1.1132` n `238`; crypto_major avg `1.1372` n `8`; equity avg `1.4617` n `154`; fx avg `0.0031` n `6`; index avg `0.1569` n `27`; metal avg `0.3975` n `20`; unknown avg `1.5847` n `1112`
- 24h: commodity avg `-0.1966` n `13`; crypto_alt avg `0.0225` n `237`; crypto_major avg `0.654` n `8`; equity avg `1.8996` n `154`; fx avg `-0.0411` n `6`; index avg `0.3302` n `27`; metal avg `0.0737` n `20`; unknown avg `388.094` n `1046`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2127`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1903`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
