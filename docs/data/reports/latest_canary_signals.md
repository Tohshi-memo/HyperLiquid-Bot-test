# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T18:37:30.857267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.0617` n `228`; crypto_major avg `0.0704` n `8`; equity avg `-0.0064` n `78`; fx avg `0.0011` n `6`; index avg `-0.0048` n `23`; metal avg `0.0117` n `18`; unknown avg `1.2532` n `701`
- 1h: commodity avg `0.02` n `12`; crypto_alt avg `0.471` n `228`; crypto_major avg `0.3917` n `8`; equity avg `-0.0095` n `78`; fx avg `0.1409` n `6`; index avg `0.0068` n `23`; metal avg `-0.0118` n `18`; unknown avg `-0.1561` n `701`
- 4h: commodity avg `-0.0992` n `12`; crypto_alt avg `0.9539` n `228`; crypto_major avg `0.5579` n `8`; equity avg `0.1313` n `78`; fx avg `0.0239` n `6`; index avg `0.0012` n `23`; metal avg `-0.0025` n `18`; unknown avg `1.0867` n `701`
- 24h: commodity avg `0.3373` n `12`; crypto_alt avg `0.716` n `228`; crypto_major avg `1.0378` n `8`; equity avg `0.3295` n `78`; fx avg `0.039` n `6`; index avg `0.0462` n `23`; metal avg `0.0919` n `18`; unknown avg `0.0984` n `557`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0584`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
