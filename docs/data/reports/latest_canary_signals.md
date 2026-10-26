# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T16:52:27.858807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0604` n `13`; crypto_alt avg `0.1396` n `237`; crypto_major avg `0.148` n `8`; equity avg `-0.0667` n `154`; fx avg `-0.0001` n `6`; index avg `-0.028` n `27`; metal avg `-0.0104` n `20`; unknown avg `0.0108` n `1238`
- 1h: commodity avg `0.0361` n `13`; crypto_alt avg `-0.8194` n `237`; crypto_major avg `-0.579` n `8`; equity avg `-0.2175` n `154`; fx avg `0.0017` n `6`; index avg `-0.0426` n `27`; metal avg `-0.0412` n `20`; unknown avg `-0.0019` n `1232`
- 4h: commodity avg `0.3891` n `13`; crypto_alt avg `-0.2532` n `237`; crypto_major avg `-0.2046` n `8`; equity avg `0.7312` n `153`; fx avg `0.0211` n `6`; index avg `0.1113` n `27`; metal avg `-0.0027` n `20`; unknown avg `598.6175` n `1154`
- 24h: commodity avg `0.0615` n `13`; crypto_alt avg `-0.4304` n `237`; crypto_major avg `-0.2696` n `8`; equity avg `0.5429` n `153`; fx avg `0.0665` n `6`; index avg `-0.0991` n `27`; metal avg `0.0838` n `20`; unknown avg `788.6287` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2251`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1869`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1115`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
