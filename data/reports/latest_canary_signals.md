# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T03:07:27.505855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `-0.0391` n `229`; crypto_major avg `-0.2385` n `8`; equity avg `0.0187` n `88`; fx avg `0.0077` n `6`; index avg `-0.0059` n `25`; metal avg `-0.0007` n `20`; unknown avg `0.0344` n `765`
- 1h: commodity avg `-0.0091` n `12`; crypto_alt avg `0.1804` n `229`; crypto_major avg `0.0408` n `8`; equity avg `0.0878` n `88`; fx avg `-0.0141` n `6`; index avg `-0.0027` n `25`; metal avg `0.0055` n `20`; unknown avg `-0.455` n `765`
- 4h: commodity avg `0.0012` n `12`; crypto_alt avg `-0.3757` n `229`; crypto_major avg `-0.188` n `8`; equity avg `0.1735` n `88`; fx avg `-0.0306` n `6`; index avg `-0.044` n `25`; metal avg `-0.0279` n `20`; unknown avg `-0.0918` n `763`
- 24h: commodity avg `0.0116` n `12`; crypto_alt avg `2.1058` n `229`; crypto_major avg `2.6513` n `8`; equity avg `0.9314` n `88`; fx avg `-0.1809` n `6`; index avg `0.1864` n `25`; metal avg `-0.1454` n `20`; unknown avg `4.3708` n `737`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0989`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
