# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T02:22:30.291235+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `0.0043` n `229`; crypto_major avg `-0.0884` n `8`; equity avg `-0.0069` n `88`; fx avg `-0.0044` n `6`; index avg `-0.0038` n `25`; metal avg `0.0018` n `20`; unknown avg `-0.1129` n `765`
- 1h: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.1737` n `229`; crypto_major avg `-0.288` n `8`; equity avg `0.0328` n `88`; fx avg `-0.0056` n `6`; index avg `0.0113` n `25`; metal avg `0.0166` n `20`; unknown avg `-0.1067` n `763`
- 4h: commodity avg `-0.0053` n `12`; crypto_alt avg `-0.6805` n `229`; crypto_major avg `-0.4519` n `8`; equity avg `0.0434` n `88`; fx avg `-0.0215` n `6`; index avg `-0.0355` n `25`; metal avg `-0.0118` n `20`; unknown avg `0.1251` n `763`
- 24h: commodity avg `0.0131` n `12`; crypto_alt avg `1.7007` n `229`; crypto_major avg `2.1328` n `8`; equity avg `0.793` n `88`; fx avg `-0.133` n `6`; index avg `0.1758` n `25`; metal avg `-0.1411` n `20`; unknown avg `3.3647` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0845`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0618`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0567`, n `668`, weak_sample_signal
