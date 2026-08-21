# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T04:37:25.355787+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0068` n `12`; crypto_alt avg `0.1127` n `230`; crypto_major avg `-0.0336` n `8`; equity avg `-0.0433` n `121`; fx avg `0.0019` n `6`; index avg `-0.0182` n `25`; metal avg `-0.0091` n `20`; unknown avg `0.015` n `793`
- 1h: commodity avg `-0.0092` n `12`; crypto_alt avg `0.2542` n `230`; crypto_major avg `0.1918` n `8`; equity avg `-0.2034` n `121`; fx avg `-0.024` n `6`; index avg `-0.0505` n `25`; metal avg `0.0699` n `20`; unknown avg `0.0902` n `793`
- 4h: commodity avg `0.0255` n `12`; crypto_alt avg `1.0923` n `230`; crypto_major avg `1.1387` n `8`; equity avg `0.3505` n `121`; fx avg `-0.0262` n `6`; index avg `0.067` n `25`; metal avg `0.3012` n `20`; unknown avg `-0.0906` n `793`
- 24h: commodity avg `0.3043` n `12`; crypto_alt avg `5.8844` n `230`; crypto_major avg `7.1412` n `8`; equity avg `-0.7052` n `121`; fx avg `-0.0327` n `6`; index avg `-0.1398` n `25`; metal avg `0.5812` n `20`; unknown avg `2.6116` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2126`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0925`, n `668`, weak_sample_signal
