# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T19:37:13.996278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0847` n `12`; crypto_alt avg `-0.2474` n `228`; crypto_major avg `-0.1399` n `8`; equity avg `0.0001` n `67`; fx avg `0.0069` n `6`; index avg `-0.0064` n `23`; metal avg `0.0009` n `18`; unknown avg `-0.0115` n `405`
- 1h: commodity avg `-0.3466` n `12`; crypto_alt avg `-0.3634` n `228`; crypto_major avg `-0.3451` n `8`; equity avg `-0.0465` n `67`; fx avg `0.0069` n `6`; index avg `-0.0205` n `23`; metal avg `-0.0046` n `18`; unknown avg `0.7896` n `405`
- 4h: commodity avg `-0.1485` n `12`; crypto_alt avg `-0.05` n `228`; crypto_major avg `-0.5581` n `8`; equity avg `-0.0408` n `67`; fx avg `-0.0055` n `6`; index avg `0.1076` n `23`; metal avg `0.113` n `18`; unknown avg `-0.3104` n `405`
- 24h: commodity avg `-1.1127` n `12`; crypto_alt avg `2.0343` n `228`; crypto_major avg `0.2401` n `8`; equity avg `0.8611` n `67`; fx avg `-0.0181` n `6`; index avg `0.5077` n `23`; metal avg `1.632` n `18`; unknown avg `1.3773` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1611`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1466`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
