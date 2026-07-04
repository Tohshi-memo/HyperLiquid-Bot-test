# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T21:37:29.560900+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.0883` n `229`; crypto_major avg `-0.0622` n `8`; equity avg `0.0102` n `88`; fx avg `-0.0023` n `6`; index avg `0.0064` n `25`; metal avg `0.0087` n `20`; unknown avg `0.0211` n `765`
- 1h: commodity avg `-0.0236` n `12`; crypto_alt avg `0.276` n `229`; crypto_major avg `0.2259` n `8`; equity avg `0.0493` n `88`; fx avg `0.0126` n `6`; index avg `-0.0028` n `25`; metal avg `0.0398` n `20`; unknown avg `1.0402` n `765`
- 4h: commodity avg `-0.0679` n `12`; crypto_alt avg `-0.3688` n `229`; crypto_major avg `-0.3219` n `8`; equity avg `0.0726` n `88`; fx avg `-0.0324` n `6`; index avg `0.0215` n `25`; metal avg `0.0538` n `20`; unknown avg `-1.0675` n `765`
- 24h: commodity avg `-0.0055` n `12`; crypto_alt avg `0.5198` n `229`; crypto_major avg `0.808` n `8`; equity avg `0.251` n `88`; fx avg `-0.0047` n `6`; index avg `-0.0153` n `25`; metal avg `0.0856` n `20`; unknown avg `-0.005` n `741`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.095`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0878`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
