# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T23:22:33.914521+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0021` n `12`; crypto_alt avg `0.0462` n `230`; crypto_major avg `0.0232` n `8`; equity avg `0.0331` n `114`; fx avg `0.0` n `6`; index avg `-0.0001` n `25`; metal avg `0.0015` n `20`; unknown avg `-0.0487` n `791`
- 1h: commodity avg `-0.0242` n `12`; crypto_alt avg `0.1338` n `230`; crypto_major avg `0.1039` n `8`; equity avg `0.0012` n `114`; fx avg `0.0041` n `6`; index avg `-0.0031` n `25`; metal avg `0.0051` n `20`; unknown avg `1.8803` n `791`
- 4h: commodity avg `0.0374` n `12`; crypto_alt avg `0.3886` n `230`; crypto_major avg `0.235` n `8`; equity avg `0.3475` n `114`; fx avg `0.0103` n `6`; index avg `0.0298` n `25`; metal avg `0.0468` n `20`; unknown avg `0.2589` n `791`
- 24h: commodity avg `0.2121` n `12`; crypto_alt avg `0.2652` n `230`; crypto_major avg `-0.829` n `8`; equity avg `-0.5169` n `114`; fx avg `0.0833` n `6`; index avg `-0.0968` n `25`; metal avg `0.2083` n `20`; unknown avg `-0.1082` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2166`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1928`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1565`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1506`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1405`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.136`, n `668`, weak_sample_signal
