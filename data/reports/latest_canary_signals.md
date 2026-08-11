# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T13:22:35.173711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0336` n `12`; crypto_alt avg `-0.0994` n `230`; crypto_major avg `-0.0613` n `8`; equity avg `0.0098` n `113`; fx avg `0.0002` n `6`; index avg `-0.0064` n `25`; metal avg `0.0143` n `20`; unknown avg `0.0059` n `785`
- 1h: commodity avg `-0.1262` n `12`; crypto_alt avg `-0.1546` n `230`; crypto_major avg `-0.1731` n `8`; equity avg `0.0723` n `113`; fx avg `0.0097` n `6`; index avg `-0.0035` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.0075` n `785`
- 4h: commodity avg `-0.4834` n `12`; crypto_alt avg `-0.2547` n `230`; crypto_major avg `0.1557` n `8`; equity avg `0.6461` n `113`; fx avg `-0.0427` n `6`; index avg `0.1016` n `25`; metal avg `0.0207` n `20`; unknown avg `-0.2103` n `785`
- 24h: commodity avg `0.3862` n `12`; crypto_alt avg `-1.4417` n `230`; crypto_major avg `-0.2696` n `8`; equity avg `-0.2204` n `113`; fx avg `-0.0379` n `6`; index avg `0.1514` n `25`; metal avg `0.3727` n `20`; unknown avg `-0.0703` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1902`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1883`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1807`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1361`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
