# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T22:37:17.270574+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0356` n `12`; crypto_alt avg `-0.6609` n `228`; crypto_major avg `-0.452` n `8`; equity avg `-0.1481` n `67`; fx avg `0.0021` n `6`; index avg `-0.0689` n `23`; metal avg `-0.1227` n `18`; unknown avg `0.7343` n `405`
- 1h: commodity avg `-0.4766` n `12`; crypto_alt avg `-0.773` n `228`; crypto_major avg `-0.2548` n `8`; equity avg `-0.1607` n `67`; fx avg `0.0163` n `6`; index avg `-0.2036` n `23`; metal avg `-0.0906` n `18`; unknown avg `0.6459` n `405`
- 4h: commodity avg `-0.4396` n `12`; crypto_alt avg `-1.358` n `228`; crypto_major avg `-0.8765` n `8`; equity avg `-0.1375` n `67`; fx avg `0.0368` n `6`; index avg `-0.0852` n `23`; metal avg `-0.063` n `18`; unknown avg `0.2357` n `405`
- 24h: commodity avg `-0.6386` n `12`; crypto_alt avg `1.5654` n `228`; crypto_major avg `0.0866` n `8`; equity avg `0.8394` n `67`; fx avg `-0.0566` n `6`; index avg `0.4806` n `23`; metal avg `0.6902` n `18`; unknown avg `1.0707` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1312`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
