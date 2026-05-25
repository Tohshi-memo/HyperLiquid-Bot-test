# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T22:22:18.341533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1502` n `12`; crypto_alt avg `0.0319` n `228`; crypto_major avg `0.0959` n `8`; equity avg `0.0427` n `67`; fx avg `0.0098` n `6`; index avg `-0.0149` n `23`; metal avg `0.0398` n `18`; unknown avg `-0.0197` n `405`
- 1h: commodity avg `-0.1365` n `12`; crypto_alt avg `0.081` n `228`; crypto_major avg `0.1288` n `8`; equity avg `0.0335` n `67`; fx avg `-0.0098` n `6`; index avg `-0.0614` n `23`; metal avg `0.0327` n `18`; unknown avg `0.1987` n `405`
- 4h: commodity avg `-0.0995` n `12`; crypto_alt avg `-0.7567` n `228`; crypto_major avg `-0.405` n `8`; equity avg `0.018` n `67`; fx avg `0.03` n `6`; index avg `-0.1682` n `23`; metal avg `0.0521` n `18`; unknown avg `-0.4745` n `405`
- 24h: commodity avg `-0.6317` n `12`; crypto_alt avg `2.0924` n `228`; crypto_major avg `0.3118` n `8`; equity avg `1.008` n `67`; fx avg `-0.0508` n `6`; index avg `0.5968` n `23`; metal avg `0.8258` n `18`; unknown avg `1.2726` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.136`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1324`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
