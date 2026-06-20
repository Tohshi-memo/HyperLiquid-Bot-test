# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T20:37:26.778425+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0374` n `12`; crypto_alt avg `-0.1965` n `228`; crypto_major avg `-0.1676` n `8`; equity avg `-0.0269` n `78`; fx avg `0.0` n `6`; index avg `-0.004` n `23`; metal avg `-0.0007` n `18`; unknown avg `0.3242` n `701`
- 1h: commodity avg `-0.0344` n `12`; crypto_alt avg `-0.2171` n `228`; crypto_major avg `-0.0435` n `8`; equity avg `0.0548` n `78`; fx avg `-0.0015` n `6`; index avg `-0.0085` n `23`; metal avg `0.0009` n `18`; unknown avg `-0.1084` n `701`
- 4h: commodity avg `-0.0952` n `12`; crypto_alt avg `-0.1664` n `228`; crypto_major avg `-0.113` n `8`; equity avg `0.0352` n `78`; fx avg `0.0146` n `6`; index avg `0.0016` n `23`; metal avg `-0.065` n `18`; unknown avg `0.0306` n `701`
- 24h: commodity avg `0.2377` n `12`; crypto_alt avg `0.6946` n `228`; crypto_major avg `1.1047` n `8`; equity avg `0.5039` n `78`; fx avg `0.1055` n `6`; index avg `0.054` n `23`; metal avg `-0.0116` n `18`; unknown avg `-0.1454` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0965`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0962`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0697`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.067`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
