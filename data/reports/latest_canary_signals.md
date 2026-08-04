# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T22:07:30.678402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0204` n `12`; crypto_alt avg `-0.0322` n `230`; crypto_major avg `0.0039` n `8`; equity avg `0.1002` n `108`; fx avg `-0.007` n `6`; index avg `-0.0102` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.0064` n `781`
- 1h: commodity avg `-0.0431` n `12`; crypto_alt avg `-0.1249` n `230`; crypto_major avg `-0.1165` n `8`; equity avg `0.0765` n `108`; fx avg `-0.0125` n `6`; index avg `0.007` n `25`; metal avg `-0.0016` n `20`; unknown avg `0.016` n `781`
- 4h: commodity avg `-0.0761` n `12`; crypto_alt avg `0.0709` n `230`; crypto_major avg `-0.1151` n `8`; equity avg `-0.4572` n `108`; fx avg `0.0477` n `6`; index avg `-0.0338` n `25`; metal avg `-0.1062` n `20`; unknown avg `0.0136` n `781`
- 24h: commodity avg `-1.2374` n `12`; crypto_alt avg `0.065` n `230`; crypto_major avg `0.7464` n `8`; equity avg `3.0079` n `107`; fx avg `0.1026` n `6`; index avg `0.7018` n `25`; metal avg `0.9149` n `20`; unknown avg `0.4559` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1477`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1288`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
