# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T12:52:25.016468+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `0.0285` n `229`; crypto_major avg `-0.0414` n `8`; equity avg `0.0041` n `88`; fx avg `-0.0175` n `6`; index avg `0.0002` n `25`; metal avg `0.0118` n `20`; unknown avg `0.0129` n `765`
- 1h: commodity avg `-0.0275` n `12`; crypto_alt avg `0.4728` n `229`; crypto_major avg `0.4207` n `8`; equity avg `0.0361` n `88`; fx avg `-0.0364` n `6`; index avg `0.0055` n `25`; metal avg `0.0016` n `20`; unknown avg `0.1206` n `765`
- 4h: commodity avg `-0.0414` n `12`; crypto_alt avg `0.0473` n `229`; crypto_major avg `0.2356` n `8`; equity avg `0.0295` n `88`; fx avg `-0.0352` n `6`; index avg `-0.0012` n `25`; metal avg `0.0303` n `20`; unknown avg `-0.0354` n `765`
- 24h: commodity avg `-0.091` n `12`; crypto_alt avg `-0.9542` n `229`; crypto_major avg `-0.2803` n `8`; equity avg `0.3138` n `88`; fx avg `-0.0223` n `6`; index avg `0.0578` n `25`; metal avg `0.0998` n `20`; unknown avg `-1.1854` n `725`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0918`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
