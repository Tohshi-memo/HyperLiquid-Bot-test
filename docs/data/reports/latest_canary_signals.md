# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T18:37:26.832671+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0016` n `12`; crypto_alt avg `0.0022` n `229`; crypto_major avg `0.0441` n `8`; equity avg `-0.0019` n `88`; fx avg `0.0` n `6`; index avg `0.0035` n `25`; metal avg `-0.0005` n `20`; unknown avg `-0.0569` n `765`
- 1h: commodity avg `0.0024` n `12`; crypto_alt avg `0.1813` n `229`; crypto_major avg `0.0092` n `8`; equity avg `0.0506` n `88`; fx avg `-0.004` n `6`; index avg `0.0128` n `25`; metal avg `-0.0074` n `20`; unknown avg `0.0012` n `765`
- 4h: commodity avg `-0.0064` n `12`; crypto_alt avg `0.4282` n `229`; crypto_major avg `0.2202` n `8`; equity avg `0.088` n `88`; fx avg `0.0006` n `6`; index avg `-0.0034` n `25`; metal avg `-0.0058` n `20`; unknown avg `0.1253` n `695`
- 24h: commodity avg `0.0229` n `12`; crypto_alt avg `-1.4229` n `229`; crypto_major avg `-0.9471` n `8`; equity avg `0.3574` n `88`; fx avg `-0.0748` n `6`; index avg `0.1056` n `25`; metal avg `0.055` n `20`; unknown avg `-0.0392` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0841`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0803`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
