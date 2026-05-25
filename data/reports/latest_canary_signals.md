# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T22:34:00.136409+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0043` n `12`; crypto_alt avg `-0.6729` n `228`; crypto_major avg `-0.468` n `8`; equity avg `-0.1092` n `67`; fx avg `0.0021` n `6`; index avg `-0.0438` n `23`; metal avg `-0.0915` n `18`; unknown avg `1.0168` n `405`
- 1h: commodity avg `-0.5164` n `12`; crypto_alt avg `-0.7845` n `228`; crypto_major avg `-0.2709` n `8`; equity avg `-0.1218` n `67`; fx avg `0.0163` n `6`; index avg `-0.1785` n `23`; metal avg `-0.0594` n `18`; unknown avg `0.9273` n `405`
- 4h: commodity avg `-0.4794` n `12`; crypto_alt avg `-1.3701` n `228`; crypto_major avg `-0.8925` n `8`; equity avg `-0.0985` n `67`; fx avg `0.0368` n `6`; index avg `-0.06` n `23`; metal avg `-0.0318` n `18`; unknown avg `0.4381` n `405`
- 24h: commodity avg `-0.6778` n `12`; crypto_alt avg `1.5508` n `228`; crypto_major avg `0.0706` n `8`; equity avg `0.8789` n `67`; fx avg `-0.0566` n `6`; index avg `0.5059` n `23`; metal avg `0.7215` n `18`; unknown avg `1.1464` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1549`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1366`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.128`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
