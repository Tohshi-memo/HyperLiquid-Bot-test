# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-31T01:57:00.961748+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0172` n `12`; crypto_alt avg `-0.1687` n `228`; crypto_major avg `-0.1741` n `8`; equity avg `-0.0263` n `69`; fx avg `0.0183` n `6`; index avg `0.007` n `23`; metal avg `-0.0031` n `18`; unknown avg `0.9388` n `421`
- 1h: commodity avg `0.0994` n `12`; crypto_alt avg `0.154` n `228`; crypto_major avg `0.3076` n `8`; equity avg `0.04` n `69`; fx avg `0.019` n `6`; index avg `0.0325` n `23`; metal avg `0.0149` n `18`; unknown avg `1.1854` n `421`
- 4h: commodity avg `0.0648` n `12`; crypto_alt avg `-0.3229` n `228`; crypto_major avg `0.3507` n `8`; equity avg `0.1544` n `69`; fx avg `-0.0039` n `6`; index avg `0.0402` n `23`; metal avg `-0.0313` n `18`; unknown avg `0.5988` n `421`
- 24h: commodity avg `-0.2058` n `12`; crypto_alt avg `0.2852` n `228`; crypto_major avg `2.2252` n `8`; equity avg `0.9392` n `69`; fx avg `0.0268` n `6`; index avg `0.1127` n `23`; metal avg `0.011` n `18`; unknown avg `1.371` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1365`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0914`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
