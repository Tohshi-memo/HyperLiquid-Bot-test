# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T12:52:24.200230+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0463` n `12`; crypto_alt avg `0.1578` n `230`; crypto_major avg `0.0442` n `8`; equity avg `-0.0543` n `92`; fx avg `-0.0031` n `6`; index avg `-0.0062` n `25`; metal avg `-0.0042` n `20`; unknown avg `0.0161` n `765`
- 1h: commodity avg `-0.0189` n `12`; crypto_alt avg `0.2028` n `230`; crypto_major avg `0.0292` n `8`; equity avg `-0.0616` n `92`; fx avg `-0.0042` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0065` n `20`; unknown avg `0.0093` n `765`
- 4h: commodity avg `0.0213` n `12`; crypto_alt avg `0.3381` n `230`; crypto_major avg `0.118` n `8`; equity avg `-0.0197` n `92`; fx avg `-0.0119` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0189` n `20`; unknown avg `-0.1879` n `761`
- 24h: commodity avg `-0.1642` n `12`; crypto_alt avg `0.3942` n `229`; crypto_major avg `-0.2052` n `8`; equity avg `-0.2727` n `92`; fx avg `-0.0865` n `6`; index avg `0.1258` n `25`; metal avg `0.1407` n `20`; unknown avg `2.8285` n `727`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1061`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0908`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
