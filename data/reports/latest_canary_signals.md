# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T18:07:29.549202+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0133` n `12`; crypto_alt avg `0.1984` n `229`; crypto_major avg `0.1194` n `8`; equity avg `0.0145` n `88`; fx avg `-0.0038` n `6`; index avg `0.0021` n `25`; metal avg `0.0025` n `20`; unknown avg `-0.0009` n `765`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `0.1739` n `229`; crypto_major avg `0.026` n `8`; equity avg `0.0373` n `88`; fx avg `0.0022` n `6`; index avg `-0.0093` n `25`; metal avg `-0.0003` n `20`; unknown avg `0.0087` n `765`
- 4h: commodity avg `0.0077` n `12`; crypto_alt avg `0.3628` n `229`; crypto_major avg `0.2188` n `8`; equity avg `0.0588` n `88`; fx avg `-0.0318` n `6`; index avg `0.0342` n `25`; metal avg `-0.0026` n `20`; unknown avg `0.0297` n `695`
- 24h: commodity avg `0.0197` n `12`; crypto_alt avg `-1.6907` n `229`; crypto_major avg `-1.19` n `8`; equity avg `0.2796` n `88`; fx avg `-0.0722` n `6`; index avg `0.089` n `25`; metal avg `0.0488` n `20`; unknown avg `-0.019` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0692`, n `668`, weak_sample_signal
