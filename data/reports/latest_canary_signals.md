# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T21:22:25.135149+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `12`; crypto_alt avg `0.2239` n `228`; crypto_major avg `0.0782` n `8`; equity avg `0.0006` n `78`; fx avg `-0.0063` n `6`; index avg `0.0032` n `23`; metal avg `-0.0064` n `18`; unknown avg `-0.013` n `701`
- 1h: commodity avg `0.0457` n `12`; crypto_alt avg `0.1582` n `228`; crypto_major avg `0.1223` n `8`; equity avg `0.0164` n `78`; fx avg `-0.0024` n `6`; index avg `-0.0026` n `23`; metal avg `0.0145` n `18`; unknown avg `0.4259` n `701`
- 4h: commodity avg `0.0035` n `12`; crypto_alt avg `0.0376` n `228`; crypto_major avg `0.2712` n `8`; equity avg `0.095` n `78`; fx avg `-0.007` n `6`; index avg `0.0018` n `23`; metal avg `-0.0218` n `18`; unknown avg `0.1134` n `701`
- 24h: commodity avg `0.275` n `12`; crypto_alt avg `0.7187` n `228`; crypto_major avg `1.1623` n `8`; equity avg `0.4872` n `78`; fx avg `0.1024` n `6`; index avg `0.0577` n `23`; metal avg `-0.0595` n `18`; unknown avg `0.2181` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0956`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
