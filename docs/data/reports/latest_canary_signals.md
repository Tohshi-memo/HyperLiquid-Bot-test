# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T00:22:29.184133+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0203` n `12`; crypto_alt avg `-0.0857` n `228`; crypto_major avg `-0.1391` n `8`; equity avg `-0.0499` n `86`; fx avg `0.0111` n `6`; index avg `0.007` n `23`; metal avg `-0.0444` n `20`; unknown avg `-0.1627` n `764`
- 1h: commodity avg `0.0474` n `12`; crypto_alt avg `0.1619` n `228`; crypto_major avg `0.0193` n `8`; equity avg `-0.1919` n `86`; fx avg `0.0865` n `6`; index avg `-0.1052` n `23`; metal avg `0.0126` n `20`; unknown avg `-0.3642` n `764`
- 4h: commodity avg `0.0878` n `12`; crypto_alt avg `0.7303` n `228`; crypto_major avg `0.8083` n `8`; equity avg `0.8517` n `86`; fx avg `0.0435` n `6`; index avg `0.1119` n `23`; metal avg `0.0499` n `20`; unknown avg `-0.9153` n `748`
- 24h: commodity avg `-0.4565` n `12`; crypto_alt avg `-2.3339` n `228`; crypto_major avg `-2.0466` n `8`; equity avg `4.6479` n `86`; fx avg `0.0699` n `6`; index avg `0.3982` n `23`; metal avg `-1.5521` n `20`; unknown avg `-1.5373` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0634`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
