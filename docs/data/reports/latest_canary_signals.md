# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T07:52:26.313865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0529` n `12`; crypto_alt avg `0.0696` n `230`; crypto_major avg `0.1019` n `8`; equity avg `0.0075` n `108`; fx avg `0.0062` n `6`; index avg `0.0128` n `25`; metal avg `0.019` n `20`; unknown avg `0.0301` n `781`
- 1h: commodity avg `0.2017` n `12`; crypto_alt avg `-0.1077` n `230`; crypto_major avg `-0.2302` n `8`; equity avg `-0.3317` n `108`; fx avg `0.0115` n `6`; index avg `-0.0465` n `25`; metal avg `-0.028` n `20`; unknown avg `0.0174` n `781`
- 4h: commodity avg `0.3173` n `12`; crypto_alt avg `0.3072` n `230`; crypto_major avg `0.215` n `8`; equity avg `-0.1587` n `108`; fx avg `0.0589` n `6`; index avg `-0.032` n `25`; metal avg `0.3306` n `20`; unknown avg `0.0881` n `749`
- 24h: commodity avg `-1.1757` n `12`; crypto_alt avg `0.5368` n `230`; crypto_major avg `0.5319` n `8`; equity avg `2.981` n `108`; fx avg `-0.0238` n `6`; index avg `0.6566` n `25`; metal avg `1.2366` n `20`; unknown avg `0.0459` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1472`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1216`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1031`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
