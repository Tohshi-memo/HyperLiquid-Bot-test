# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T21:52:30.530865+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0064` n `12`; crypto_alt avg `0.0863` n `229`; crypto_major avg `0.011` n `8`; equity avg `0.0009` n `88`; fx avg `0.0308` n `6`; index avg `-0.0071` n `25`; metal avg `-0.0143` n `20`; unknown avg `0.1485` n `765`
- 1h: commodity avg `0.0521` n `12`; crypto_alt avg `0.4896` n `229`; crypto_major avg `0.4219` n `8`; equity avg `0.0088` n `88`; fx avg `0.0604` n `6`; index avg `-0.0092` n `25`; metal avg `-0.0212` n `20`; unknown avg `0.3579` n `765`
- 4h: commodity avg `-0.0143` n `12`; crypto_alt avg `0.7814` n `229`; crypto_major avg `0.7167` n `8`; equity avg `0.1087` n `88`; fx avg `0.0336` n `6`; index avg `0.0027` n `25`; metal avg `-0.0065` n `20`; unknown avg `0.974` n `765`
- 24h: commodity avg `0.0473` n `12`; crypto_alt avg `-0.5539` n `229`; crypto_major avg `-0.0719` n `8`; equity avg `0.324` n `88`; fx avg `-0.0069` n `6`; index avg `0.0736` n `25`; metal avg `0.0022` n `20`; unknown avg `1.2917` n `663`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0897`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
