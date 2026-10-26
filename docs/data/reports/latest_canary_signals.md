# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T19:07:31.454425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0624` n `13`; crypto_alt avg `0.074` n `237`; crypto_major avg `0.0397` n `8`; equity avg `-0.1111` n `154`; fx avg `-0.007` n `6`; index avg `-0.0172` n `27`; metal avg `-0.0505` n `20`; unknown avg `2.0838` n `1236`
- 1h: commodity avg `0.0402` n `13`; crypto_alt avg `-0.6789` n `237`; crypto_major avg `-0.5314` n `8`; equity avg `-0.4103` n `154`; fx avg `-0.0143` n `6`; index avg `-0.0675` n `27`; metal avg `-0.1076` n `20`; unknown avg `2.1437` n `1236`
- 4h: commodity avg `0.0754` n `13`; crypto_alt avg `-1.2487` n `237`; crypto_major avg `-0.6179` n `8`; equity avg `-0.0914` n `154`; fx avg `-0.0229` n `6`; index avg `-0.0803` n `27`; metal avg `-0.189` n `20`; unknown avg `1.5044` n `1224`
- 24h: commodity avg `-0.1722` n `13`; crypto_alt avg `-0.7359` n `237`; crypto_major avg `-0.1927` n `8`; equity avg `0.5726` n `153`; fx avg `0.0481` n `6`; index avg `-0.1135` n `27`; metal avg `-0.0189` n `20`; unknown avg `778.0013` n `924`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
