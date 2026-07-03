# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T08:37:27.414611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0862` n `12`; crypto_alt avg `0.0806` n `229`; crypto_major avg `0.0868` n `8`; equity avg `-0.0582` n `88`; fx avg `0.0166` n `6`; index avg `0.0057` n `25`; metal avg `-0.0019` n `20`; unknown avg `0.024` n `765`
- 1h: commodity avg `-0.13` n `12`; crypto_alt avg `0.17` n `229`; crypto_major avg `0.1275` n `8`; equity avg `-0.0081` n `88`; fx avg `0.0385` n `6`; index avg `0.0038` n `25`; metal avg `0.0293` n `20`; unknown avg `-0.0559` n `765`
- 4h: commodity avg `-0.1278` n `12`; crypto_alt avg `0.6404` n `229`; crypto_major avg `0.6636` n `8`; equity avg `0.141` n `88`; fx avg `-0.1107` n `6`; index avg `0.0692` n `25`; metal avg `0.1089` n `20`; unknown avg `-0.1564` n `743`
- 24h: commodity avg `0.2862` n `12`; crypto_alt avg `2.2537` n `228`; crypto_major avg `3.4888` n `8`; equity avg `0.2928` n `88`; fx avg `-0.1177` n `6`; index avg `0.2077` n `25`; metal avg `1.2558` n `20`; unknown avg `5.2359` n `741`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
