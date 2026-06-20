# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T19:37:26.732612+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0257` n `12`; crypto_alt avg `0.1212` n `228`; crypto_major avg `0.0474` n `8`; equity avg `0.0267` n `78`; fx avg `0.0006` n `6`; index avg `0.005` n `23`; metal avg `-0.0307` n `18`; unknown avg `13.5397` n `701`
- 1h: commodity avg `-0.0457` n `12`; crypto_alt avg `0.0124` n `228`; crypto_major avg `0.0022` n `8`; equity avg `0.0759` n `78`; fx avg `-0.0023` n `6`; index avg `0.0093` n `23`; metal avg `-0.0165` n `18`; unknown avg `1.37` n `701`
- 4h: commodity avg `-0.0693` n `12`; crypto_alt avg `-0.3456` n `228`; crypto_major avg `-0.4962` n `8`; equity avg `-0.0843` n `78`; fx avg `0.0214` n `6`; index avg `-0.0164` n `23`; metal avg `-0.1141` n `18`; unknown avg `0.1268` n `701`
- 24h: commodity avg `0.273` n `12`; crypto_alt avg `1.0608` n `228`; crypto_major avg `1.1601` n `8`; equity avg `0.4574` n `78`; fx avg `0.1` n `6`; index avg `0.0531` n `23`; metal avg `0.0506` n `18`; unknown avg `0.0539` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1017`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
