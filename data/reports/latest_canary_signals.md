# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T19:22:18.618590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1082` n `12`; crypto_alt avg `0.0418` n `228`; crypto_major avg `0.0261` n `8`; equity avg `0.0742` n `69`; fx avg `-0.0051` n `6`; index avg `0.0282` n `23`; metal avg `-0.0011` n `18`; unknown avg `0.4949` n `421`
- 1h: commodity avg `0.2015` n `12`; crypto_alt avg `0.1434` n `228`; crypto_major avg `0.1384` n `8`; equity avg `0.1103` n `69`; fx avg `0.005` n `6`; index avg `0.0337` n `23`; metal avg `-0.0107` n `18`; unknown avg `1.5777` n `421`
- 4h: commodity avg `-0.2904` n `12`; crypto_alt avg `0.4773` n `228`; crypto_major avg `0.7279` n `8`; equity avg `-0.0255` n `69`; fx avg `-0.0149` n `6`; index avg `-0.0875` n `23`; metal avg `0.0384` n `18`; unknown avg `1.4532` n `421`
- 24h: commodity avg `0.1025` n `12`; crypto_alt avg `2.1936` n `228`; crypto_major avg `3.0828` n `8`; equity avg `1.3085` n `69`; fx avg `-0.0036` n `6`; index avg `0.18` n `23`; metal avg `-0.1947` n `18`; unknown avg `1.3285` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1888`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
