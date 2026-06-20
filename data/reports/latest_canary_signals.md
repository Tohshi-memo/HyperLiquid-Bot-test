# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T21:37:31.167354+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0191` n `12`; crypto_alt avg `-0.0214` n `228`; crypto_major avg `0.0439` n `8`; equity avg `-0.0235` n `78`; fx avg `-0.1772` n `6`; index avg `0.0015` n `23`; metal avg `-0.0068` n `18`; unknown avg `0.1695` n `701`
- 1h: commodity avg `0.1024` n `12`; crypto_alt avg `0.3341` n `228`; crypto_major avg `0.3348` n `8`; equity avg `0.0198` n `78`; fx avg `-0.1795` n `6`; index avg `0.0029` n `23`; metal avg `0.0085` n `18`; unknown avg `0.1089` n `701`
- 4h: commodity avg `0.0276` n `12`; crypto_alt avg `0.4745` n `228`; crypto_major avg `0.6513` n `8`; equity avg `0.1462` n `78`; fx avg `-0.0451` n `6`; index avg `0.0158` n `23`; metal avg `-0.0175` n `18`; unknown avg `0.0207` n `701`
- 24h: commodity avg `0.2948` n `12`; crypto_alt avg `0.9108` n `228`; crypto_major avg `1.3783` n `8`; equity avg `0.4898` n `78`; fx avg `-0.0656` n `6`; index avg `0.068` n `23`; metal avg `-0.0499` n `18`; unknown avg `-0.0429` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0799`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
