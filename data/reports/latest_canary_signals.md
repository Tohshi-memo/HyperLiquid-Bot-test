# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T05:34:24.728314+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `0.3388` n `229`; crypto_major avg `0.4047` n `8`; equity avg `0.1071` n `88`; fx avg `-0.0238` n `6`; index avg `0.0243` n `25`; metal avg `0.0696` n `20`; unknown avg `0.3704` n `765`
- 1h: commodity avg `0.0335` n `12`; crypto_alt avg `0.2575` n `229`; crypto_major avg `0.5536` n `8`; equity avg `0.0616` n `88`; fx avg `0.0302` n `6`; index avg `0.0169` n `25`; metal avg `0.0182` n `20`; unknown avg `-0.1045` n `765`
- 4h: commodity avg `0.1861` n `12`; crypto_alt avg `-0.0288` n `229`; crypto_major avg `0.2226` n `8`; equity avg `0.7082` n `88`; fx avg `0.0666` n `6`; index avg `0.1844` n `25`; metal avg `-0.0061` n `20`; unknown avg `-0.3484` n `761`
- 24h: commodity avg `0.4469` n `12`; crypto_alt avg `1.9244` n `228`; crypto_major avg `3.1535` n `8`; equity avg `-0.3424` n `88`; fx avg `-0.0515` n `6`; index avg `0.0461` n `25`; metal avg `1.3343` n `20`; unknown avg `6.1888` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0848`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0717`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
