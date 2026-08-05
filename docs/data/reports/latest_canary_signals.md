# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T05:07:36.206981+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `12`; crypto_alt avg `0.1909` n `230`; crypto_major avg `0.3389` n `8`; equity avg `0.1902` n `108`; fx avg `0.0203` n `6`; index avg `0.0205` n `25`; metal avg `0.0143` n `20`; unknown avg `-0.2161` n `781`
- 1h: commodity avg `0.103` n `12`; crypto_alt avg `0.2719` n `230`; crypto_major avg `0.3504` n `8`; equity avg `0.1975` n `108`; fx avg `0.0856` n `6`; index avg `0.0168` n `25`; metal avg `-0.0454` n `20`; unknown avg `-0.2878` n `781`
- 4h: commodity avg `-0.1509` n `12`; crypto_alt avg `0.7662` n `230`; crypto_major avg `0.6951` n `8`; equity avg `0.879` n `108`; fx avg `0.0426` n `6`; index avg `0.0557` n `25`; metal avg `0.396` n `20`; unknown avg `-0.3183` n `781`
- 24h: commodity avg `-1.4519` n `12`; crypto_alt avg `0.4881` n `230`; crypto_major avg `0.6912` n `8`; equity avg `4.3623` n `108`; fx avg `0.0575` n `6`; index avg `0.8781` n `25`; metal avg `1.0358` n `20`; unknown avg `0.3765` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1426`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
