# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T17:07:27.308294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0308` n `12`; crypto_alt avg `0.2097` n `229`; crypto_major avg `0.34` n `8`; equity avg `0.0599` n `88`; fx avg `0.0025` n `6`; index avg `-0.0033` n `25`; metal avg `-0.0056` n `20`; unknown avg `0.376` n `765`
- 1h: commodity avg `0.0298` n `12`; crypto_alt avg `0.2597` n `229`; crypto_major avg `0.2759` n `8`; equity avg `0.0374` n `88`; fx avg `-0.0079` n `6`; index avg `0.042` n `25`; metal avg `0.0707` n `20`; unknown avg `0.2304` n `765`
- 4h: commodity avg `0.0572` n `12`; crypto_alt avg `0.4198` n `229`; crypto_major avg `0.4783` n `8`; equity avg `0.0848` n `88`; fx avg `-0.0354` n `6`; index avg `0.0092` n `25`; metal avg `0.0154` n `20`; unknown avg `1.1346` n `765`
- 24h: commodity avg `0.2985` n `12`; crypto_alt avg `2.6661` n `229`; crypto_major avg `2.2021` n `8`; equity avg `2.1664` n `88`; fx avg `-0.0332` n `6`; index avg `0.6004` n `25`; metal avg `0.5904` n `20`; unknown avg `8.4917` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1066`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1062`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0653`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0481`, n `668`, weak_sample_signal
