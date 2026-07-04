# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T03:52:29.523440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0041` n `12`; crypto_alt avg `-0.1141` n `229`; crypto_major avg `-0.0421` n `8`; equity avg `-0.0491` n `88`; fx avg `0.0037` n `6`; index avg `0.0016` n `25`; metal avg `0.0012` n `20`; unknown avg `0.5374` n `765`
- 1h: commodity avg `0.0118` n `12`; crypto_alt avg `0.1634` n `229`; crypto_major avg `0.2139` n `8`; equity avg `0.021` n `88`; fx avg `0.0277` n `6`; index avg `0.0083` n `25`; metal avg `-0.0008` n `20`; unknown avg `3.1693` n `765`
- 4h: commodity avg `-0.0005` n `12`; crypto_alt avg `-0.3047` n `229`; crypto_major avg `0.1067` n `8`; equity avg `0.1921` n `88`; fx avg `-0.0069` n `6`; index avg `-0.0114` n `25`; metal avg `-0.041` n `20`; unknown avg `-0.0248` n `763`
- 24h: commodity avg `-0.0144` n `12`; crypto_alt avg `2.3484` n `229`; crypto_major avg `3.0507` n `8`; equity avg `0.8773` n `88`; fx avg `-0.183` n `6`; index avg `0.1853` n `25`; metal avg `-0.1056` n `20`; unknown avg `4.168` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0841`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
