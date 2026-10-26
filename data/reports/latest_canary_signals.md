# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T20:52:34.284430+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0343` n `13`; crypto_alt avg `-0.0801` n `237`; crypto_major avg `-0.0555` n `8`; equity avg `-0.0337` n `154`; fx avg `-0.0016` n `6`; index avg `0.0013` n `27`; metal avg `0.0082` n `20`; unknown avg `1.8314` n `1236`
- 1h: commodity avg `-0.0891` n `13`; crypto_alt avg `-0.1474` n `237`; crypto_major avg `-0.2912` n `8`; equity avg `0.0648` n `154`; fx avg `-0.0209` n `6`; index avg `0.0072` n `27`; metal avg `0.006` n `20`; unknown avg `10.3423` n `1142`
- 4h: commodity avg `-0.4235` n `13`; crypto_alt avg `-0.3103` n `237`; crypto_major avg `-0.2255` n `8`; equity avg `-0.0247` n `154`; fx avg `-0.0401` n `6`; index avg `0.0081` n `27`; metal avg `-0.052` n `20`; unknown avg `9.5788` n `1142`
- 24h: commodity avg `-0.3509` n `13`; crypto_alt avg `-0.649` n `237`; crypto_major avg `-0.3982` n `8`; equity avg `0.4391` n `153`; fx avg `-0.0026` n `6`; index avg `-0.1076` n `27`; metal avg `0.0141` n `20`; unknown avg `703.1924` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.213`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
