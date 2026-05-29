# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T06:52:21.711363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0276` n `12`; crypto_alt avg `0.2891` n `228`; crypto_major avg `0.1905` n `8`; equity avg `0.0791` n `69`; fx avg `0.007` n `6`; index avg `0.0342` n `23`; metal avg `0.1207` n `18`; unknown avg `0.1007` n `417`
- 1h: commodity avg `-0.0835` n `12`; crypto_alt avg `0.3732` n `228`; crypto_major avg `0.2299` n `8`; equity avg `0.2588` n `69`; fx avg `0.0487` n `6`; index avg `0.0604` n `23`; metal avg `0.1926` n `18`; unknown avg `0.0835` n `407`
- 4h: commodity avg `-0.0686` n `12`; crypto_alt avg `0.7327` n `228`; crypto_major avg `0.756` n `8`; equity avg `0.7863` n `69`; fx avg `0.0762` n `6`; index avg `0.2236` n `23`; metal avg `0.0834` n `18`; unknown avg `0.1201` n `407`
- 24h: commodity avg `0.1812` n `12`; crypto_alt avg `1.6891` n `228`; crypto_major avg `2.1713` n `8`; equity avg `4.1758` n `69`; fx avg `0.1908` n `6`; index avg `1.3474` n `23`; metal avg `1.9452` n `18`; unknown avg `0.6421` n `407`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1524`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1283`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.123`, n `668`, weak_sample_signal
