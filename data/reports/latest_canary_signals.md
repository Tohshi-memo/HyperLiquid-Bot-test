# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T03:37:36.108012+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0106` n `12`; crypto_alt avg `-0.0487` n `229`; crypto_major avg `-0.0722` n `8`; equity avg `0.026` n `88`; fx avg `-0.0119` n `6`; index avg `-0.0059` n `25`; metal avg `-0.0093` n `20`; unknown avg `-0.1492` n `765`
- 1h: commodity avg `0.0103` n `12`; crypto_alt avg `0.0758` n `229`; crypto_major avg `0.1366` n `8`; equity avg `0.1425` n `88`; fx avg `0.0256` n `6`; index avg `0.023` n `25`; metal avg `-0.0571` n `20`; unknown avg `-0.0012` n `761`
- 4h: commodity avg `0.1597` n `12`; crypto_alt avg `0.4927` n `229`; crypto_major avg `0.2796` n `8`; equity avg `1.1031` n `88`; fx avg `0.0884` n `6`; index avg `0.2027` n `25`; metal avg `0.6263` n `20`; unknown avg `0.0565` n `761`
- 24h: commodity avg `0.3935` n `12`; crypto_alt avg `1.9774` n `228`; crypto_major avg `2.687` n `8`; equity avg `-1.1436` n `88`; fx avg `-0.0467` n `6`; index avg `-0.221` n `25`; metal avg `1.1875` n `20`; unknown avg `6.2908` n `735`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0563`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
