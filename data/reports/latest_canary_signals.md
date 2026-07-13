# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T01:07:26.223618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.0062` n `230`; crypto_major avg `0.0291` n `8`; equity avg `-0.242` n `92`; fx avg `0.0048` n `6`; index avg `-0.042` n `25`; metal avg `0.0016` n `20`; unknown avg `-0.0741` n `766`
- 1h: commodity avg `0.0905` n `12`; crypto_alt avg `-0.3607` n `230`; crypto_major avg `-0.3151` n `8`; equity avg `-1.0464` n `92`; fx avg `0.035` n `6`; index avg `-0.2563` n `25`; metal avg `-0.1508` n `20`; unknown avg `0.2194` n `766`
- 4h: commodity avg `-0.1415` n `12`; crypto_alt avg `-0.5185` n `230`; crypto_major avg `-0.3417` n `8`; equity avg `-1.1204` n `92`; fx avg `0.0553` n `6`; index avg `-0.2666` n `25`; metal avg `-0.2237` n `20`; unknown avg `-0.0023` n `765`
- 24h: commodity avg `-0.0402` n `12`; crypto_alt avg `-0.0448` n `230`; crypto_major avg `0.6968` n `8`; equity avg `-0.9626` n `92`; fx avg `0.0004` n `6`; index avg `-0.235` n `25`; metal avg `-0.2607` n `20`; unknown avg `0.3759` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1873`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1406`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
