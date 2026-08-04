# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T15:07:31.824990+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0483` n `12`; crypto_alt avg `0.0942` n `230`; crypto_major avg `0.095` n `8`; equity avg `0.2743` n `107`; fx avg `-0.0062` n `6`; index avg `0.0335` n `25`; metal avg `0.0341` n `20`; unknown avg `-0.0128` n `782`
- 1h: commodity avg `0.1552` n `12`; crypto_alt avg `0.1312` n `230`; crypto_major avg `0.3607` n `8`; equity avg `0.5276` n `107`; fx avg `0.0392` n `6`; index avg `0.0502` n `25`; metal avg `0.0438` n `20`; unknown avg `0.0262` n `782`
- 4h: commodity avg `-0.9704` n `12`; crypto_alt avg `-0.1451` n `230`; crypto_major avg `0.3209` n `8`; equity avg `1.2717` n `107`; fx avg `-0.05` n `6`; index avg `0.3442` n `25`; metal avg `0.5757` n `20`; unknown avg `-0.1901` n `781`
- 24h: commodity avg `-0.8608` n `12`; crypto_alt avg `-0.0878` n `230`; crypto_major avg `0.5031` n `8`; equity avg `3.8461` n `107`; fx avg `0.0869` n `6`; index avg `0.6904` n `25`; metal avg `1.1219` n `20`; unknown avg `0.5962` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
