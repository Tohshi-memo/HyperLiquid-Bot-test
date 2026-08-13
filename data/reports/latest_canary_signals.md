# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T15:22:26.391962+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `0.0193` n `230`; crypto_major avg `0.0903` n `8`; equity avg `-0.0115` n `113`; fx avg `-0.0043` n `6`; index avg `0.0134` n `25`; metal avg `-0.0168` n `20`; unknown avg `-0.0221` n `787`
- 1h: commodity avg `0.2761` n `12`; crypto_alt avg `0.1281` n `230`; crypto_major avg `0.1676` n `8`; equity avg `0.0817` n `113`; fx avg `0.0065` n `6`; index avg `0.0651` n `25`; metal avg `-0.0013` n `20`; unknown avg `-0.07` n `787`
- 4h: commodity avg `0.0485` n `12`; crypto_alt avg `0.3888` n `230`; crypto_major avg `0.6146` n `8`; equity avg `1.8085` n `113`; fx avg `-0.0232` n `6`; index avg `0.3301` n `25`; metal avg `-0.154` n `20`; unknown avg `0.1371` n `787`
- 24h: commodity avg `-0.3211` n `12`; crypto_alt avg `0.1247` n `230`; crypto_major avg `0.6122` n `8`; equity avg `1.8471` n `113`; fx avg `0.0054` n `6`; index avg `0.3623` n `25`; metal avg `-0.6092` n `20`; unknown avg `0.3185` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2266`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2022`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1971`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1946`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.178`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1489`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1482`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
