# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-26T20:07:28.195719+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `-0.0503` n `237`; crypto_major avg `-0.038` n `8`; equity avg `-0.0748` n `154`; fx avg `-0.0074` n `6`; index avg `-0.0034` n `27`; metal avg `-0.0119` n `20`; unknown avg `9.1851` n `1210`
- 1h: commodity avg `-0.0774` n `13`; crypto_alt avg `-0.0555` n `237`; crypto_major avg `-0.0627` n `8`; equity avg `-0.3129` n `154`; fx avg `-0.0033` n `6`; index avg `-0.013` n `27`; metal avg `0.017` n `20`; unknown avg `115.2041` n `1210`
- 4h: commodity avg `-0.3452` n `13`; crypto_alt avg `-0.8108` n `237`; crypto_major avg `-0.4044` n `8`; equity avg `-0.3141` n `154`; fx avg `-0.0312` n `6`; index avg `-0.0434` n `27`; metal avg `-0.1065` n `20`; unknown avg `1.5211` n `1210`
- 24h: commodity avg `-0.3081` n `13`; crypto_alt avg `-0.7589` n `237`; crypto_major avg `-0.2925` n `8`; equity avg `0.2638` n `153`; fx avg `0.0176` n `6`; index avg `-0.1199` n `27`; metal avg `0.0081` n `20`; unknown avg `756.2645` n `954`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1888`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1811`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
