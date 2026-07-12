# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T06:07:26.512138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0488` n `12`; crypto_alt avg `-0.3969` n `230`; crypto_major avg `-0.2994` n `8`; equity avg `-0.0707` n `92`; fx avg `-0.0045` n `6`; index avg `-0.0064` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.1811` n `749`
- 1h: commodity avg `-0.0533` n `12`; crypto_alt avg `-0.544` n `230`; crypto_major avg `-0.4205` n `8`; equity avg `-0.0822` n `92`; fx avg `-0.0007` n `6`; index avg `-0.013` n `25`; metal avg `-0.0106` n `20`; unknown avg `-0.1508` n `749`
- 4h: commodity avg `-0.1538` n `12`; crypto_alt avg `-0.3552` n `230`; crypto_major avg `-0.449` n `8`; equity avg `-0.1052` n `92`; fx avg `-0.0034` n `6`; index avg `-0.0169` n `25`; metal avg `-0.0066` n `20`; unknown avg `-0.3374` n `749`
- 24h: commodity avg `0.4178` n `12`; crypto_alt avg `-0.8038` n `230`; crypto_major avg `-0.7842` n `8`; equity avg `-0.0474` n `92`; fx avg `-0.0141` n `6`; index avg `-0.0955` n `25`; metal avg `-0.0976` n `20`; unknown avg `-0.0655` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1794`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1267`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.105`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
