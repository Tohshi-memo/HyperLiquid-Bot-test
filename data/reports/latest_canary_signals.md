# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-12T16:32:09.543399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0143` n `12`; crypto_alt avg `-0.031` n `230`; crypto_major avg `0.007` n `8`; equity avg `0.0309` n `92`; fx avg `0.0012` n `6`; index avg `0.0062` n `25`; metal avg `-0.0019` n `20`; unknown avg `-0.0065` n `759`
- 1h: commodity avg `0.0593` n `12`; crypto_alt avg `-0.0351` n `230`; crypto_major avg `0.1065` n `8`; equity avg `-0.0317` n `92`; fx avg `-0.0051` n `6`; index avg `0.0282` n `25`; metal avg `-0.0156` n `20`; unknown avg `-0.0011` n `759`
- 4h: commodity avg `0.085` n `12`; crypto_alt avg `0.0861` n `230`; crypto_major avg `0.4932` n `8`; equity avg `-0.0168` n `92`; fx avg `-0.0009` n `6`; index avg `0.0612` n `25`; metal avg `-0.0217` n `20`; unknown avg `-0.0129` n `759`
- 24h: commodity avg `0.5191` n `12`; crypto_alt avg `-0.9898` n `230`; crypto_major avg `-0.2249` n `8`; equity avg `-0.073` n `92`; fx avg `0.0315` n `6`; index avg `-0.0741` n `25`; metal avg `-0.1077` n `20`; unknown avg `0.4631` n `741`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1644`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.134`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
