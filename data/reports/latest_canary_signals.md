# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T02:52:29.438916+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0429` n `12`; crypto_alt avg `0.2188` n `228`; crypto_major avg `0.1856` n `8`; equity avg `0.0777` n `88`; fx avg `-0.0057` n `6`; index avg `0.0242` n `23`; metal avg `0.1439` n `20`; unknown avg `0.0149` n `765`
- 1h: commodity avg `0.0388` n `12`; crypto_alt avg `0.2582` n `228`; crypto_major avg `0.1696` n `8`; equity avg `0.2759` n `88`; fx avg `-0.0296` n `6`; index avg `0.0683` n `23`; metal avg `0.0794` n `20`; unknown avg `-0.3275` n `763`
- 4h: commodity avg `0.0612` n `12`; crypto_alt avg `-0.5153` n `228`; crypto_major avg `-0.854` n `8`; equity avg `0.0636` n `88`; fx avg `0.0261` n `6`; index avg `0.0098` n `23`; metal avg `-0.3948` n `20`; unknown avg `-0.0719` n `763`
- 24h: commodity avg `-0.1824` n `12`; crypto_alt avg `0.2993` n `228`; crypto_major avg `1.4078` n `8`; equity avg `2.2355` n `88`; fx avg `0.1405` n `6`; index avg `0.2991` n `23`; metal avg `-0.8019` n `20`; unknown avg `1.6862` n `728`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0915`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
