# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T19:07:20.098292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0193` n `12`; crypto_alt avg `-0.0355` n `228`; crypto_major avg `0.0994` n `8`; equity avg `0.0055` n `69`; fx avg `0.011` n `6`; index avg `0.0132` n `23`; metal avg `-0.0025` n `18`; unknown avg `1.3167` n `421`
- 1h: commodity avg `-0.0012` n `12`; crypto_alt avg `0.1363` n `228`; crypto_major avg `0.1514` n `8`; equity avg `0.04` n `69`; fx avg `0.0112` n `6`; index avg `0.0035` n `23`; metal avg `-0.0102` n `18`; unknown avg `1.047` n `421`
- 4h: commodity avg `-0.4022` n `12`; crypto_alt avg `0.3626` n `228`; crypto_major avg `0.7332` n `8`; equity avg `-0.1416` n `69`; fx avg `-0.0104` n `6`; index avg `-0.1405` n `23`; metal avg `0.0462` n `18`; unknown avg `0.7707` n `421`
- 24h: commodity avg `-0.0332` n `12`; crypto_alt avg `1.614` n `228`; crypto_major avg `2.8432` n `8`; equity avg `1.3055` n `69`; fx avg `0.0084` n `6`; index avg `0.162` n `23`; metal avg `-0.1578` n `18`; unknown avg `0.2942` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.189`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1508`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1337`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1193`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1106`, n `668`, weak_sample_signal
