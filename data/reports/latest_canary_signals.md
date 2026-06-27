# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-27T06:37:30.024531+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `0.149` n `228`; crypto_major avg `0.1834` n `8`; equity avg `0.1163` n `88`; fx avg `-0.006` n `6`; index avg `0.0175` n `23`; metal avg `0.0051` n `20`; unknown avg `0.4061` n `764`
- 1h: commodity avg `-0.0326` n `12`; crypto_alt avg `0.0096` n `228`; crypto_major avg `0.1188` n `8`; equity avg `0.1121` n `88`; fx avg `0.0015` n `6`; index avg `0.0088` n `23`; metal avg `0.0133` n `20`; unknown avg `-0.3177` n `732`
- 4h: commodity avg `0.0183` n `12`; crypto_alt avg `-0.377` n `228`; crypto_major avg `-0.2355` n `8`; equity avg `0.073` n `88`; fx avg `0.0039` n `6`; index avg `-0.0035` n `23`; metal avg `0.0037` n `20`; unknown avg `-0.7245` n `732`
- 24h: commodity avg `-0.2474` n `12`; crypto_alt avg `1.6532` n `228`; crypto_major avg `1.2222` n `8`; equity avg `1.5624` n `87`; fx avg `0.0734` n `6`; index avg `0.0299` n `23`; metal avg `0.8605` n `20`; unknown avg `-0.4241` n `708`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2042`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0955`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
