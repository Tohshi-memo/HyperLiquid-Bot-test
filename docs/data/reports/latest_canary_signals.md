# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T13:52:30.162887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `0.1678` n `229`; crypto_major avg `0.2613` n `8`; equity avg `0.0018` n `88`; fx avg `-0.0` n `6`; index avg `0.0338` n `25`; metal avg `0.0189` n `20`; unknown avg `-0.1243` n `765`
- 1h: commodity avg `0.143` n `12`; crypto_alt avg `0.4124` n `229`; crypto_major avg `0.5301` n `8`; equity avg `-0.0818` n `88`; fx avg `-0.0157` n `6`; index avg `0.0411` n `25`; metal avg `-0.083` n `20`; unknown avg `0.3223` n `765`
- 4h: commodity avg `0.0479` n `12`; crypto_alt avg `1.1854` n `229`; crypto_major avg `1.1759` n `8`; equity avg `0.0421` n `88`; fx avg `0.0049` n `6`; index avg `0.0665` n `25`; metal avg `-0.1484` n `20`; unknown avg `1.3449` n `765`
- 24h: commodity avg `0.3784` n `12`; crypto_alt avg `1.5137` n `229`; crypto_major avg `1.2795` n `8`; equity avg `-1.6344` n `88`; fx avg `-0.0986` n `6`; index avg `-0.0344` n `25`; metal avg `0.1781` n `20`; unknown avg `6.6246` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0703`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
