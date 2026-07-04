# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T15:52:25.728176+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `12`; crypto_alt avg `0.058` n `229`; crypto_major avg `-0.0545` n `8`; equity avg `0.0238` n `88`; fx avg `0.0015` n `6`; index avg `0.0008` n `25`; metal avg `0.01` n `20`; unknown avg `0.0518` n `765`
- 1h: commodity avg `0.0007` n `12`; crypto_alt avg `0.6322` n `229`; crypto_major avg `0.4236` n `8`; equity avg `0.0558` n `88`; fx avg `0.0082` n `6`; index avg `-0.0003` n `25`; metal avg `0.0138` n `20`; unknown avg `0.1571` n `765`
- 4h: commodity avg `-0.0451` n `12`; crypto_alt avg `0.8684` n `229`; crypto_major avg `1.0237` n `8`; equity avg `0.0416` n `88`; fx avg `0.0352` n `6`; index avg `0.0079` n `25`; metal avg `0.0248` n `20`; unknown avg `0.1251` n `759`
- 24h: commodity avg `0.0222` n `12`; crypto_alt avg `1.3526` n `229`; crypto_major avg `1.9987` n `8`; equity avg `0.3453` n `88`; fx avg `-0.0202` n `6`; index avg `0.0052` n `25`; metal avg `0.0868` n `20`; unknown avg `1.6138` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0685`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0675`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
