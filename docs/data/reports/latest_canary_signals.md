# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T11:53:01.331342+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0596` n `12`; crypto_alt avg `0.0588` n `228`; crypto_major avg `0.1206` n `8`; equity avg `0.0637` n `78`; fx avg `-0.0056` n `6`; index avg `0.0003` n `23`; metal avg `0.0048` n `18`; unknown avg `0.114` n `687`
- 1h: commodity avg `-0.0451` n `12`; crypto_alt avg `0.0571` n `228`; crypto_major avg `0.112` n `8`; equity avg `-0.0078` n `78`; fx avg `0.0035` n `6`; index avg `0.0087` n `23`; metal avg `0.0034` n `18`; unknown avg `0.2293` n `687`
- 4h: commodity avg `-0.0953` n `12`; crypto_alt avg `0.223` n `228`; crypto_major avg `0.1975` n `8`; equity avg `-0.1119` n `78`; fx avg `0.0364` n `6`; index avg `0.0183` n `23`; metal avg `-0.018` n `18`; unknown avg `-0.2278` n `687`
- 24h: commodity avg `0.4305` n `12`; crypto_alt avg `-3.012` n `228`; crypto_major avg `-3.2282` n `8`; equity avg `1.1763` n `78`; fx avg `-0.0775` n `6`; index avg `0.2937` n `23`; metal avg `-4.0975` n `18`; unknown avg `-0.0685` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0943`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.056`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0535`, n `668`, weak_sample_signal
