# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-05T17:52:26.021800+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0007` n `12`; crypto_alt avg `-0.0476` n `229`; crypto_major avg `-0.1419` n `8`; equity avg `0.0008` n `88`; fx avg `0.0017` n `6`; index avg `0.002` n `25`; metal avg `-0.0093` n `20`; unknown avg `-0.0059` n `765`
- 1h: commodity avg `-0.0087` n `12`; crypto_alt avg `0.0939` n `229`; crypto_major avg `0.0486` n `8`; equity avg `0.0126` n `88`; fx avg `0.0062` n `6`; index avg `-0.0056` n `25`; metal avg `-0.0083` n `20`; unknown avg `-0.0541` n `765`
- 4h: commodity avg `-0.0053` n `12`; crypto_alt avg `0.0287` n `229`; crypto_major avg `0.1328` n `8`; equity avg `-0.0089` n `88`; fx avg `-0.0261` n `6`; index avg `-0.002` n `25`; metal avg `-0.0259` n `20`; unknown avg `0.0409` n `695`
- 24h: commodity avg `-0.0254` n `12`; crypto_alt avg `-2.035` n `229`; crypto_major avg `-1.5541` n `8`; equity avg `0.2139` n `88`; fx avg `-0.0795` n `6`; index avg `0.0906` n `25`; metal avg `0.044` n `20`; unknown avg `-0.1167` n `663`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0936`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0802`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
