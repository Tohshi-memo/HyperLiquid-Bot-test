# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T18:07:29.740153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0503` n `12`; crypto_alt avg `0.2038` n `228`; crypto_major avg `0.12` n `8`; equity avg `-0.0107` n `78`; fx avg `0.0031` n `6`; index avg `-0.0219` n `23`; metal avg `-0.0157` n `18`; unknown avg `0.1026` n `701`
- 1h: commodity avg `-0.0044` n `12`; crypto_alt avg `-0.1441` n `228`; crypto_major avg `-0.1249` n `8`; equity avg `-0.0525` n `78`; fx avg `0.0017` n `6`; index avg `-0.0118` n `23`; metal avg `-0.0396` n `18`; unknown avg `-0.1092` n `701`
- 4h: commodity avg `-0.1371` n `12`; crypto_alt avg `1.3139` n `228`; crypto_major avg `0.7273` n `8`; equity avg `0.2455` n `78`; fx avg `0.0559` n `6`; index avg `0.0033` n `23`; metal avg `-0.0332` n `18`; unknown avg `0.761` n `701`
- 24h: commodity avg `0.3816` n `12`; crypto_alt avg `0.3574` n `228`; crypto_major avg `0.8306` n `8`; equity avg `0.3087` n `78`; fx avg `0.0768` n `6`; index avg `0.0348` n `23`; metal avg `0.0772` n `18`; unknown avg `0.1407` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.091`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0783`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0574`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
