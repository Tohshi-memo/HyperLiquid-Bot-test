# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T10:37:27.051768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0475` n `12`; crypto_alt avg `0.096` n `229`; crypto_major avg `0.2204` n `8`; equity avg `0.0494` n `88`; fx avg `-0.0023` n `6`; index avg `0.0004` n `25`; metal avg `-0.058` n `20`; unknown avg `0.6432` n `765`
- 1h: commodity avg `-0.0676` n `12`; crypto_alt avg `0.418` n `229`; crypto_major avg `0.6041` n `8`; equity avg `0.1488` n `88`; fx avg `-0.0056` n `6`; index avg `0.0221` n `25`; metal avg `0.0135` n `20`; unknown avg `0.6624` n `765`
- 4h: commodity avg `-0.1579` n `12`; crypto_alt avg `0.614` n `229`; crypto_major avg `0.613` n `8`; equity avg `0.2574` n `88`; fx avg `0.0368` n `6`; index avg `0.0174` n `25`; metal avg `0.0276` n `20`; unknown avg `1.0128` n `755`
- 24h: commodity avg `0.34` n `12`; crypto_alt avg `1.7034` n `229`; crypto_major avg `2.4789` n `8`; equity avg `0.2669` n `88`; fx avg `-0.0893` n `6`; index avg `0.2082` n `25`; metal avg `1.1693` n `20`; unknown avg `5.9043` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.063`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
