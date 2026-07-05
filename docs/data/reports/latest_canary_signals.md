# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T17:37:32.742650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0085` n `12`; crypto_alt avg `-0.0058` n `229`; crypto_major avg `0.0344` n `8`; equity avg `0.0207` n `88`; fx avg `0.0022` n `6`; index avg `0.0006` n `25`; metal avg `0.0065` n `20`; unknown avg `-0.0307` n `765`
- 1h: commodity avg `0.0023` n `12`; crypto_alt avg `0.1528` n `229`; crypto_major avg `0.1438` n `8`; equity avg `0.0208` n `88`; fx avg `0.0034` n `6`; index avg `-0.0073` n `25`; metal avg `0.005` n `20`; unknown avg `-0.0143` n `765`
- 4h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.2282` n `229`; crypto_major avg `0.4383` n `8`; equity avg `-0.0225` n `88`; fx avg `-0.0313` n `6`; index avg `0.014` n `25`; metal avg `-0.0112` n `20`; unknown avg `0.0942` n `695`
- 24h: commodity avg `-0.0088` n `12`; crypto_alt avg `-1.7447` n `229`; crypto_major avg `-1.0406` n `8`; equity avg `0.267` n `88`; fx avg `-0.0734` n `6`; index avg `0.0964` n `25`; metal avg `0.0631` n `20`; unknown avg `-0.089` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.101`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0839`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0735`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
