# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T23:22:48.428950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0249` n `13`; crypto_alt avg `0.3035` n `237`; crypto_major avg `0.2454` n `8`; equity avg `0.1355` n `154`; fx avg `0.0009` n `6`; index avg `0.0322` n `27`; metal avg `0.0165` n `20`; unknown avg `0.0722` n `1238`
- 1h: commodity avg `0.006` n `13`; crypto_alt avg `-0.0021` n `237`; crypto_major avg `-0.0028` n `8`; equity avg `-0.2145` n `154`; fx avg `-0.0225` n `6`; index avg `-0.021` n `27`; metal avg `-0.03` n `20`; unknown avg `-0.3018` n `1218`
- 4h: commodity avg `-0.1957` n `13`; crypto_alt avg `-0.4359` n `237`; crypto_major avg `-0.4883` n `8`; equity avg `-0.2399` n `154`; fx avg `-0.0236` n `6`; index avg `-0.0178` n `27`; metal avg `-0.0152` n `20`; unknown avg `9.2833` n `1116`
- 24h: commodity avg `-0.1391` n `13`; crypto_alt avg `-0.3822` n `237`; crypto_major avg `-0.1597` n `8`; equity avg `0.5594` n `153`; fx avg `-0.0058` n `6`; index avg `-0.1071` n `27`; metal avg `-0.049` n `20`; unknown avg `756.151` n `972`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1833`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.177`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
