# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-21T08:22:28.282746+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.263` n `228`; crypto_major avg `-0.1495` n `8`; equity avg `-0.0435` n `78`; fx avg `-0.0058` n `6`; index avg `-0.0125` n `23`; metal avg `-0.0192` n `18`; unknown avg `-0.1147` n `702`
- 1h: commodity avg `-0.0046` n `12`; crypto_alt avg `0.0533` n `228`; crypto_major avg `-0.4106` n `8`; equity avg `-0.0884` n `78`; fx avg `-0.0059` n `6`; index avg `-0.022` n `23`; metal avg `-0.0418` n `18`; unknown avg `-0.1846` n `694`
- 4h: commodity avg `-0.1046` n `12`; crypto_alt avg `0.1009` n `228`; crypto_major avg `-0.745` n `8`; equity avg `0.0573` n `78`; fx avg `-0.0056` n `6`; index avg `0.0042` n `23`; metal avg `0.0219` n `18`; unknown avg `-0.0901` n `654`
- 24h: commodity avg `0.0367` n `12`; crypto_alt avg `1.1528` n `228`; crypto_major avg `-0.0782` n `8`; equity avg `0.2234` n `78`; fx avg `0.0433` n `6`; index avg `0.0304` n `23`; metal avg `-0.0248` n `18`; unknown avg `-0.003` n `525`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0766`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0562`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0526`, n `668`, weak_sample_signal
