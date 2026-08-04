# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T23:49:25.954353+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.013` n `12`; crypto_alt avg `-0.0589` n `230`; crypto_major avg `0.0244` n `8`; equity avg `0.1048` n `108`; fx avg `-0.0018` n `6`; index avg `0.0074` n `25`; metal avg `0.0247` n `20`; unknown avg `-0.0013` n `781`
- 1h: commodity avg `-0.0221` n `12`; crypto_alt avg `-0.1743` n `230`; crypto_major avg `-0.1161` n `8`; equity avg `0.25` n `108`; fx avg `0.004` n `6`; index avg `0.0175` n `25`; metal avg `-0.0536` n `20`; unknown avg `0.0016` n `781`
- 4h: commodity avg `-0.1209` n `12`; crypto_alt avg `-0.1929` n `230`; crypto_major avg `-0.3099` n `8`; equity avg `-0.138` n `108`; fx avg `0.0058` n `6`; index avg `-0.0462` n `25`; metal avg `-0.0288` n `20`; unknown avg `0.1845` n `781`
- 24h: commodity avg `-1.2907` n `12`; crypto_alt avg `0.0365` n `230`; crypto_major avg `0.6111` n `8`; equity avg `2.9972` n `107`; fx avg `0.0761` n `6`; index avg `0.6524` n `25`; metal avg `0.8376` n `20`; unknown avg `0.4121` n `764`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
