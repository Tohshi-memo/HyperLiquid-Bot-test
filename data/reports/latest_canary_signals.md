# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T22:37:15.837829+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0416` n `12`; crypto_alt avg `-0.0202` n `228`; crypto_major avg `0.0921` n `8`; equity avg `0.0118` n `69`; fx avg `0.0006` n `6`; index avg `-0.0255` n `23`; metal avg `-0.0167` n `18`; unknown avg `-0.0865` n `421`
- 1h: commodity avg `0.0365` n `12`; crypto_alt avg `-0.7725` n `228`; crypto_major avg `-0.3704` n `8`; equity avg `-0.0961` n `69`; fx avg `0.0019` n `6`; index avg `-0.0145` n `23`; metal avg `-0.0073` n `18`; unknown avg `0.8763` n `421`
- 4h: commodity avg `0.1655` n `12`; crypto_alt avg `-0.5611` n `228`; crypto_major avg `-0.2818` n `8`; equity avg `0.1679` n `69`; fx avg `0.009` n `6`; index avg `-0.0236` n `23`; metal avg `-0.0237` n `18`; unknown avg `0.7951` n `421`
- 24h: commodity avg `-0.057` n `12`; crypto_alt avg `1.2393` n `228`; crypto_major avg `2.6008` n `8`; equity avg `0.9305` n `69`; fx avg `0.0299` n `6`; index avg `0.0242` n `23`; metal avg `0.0372` n `18`; unknown avg `1.1824` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1754`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1042`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
