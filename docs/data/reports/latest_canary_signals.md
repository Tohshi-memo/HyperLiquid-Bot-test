# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T18:43:40.719286+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0159` n `12`; crypto_alt avg `-0.0621` n `228`; crypto_major avg `0.0353` n `8`; equity avg `-0.0011` n `78`; fx avg `-0.0001` n `6`; index avg `0.0005` n `23`; metal avg `0.0131` n `18`; unknown avg `1.1054` n `701`
- 1h: commodity avg `0.0056` n `12`; crypto_alt avg `0.3465` n `228`; crypto_major avg `0.3564` n `8`; equity avg `-0.0042` n `78`; fx avg `0.1397` n `6`; index avg `0.0122` n `23`; metal avg `-0.0104` n `18`; unknown avg `-0.1695` n `701`
- 4h: commodity avg `-0.1134` n `12`; crypto_alt avg `0.8282` n `228`; crypto_major avg `0.5225` n `8`; equity avg `0.1367` n `78`; fx avg `0.0226` n `6`; index avg `0.0065` n `23`; metal avg `-0.0011` n `18`; unknown avg `1.0669` n `701`
- 24h: commodity avg `0.3226` n `12`; crypto_alt avg `0.5897` n `228`; crypto_major avg `1.0019` n `8`; equity avg `0.3348` n `78`; fx avg `0.0378` n `6`; index avg `0.0516` n `23`; metal avg `0.0933` n `18`; unknown avg `0.0802` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
