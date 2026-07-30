# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T23:38:00.744808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `0.246` n `230`; crypto_major avg `0.1953` n `8`; equity avg `0.2019` n `102`; fx avg `0.0146` n `6`; index avg `0.0403` n `25`; metal avg `0.0017` n `20`; unknown avg `-0.1245` n `779`
- 1h: commodity avg `-0.0097` n `12`; crypto_alt avg `0.1503` n `230`; crypto_major avg `0.0943` n `8`; equity avg `0.1348` n `102`; fx avg `0.0192` n `6`; index avg `-0.0174` n `25`; metal avg `-0.0161` n `20`; unknown avg `-0.1885` n `779`
- 4h: commodity avg `0.1057` n `12`; crypto_alt avg `0.3292` n `230`; crypto_major avg `0.3016` n `8`; equity avg `1.2071` n `102`; fx avg `0.0475` n `6`; index avg `0.1124` n `25`; metal avg `-0.0242` n `20`; unknown avg `-0.114` n `779`
- 24h: commodity avg `-0.0191` n `12`; crypto_alt avg `1.1244` n `230`; crypto_major avg `1.9002` n `8`; equity avg `7.6356` n `102`; fx avg `-0.3723` n `6`; index avg `0.8743` n `25`; metal avg `0.4342` n `20`; unknown avg `0.1232` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1407`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
