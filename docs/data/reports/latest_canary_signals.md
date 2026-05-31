# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T12:22:15.878832+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.035` n `12`; crypto_alt avg `0.2136` n `228`; crypto_major avg `0.133` n `8`; equity avg `0.0545` n `69`; fx avg `0.0` n `6`; index avg `-0.0006` n `23`; metal avg `0.0131` n `18`; unknown avg `0.1985` n `421`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `0.2269` n `228`; crypto_major avg `0.1421` n `8`; equity avg `0.0242` n `69`; fx avg `0.0258` n `6`; index avg `-0.0508` n `23`; metal avg `0.027` n `18`; unknown avg `0.9703` n `421`
- 4h: commodity avg `0.0746` n `12`; crypto_alt avg `-0.0004` n `228`; crypto_major avg `-0.2581` n `8`; equity avg `-0.0708` n `69`; fx avg `-0.0178` n `6`; index avg `-0.1642` n `23`; metal avg `-0.0174` n `18`; unknown avg `0.7061` n `421`
- 24h: commodity avg `0.1197` n `12`; crypto_alt avg `0.1702` n `228`; crypto_major avg `1.1099` n `8`; equity avg `0.9526` n `69`; fx avg `0.007` n `6`; index avg `-0.1556` n `23`; metal avg `-0.0483` n `18`; unknown avg `0.691` n `401`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1068`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0914`, n `668`, weak_sample_signal
