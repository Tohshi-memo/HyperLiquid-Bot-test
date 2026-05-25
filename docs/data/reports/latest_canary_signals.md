# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T20:52:19.286681+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0545` n `12`; crypto_alt avg `-0.1712` n `228`; crypto_major avg `-0.1406` n `8`; equity avg `-0.04` n `67`; fx avg `0.0047` n `6`; index avg `-0.0534` n `23`; metal avg `-0.0205` n `18`; unknown avg `-0.1006` n `405`
- 1h: commodity avg `0.0872` n `12`; crypto_alt avg `-0.4278` n `228`; crypto_major avg `-0.3637` n `8`; equity avg `-0.0351` n `67`; fx avg `-0.0199` n `6`; index avg `-0.1247` n `23`; metal avg `-0.0013` n `18`; unknown avg `-0.4666` n `405`
- 4h: commodity avg `0.1193` n `12`; crypto_alt avg `-0.7907` n `228`; crypto_major avg `-0.8902` n `8`; equity avg `0.035` n `67`; fx avg `0.008` n `6`; index avg `0.1029` n `23`; metal avg `-0.0154` n `18`; unknown avg `-0.4036` n `405`
- 24h: commodity avg `-1.1729` n `12`; crypto_alt avg `2.1497` n `228`; crypto_major avg `0.4253` n `8`; equity avg `0.818` n `67`; fx avg `-0.0725` n `6`; index avg `0.6198` n `23`; metal avg `1.7711` n `18`; unknown avg `1.2049` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1624`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1506`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1384`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1261`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
