# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-04T17:22:25.671593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0024` n `12`; crypto_alt avg `0.1634` n `229`; crypto_major avg `0.1203` n `8`; equity avg `0.0307` n `88`; fx avg `0.0` n `6`; index avg `-0.0029` n `25`; metal avg `0.0094` n `20`; unknown avg `0.1099` n `765`
- 1h: commodity avg `-0.0292` n `12`; crypto_alt avg `-0.0076` n `229`; crypto_major avg `-0.0783` n `8`; equity avg `-0.0381` n `88`; fx avg `0.0007` n `6`; index avg `-0.0403` n `25`; metal avg `-0.0079` n `20`; unknown avg `-0.004` n `765`
- 4h: commodity avg `-0.0204` n `12`; crypto_alt avg `0.7032` n `229`; crypto_major avg `0.5206` n `8`; equity avg `-0.0042` n `88`; fx avg `0.0218` n `6`; index avg `-0.0324` n `25`; metal avg `0.0116` n `20`; unknown avg `0.2499` n `765`
- 24h: commodity avg `-0.0178` n `12`; crypto_alt avg `1.3396` n `229`; crypto_major avg `1.6379` n `8`; equity avg `0.168` n `88`; fx avg `-0.0032` n `6`; index avg `-0.0772` n `25`; metal avg `0.0268` n `20`; unknown avg `1.9051` n `741`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.081`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0676`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
