# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T16:52:27.024881+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0907` n `13`; crypto_alt avg `0.1652` n `239`; crypto_major avg `0.2371` n `8`; equity avg `0.0546` n `168`; fx avg `-0.0126` n `6`; index avg `0.0004` n `27`; metal avg `0.0167` n `20`; unknown avg `0.4742` n `1267`
- 1h: commodity avg `-0.1206` n `13`; crypto_alt avg `0.1923` n `239`; crypto_major avg `0.0968` n `8`; equity avg `-0.1071` n `168`; fx avg `-0.0119` n `6`; index avg `-0.0116` n `27`; metal avg `-0.0243` n `20`; unknown avg `-0.1347` n `1245`
- 4h: commodity avg `-0.0232` n `13`; crypto_alt avg `-0.3684` n `239`; crypto_major avg `-0.4931` n `8`; equity avg `-0.3255` n `168`; fx avg `-0.0178` n `6`; index avg `-0.0451` n `27`; metal avg `-0.0371` n `20`; unknown avg `-0.301` n `1241`
- 24h: commodity avg `0.2344` n `13`; crypto_alt avg `4.5201` n `239`; crypto_major avg `3.71` n `8`; equity avg `6.6747` n `168`; fx avg `0.0224` n `6`; index avg `0.6231` n `27`; metal avg `1.4126` n `20`; unknown avg `10.9271` n `1056`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
