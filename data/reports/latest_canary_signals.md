# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-23T22:52:32.567453+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0292` n `12`; crypto_alt avg `0.0218` n `228`; crypto_major avg `0.0773` n `8`; equity avg `-0.017` n `86`; fx avg `0.0048` n `6`; index avg `-0.0041` n `23`; metal avg `0.0273` n `20`; unknown avg `0.0921` n `764`
- 1h: commodity avg `-0.0308` n `12`; crypto_alt avg `-0.067` n `228`; crypto_major avg `0.0391` n `8`; equity avg `-0.2184` n `86`; fx avg `-0.02` n `6`; index avg `-0.0387` n `23`; metal avg `-0.1125` n `20`; unknown avg `-0.5283` n `764`
- 4h: commodity avg `-0.091` n `12`; crypto_alt avg `0.5654` n `228`; crypto_major avg `0.4588` n `8`; equity avg `0.1833` n `86`; fx avg `-0.0143` n `6`; index avg `0.0794` n `23`; metal avg `-0.0006` n `20`; unknown avg `1.2939` n `756`
- 24h: commodity avg `-0.4888` n `12`; crypto_alt avg `-1.6783` n `228`; crypto_major avg `-2.8696` n `8`; equity avg `-3.2268` n `86`; fx avg `-0.1763` n `6`; index avg `-0.8993` n `23`; metal avg `-1.2162` n `20`; unknown avg `1.8482` n `596`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1251`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1004`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
