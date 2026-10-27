# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-27T06:13:15.209107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0595` n `13`; crypto_alt avg `-0.0749` n `237`; crypto_major avg `-0.0937` n `8`; equity avg `-0.0144` n `154`; fx avg `0.0069` n `6`; index avg `0.0135` n `27`; metal avg `-0.0183` n `20`; unknown avg `1.5484` n `1218`
- 1h: commodity avg `0.1004` n `13`; crypto_alt avg `0.0317` n `237`; crypto_major avg `-0.0164` n `8`; equity avg `-0.3415` n `154`; fx avg `0.0056` n `6`; index avg `-0.0848` n `27`; metal avg `-0.0534` n `20`; unknown avg `0.017` n `1216`
- 4h: commodity avg `0.072` n `13`; crypto_alt avg `-0.1252` n `237`; crypto_major avg `-0.3033` n `8`; equity avg `-1.1068` n `154`; fx avg `0.0047` n `6`; index avg `-0.0242` n `27`; metal avg `-0.1158` n `20`; unknown avg `199.1369` n `1198`
- 24h: commodity avg `0.1522` n `13`; crypto_alt avg `0.078` n `237`; crypto_major avg `0.1376` n `8`; equity avg `0.6751` n `153`; fx avg `-0.0376` n `6`; index avg `0.0823` n `27`; metal avg `-0.2013` n `20`; unknown avg `1113.2058` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2066`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1952`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1927`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1041`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
