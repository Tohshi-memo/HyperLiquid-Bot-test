# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T15:07:29.154627+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0252` n `12`; crypto_alt avg `0.3441` n `229`; crypto_major avg `0.429` n `8`; equity avg `0.1276` n `88`; fx avg `0.019` n `6`; index avg `0.0095` n `25`; metal avg `0.0483` n `20`; unknown avg `-0.0134` n `765`
- 1h: commodity avg `-0.1505` n `12`; crypto_alt avg `0.3449` n `229`; crypto_major avg `0.51` n `8`; equity avg `0.158` n `88`; fx avg `0.021` n `6`; index avg `0.0094` n `25`; metal avg `0.1115` n `20`; unknown avg `0.2736` n `765`
- 4h: commodity avg `-0.041` n `12`; crypto_alt avg `0.6601` n `229`; crypto_major avg `0.6975` n `8`; equity avg `-0.0604` n `88`; fx avg `-0.0041` n `6`; index avg `0.0088` n `25`; metal avg `-0.0043` n `20`; unknown avg `1.4078` n `765`
- 24h: commodity avg `0.4554` n `12`; crypto_alt avg `3.0138` n `229`; crypto_major avg `2.8512` n `8`; equity avg `1.4345` n `88`; fx avg `-0.0804` n `6`; index avg `0.431` n `25`; metal avg `0.6639` n `20`; unknown avg `7.7081` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0698`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0514`, n `668`, weak_sample_signal
