# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T02:22:24.327104+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0047` n `12`; crypto_alt avg `0.7241` n `230`; crypto_major avg `0.7902` n `8`; equity avg `0.021` n `121`; fx avg `0.0052` n `6`; index avg `-0.0024` n `25`; metal avg `0.009` n `20`; unknown avg `0.1089` n `793`
- 1h: commodity avg `-0.0055` n `12`; crypto_alt avg `1.0467` n `230`; crypto_major avg `1.2476` n `8`; equity avg `0.0451` n `121`; fx avg `0.0101` n `6`; index avg `0.0051` n `25`; metal avg `-0.0052` n `20`; unknown avg `0.1005` n `793`
- 4h: commodity avg `-0.0488` n `12`; crypto_alt avg `1.8957` n `230`; crypto_major avg `1.2047` n `8`; equity avg `0.0235` n `121`; fx avg `0.0092` n `6`; index avg `0.0134` n `25`; metal avg `-0.021` n `20`; unknown avg `0.2239` n `793`
- 24h: commodity avg `0.0205` n `12`; crypto_alt avg `9.7162` n `230`; crypto_major avg `7.6527` n `8`; equity avg `0.1407` n `121`; fx avg `0.0533` n `6`; index avg `-0.0127` n `25`; metal avg `0.2786` n `20`; unknown avg `1.3004` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1802`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1307`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
