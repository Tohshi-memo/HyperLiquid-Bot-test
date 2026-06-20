# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T05:22:28.476019+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0357` n `12`; crypto_alt avg `0.1265` n `228`; crypto_major avg `0.2011` n `8`; equity avg `0.0621` n `78`; fx avg `0.0046` n `6`; index avg `0.03` n `23`; metal avg `0.0094` n `18`; unknown avg `81.574` n `687`
- 1h: commodity avg `0.0252` n `12`; crypto_alt avg `0.5797` n `228`; crypto_major avg `0.8518` n `8`; equity avg `0.1758` n `78`; fx avg `-0.0141` n `6`; index avg `0.0316` n `23`; metal avg `0.0244` n `18`; unknown avg `1.2272` n `687`
- 4h: commodity avg `0.2141` n `12`; crypto_alt avg `0.3613` n `228`; crypto_major avg `0.9016` n `8`; equity avg `0.3704` n `78`; fx avg `-0.0176` n `6`; index avg `0.0581` n `23`; metal avg `0.0248` n `18`; unknown avg `0.4651` n `679`
- 24h: commodity avg `0.4597` n `12`; crypto_alt avg `-3.0777` n `228`; crypto_major avg `-3.5673` n `8`; equity avg `1.2763` n `78`; fx avg `-0.1021` n `6`; index avg `0.3289` n `23`; metal avg `-4.106` n `18`; unknown avg `-0.5394` n `556`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0551`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
