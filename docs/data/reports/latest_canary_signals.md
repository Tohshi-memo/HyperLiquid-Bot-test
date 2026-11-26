# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T02:37:33.246218+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0201` n `13`; crypto_alt avg `-0.1901` n `239`; crypto_major avg `-0.2558` n `8`; equity avg `0.0049` n `168`; fx avg `0.0004` n `6`; index avg `0.0055` n `27`; metal avg `0.1843` n `20`; unknown avg `-0.0515` n `1267`
- 1h: commodity avg `0.0087` n `13`; crypto_alt avg `0.2605` n `239`; crypto_major avg `0.3516` n `8`; equity avg `0.2873` n `168`; fx avg `-0.0183` n `6`; index avg `0.0139` n `27`; metal avg `0.49` n `20`; unknown avg `-0.2418` n `1265`
- 4h: commodity avg `0.0277` n `13`; crypto_alt avg `1.4248` n `239`; crypto_major avg `0.9519` n `8`; equity avg `1.4616` n `168`; fx avg `-0.0518` n `6`; index avg `0.1416` n `27`; metal avg `0.3452` n `20`; unknown avg `166.6277` n `1201`
- 24h: commodity avg `0.6139` n `13`; crypto_alt avg `4.234` n `239`; crypto_major avg `3.1295` n `8`; equity avg `2.3811` n `168`; fx avg `-0.016` n `6`; index avg `0.232` n `27`; metal avg `0.5136` n `20`; unknown avg `771.9763` n `1015`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1957`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1329`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
