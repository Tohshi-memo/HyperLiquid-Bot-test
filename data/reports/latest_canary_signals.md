# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-25T23:52:17.875242+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `12`; crypto_alt avg `-0.011` n `228`; crypto_major avg `0.0303` n `8`; equity avg `0.0337` n `67`; fx avg `0.0312` n `6`; index avg `-0.0001` n `23`; metal avg `0.0791` n `18`; unknown avg `-0.1832` n `405`
- 1h: commodity avg `0.1804` n `12`; crypto_alt avg `0.0865` n `228`; crypto_major avg `0.0821` n `8`; equity avg `-0.107` n `67`; fx avg `-0.0183` n `6`; index avg `-0.0873` n `23`; metal avg `-0.2989` n `18`; unknown avg `-0.3628` n `405`
- 4h: commodity avg `0.1403` n `12`; crypto_alt avg `-0.8748` n `228`; crypto_major avg `-0.4359` n `8`; equity avg `-0.263` n `67`; fx avg `0.006` n `6`; index avg `-0.314` n `23`; metal avg `-0.2896` n `18`; unknown avg `-0.6812` n `405`
- 24h: commodity avg `-0.2631` n `12`; crypto_alt avg `1.4055` n `228`; crypto_major avg `-0.2806` n `8`; equity avg `0.5994` n `67`; fx avg `-0.0343` n `6`; index avg `0.4425` n `23`; metal avg `0.0288` n `18`; unknown avg `0.8624` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1713`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1669`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1443`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1266`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
