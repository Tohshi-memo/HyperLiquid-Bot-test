# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T19:52:34.767243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.041` n `12`; crypto_alt avg `0.0188` n `230`; crypto_major avg `-0.0217` n `8`; equity avg `-0.1295` n `107`; fx avg `-0.0053` n `6`; index avg `-0.0143` n `25`; metal avg `-0.0219` n `20`; unknown avg `-0.0083` n `782`
- 1h: commodity avg `0.0365` n `12`; crypto_alt avg `0.0594` n `230`; crypto_major avg `-0.0047` n `8`; equity avg `-0.1129` n `107`; fx avg `0.0138` n `6`; index avg `0.0091` n `25`; metal avg `-0.049` n `20`; unknown avg `-0.0787` n `782`
- 4h: commodity avg `0.0918` n `12`; crypto_alt avg `0.2909` n `230`; crypto_major avg `0.0613` n `8`; equity avg `0.343` n `107`; fx avg `0.0702` n `6`; index avg `0.1714` n `25`; metal avg `-0.0666` n `20`; unknown avg `-0.2075` n `782`
- 24h: commodity avg `-1.1563` n `12`; crypto_alt avg `0.0389` n `230`; crypto_major avg `0.393` n `8`; equity avg `3.7119` n `107`; fx avg `0.1461` n `6`; index avg `0.8298` n `25`; metal avg `0.9047` n `20`; unknown avg `0.4767` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1529`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1058`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
