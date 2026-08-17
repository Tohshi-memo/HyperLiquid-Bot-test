# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T19:52:30.390895+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0182` n `12`; crypto_alt avg `-0.0814` n `230`; crypto_major avg `-0.0565` n `8`; equity avg `-0.0649` n `114`; fx avg `-0.0013` n `6`; index avg `-0.0115` n `25`; metal avg `0.0016` n `20`; unknown avg `-0.0075` n `792`
- 1h: commodity avg `0.0659` n `12`; crypto_alt avg `-0.1764` n `230`; crypto_major avg `-0.1922` n `8`; equity avg `-0.2673` n `114`; fx avg `-0.0028` n `6`; index avg `-0.0379` n `25`; metal avg `0.0325` n `20`; unknown avg `0.1529` n `792`
- 4h: commodity avg `0.3723` n `12`; crypto_alt avg `-0.302` n `230`; crypto_major avg `-0.3319` n `8`; equity avg `-0.5737` n `114`; fx avg `-0.0036` n `6`; index avg `-0.1408` n `25`; metal avg `-0.1031` n `20`; unknown avg `0.2335` n `792`
- 24h: commodity avg `0.3538` n `12`; crypto_alt avg `-0.1584` n `230`; crypto_major avg `0.7532` n `8`; equity avg `1.0981` n `114`; fx avg `0.0223` n `6`; index avg `0.0551` n `25`; metal avg `0.1901` n `20`; unknown avg `0.2462` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.185`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1703`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1387`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
