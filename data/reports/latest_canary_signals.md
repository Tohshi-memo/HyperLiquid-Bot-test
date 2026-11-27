# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T07:52:24.374889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0183` n `13`; crypto_alt avg `-0.0012` n `239`; crypto_major avg `0.1464` n `8`; equity avg `-0.0063` n `168`; fx avg `-0.003` n `6`; index avg `-0.0089` n `27`; metal avg `0.0658` n `20`; unknown avg `0.3565` n `1263`
- 1h: commodity avg `0.0282` n `13`; crypto_alt avg `-0.0788` n `239`; crypto_major avg `0.0647` n `8`; equity avg `-0.3634` n `168`; fx avg `-0.0313` n `6`; index avg `-0.0596` n `27`; metal avg `0.0879` n `20`; unknown avg `0.3849` n `1257`
- 4h: commodity avg `0.0477` n `13`; crypto_alt avg `0.1505` n `239`; crypto_major avg `0.4553` n `8`; equity avg `0.4824` n `168`; fx avg `-0.0524` n `6`; index avg `-0.0259` n `27`; metal avg `0.4023` n `20`; unknown avg `0.7355` n `1231`
- 24h: commodity avg `0.4868` n `13`; crypto_alt avg `2.1272` n `239`; crypto_major avg `2.8003` n `8`; equity avg `3.3563` n `168`; fx avg `-0.0396` n `6`; index avg `0.2608` n `27`; metal avg `1.3595` n `20`; unknown avg `218.3335` n `991`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1122`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
