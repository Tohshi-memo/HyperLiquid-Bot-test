# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-13T13:07:31.365032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1056` n `12`; crypto_alt avg `0.1287` n `230`; crypto_major avg `0.1868` n `8`; equity avg `0.1442` n `113`; fx avg `-0.0008` n `6`; index avg `0.028` n `25`; metal avg `0.0086` n `20`; unknown avg `0.0498` n `787`
- 1h: commodity avg `-0.1041` n `12`; crypto_alt avg `0.1906` n `230`; crypto_major avg `0.4078` n `8`; equity avg `0.2436` n `113`; fx avg `-0.008` n `6`; index avg `0.0571` n `25`; metal avg `0.0022` n `20`; unknown avg `0.1636` n `787`
- 4h: commodity avg `-0.1467` n `12`; crypto_alt avg `0.2123` n `230`; crypto_major avg `0.1284` n `8`; equity avg `0.27` n `113`; fx avg `-0.0176` n `6`; index avg `0.0744` n `25`; metal avg `0.1926` n `20`; unknown avg `0.0533` n `787`
- 24h: commodity avg `-0.4471` n `12`; crypto_alt avg `-0.7554` n `230`; crypto_major avg `-0.3357` n `8`; equity avg `0.6239` n `113`; fx avg `0.0301` n `6`; index avg `0.0599` n `25`; metal avg `-0.4874` n `20`; unknown avg `0.3612` n `754`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2289`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1969`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1635`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1362`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1315`, n `668`, weak_sample_signal
