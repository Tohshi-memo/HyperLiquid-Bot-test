# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T20:37:26.276525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0078` n `12`; crypto_alt avg `0.0322` n `229`; crypto_major avg `0.089` n `8`; equity avg `0.0287` n `88`; fx avg `-0.0057` n `6`; index avg `-0.0048` n `25`; metal avg `0.0014` n `20`; unknown avg `-0.0223` n `765`
- 1h: commodity avg `0.0126` n `12`; crypto_alt avg `-0.3684` n `229`; crypto_major avg `-0.2448` n `8`; equity avg `-0.0083` n `88`; fx avg `-0.0041` n `6`; index avg `0.0142` n `25`; metal avg `-0.0231` n `20`; unknown avg `-0.1627` n `765`
- 4h: commodity avg `-0.0486` n `12`; crypto_alt avg `-0.5139` n `229`; crypto_major avg `-0.3433` n `8`; equity avg `0.0276` n `88`; fx avg `-0.0428` n `6`; index avg `-0.0013` n `25`; metal avg `0.0171` n `20`; unknown avg `-0.9618` n `765`
- 24h: commodity avg `0.0118` n `12`; crypto_alt avg `-0.0006` n `229`; crypto_major avg `0.2406` n `8`; equity avg `0.2378` n `88`; fx avg `-0.0362` n `6`; index avg `-0.0156` n `25`; metal avg `0.0629` n `20`; unknown avg `-0.0686` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0928`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
