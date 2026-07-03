# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T18:52:33.729507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0292` n `12`; crypto_alt avg `-0.0359` n `229`; crypto_major avg `0.0647` n `8`; equity avg `0.0307` n `88`; fx avg `-0.0012` n `6`; index avg `0.0042` n `25`; metal avg `0.0041` n `20`; unknown avg `0.1363` n `765`
- 1h: commodity avg `-0.0073` n `12`; crypto_alt avg `-0.0715` n `229`; crypto_major avg `0.1769` n `8`; equity avg `0.036` n `88`; fx avg `0.0021` n `6`; index avg `-0.0088` n `25`; metal avg `-0.0095` n `20`; unknown avg `0.6958` n `765`
- 4h: commodity avg `0.0379` n `12`; crypto_alt avg `0.2536` n `229`; crypto_major avg `0.4511` n `8`; equity avg `0.1412` n `88`; fx avg `-0.0174` n `6`; index avg `0.0345` n `25`; metal avg `-0.0264` n `20`; unknown avg `2.47` n `765`
- 24h: commodity avg `0.2123` n `12`; crypto_alt avg `2.4193` n `229`; crypto_major avg `2.1045` n `8`; equity avg `2.0398` n `88`; fx avg `-0.0499` n `6`; index avg `0.5771` n `25`; metal avg `0.5488` n `20`; unknown avg `9.4486` n `739`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
