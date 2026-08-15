# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T06:37:30.874771+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1062` n `12`; crypto_alt avg `-0.0447` n `230`; crypto_major avg `0.0139` n `8`; equity avg `-0.0035` n `114`; fx avg `0.0` n `6`; index avg `0.0038` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.0074` n `791`
- 1h: commodity avg `-0.1153` n `12`; crypto_alt avg `-0.1332` n `230`; crypto_major avg `0.0847` n `8`; equity avg `-0.0425` n `114`; fx avg `-0.0029` n `6`; index avg `-0.0083` n `25`; metal avg `-0.0154` n `20`; unknown avg `-0.0123` n `759`
- 4h: commodity avg `-0.0437` n `12`; crypto_alt avg `0.2578` n `230`; crypto_major avg `-0.0461` n `8`; equity avg `-0.0365` n `114`; fx avg `-0.0618` n `6`; index avg `-0.0205` n `25`; metal avg `-0.0299` n `20`; unknown avg `-0.0087` n `759`
- 24h: commodity avg `-0.0677` n `12`; crypto_alt avg `0.7916` n `230`; crypto_major avg `-0.0269` n `8`; equity avg `-0.0722` n `114`; fx avg `0.108` n `6`; index avg `-0.0645` n `25`; metal avg `0.3246` n `20`; unknown avg `-0.139` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1754`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1579`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1468`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1376`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
