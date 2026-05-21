# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T09:07:19.275360+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2881` n `12`; crypto_alt avg `0.0903` n `228`; crypto_major avg `0.0911` n `8`; equity avg `0.1322` n `66`; fx avg `-0.011` n `6`; index avg `0.1193` n `23`; metal avg `0.0925` n `18`; unknown avg `-0.0116` n `386`
- 1h: commodity avg `-0.3499` n `12`; crypto_alt avg `0.0612` n `228`; crypto_major avg `-0.0783` n `8`; equity avg `0.2059` n `66`; fx avg `0.0056` n `6`; index avg `0.1137` n `23`; metal avg `0.3857` n `18`; unknown avg `0.188` n `386`
- 4h: commodity avg `-0.3221` n `12`; crypto_alt avg `0.1338` n `228`; crypto_major avg `0.4088` n `8`; equity avg `-0.0708` n `66`; fx avg `-0.0176` n `6`; index avg `0.0406` n `23`; metal avg `-0.056` n `18`; unknown avg `0.9079` n `374`
- 24h: commodity avg `-1.944` n `12`; crypto_alt avg `2.8426` n `228`; crypto_major avg `3.5299` n `8`; equity avg `1.8651` n `66`; fx avg `0.0876` n `6`; index avg `1.3576` n `23`; metal avg `0.4182` n `18`; unknown avg `5.6716` n `374`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0518`, n `668`, weak_sample_signal
