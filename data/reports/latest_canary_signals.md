# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T22:22:24.802843+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.3461` n `230`; crypto_major avg `0.2383` n `8`; equity avg `-0.0215` n `121`; fx avg `-0.0085` n `6`; index avg `-0.0065` n `25`; metal avg `0.0119` n `20`; unknown avg `0.0979` n `794`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `-0.5375` n `230`; crypto_major avg `-0.3477` n `8`; equity avg `0.0056` n `121`; fx avg `-0.0209` n `6`; index avg `0.0023` n `25`; metal avg `0.006` n `20`; unknown avg `0.0252` n `794`
- 4h: commodity avg `0.0867` n `12`; crypto_alt avg `-1.5655` n `230`; crypto_major avg `-0.7131` n `8`; equity avg `0.0746` n `121`; fx avg `0.0249` n `6`; index avg `-0.0076` n `25`; metal avg `0.005` n `20`; unknown avg `0.2196` n `794`
- 24h: commodity avg `0.0403` n `12`; crypto_alt avg `-2.3395` n `230`; crypto_major avg `-0.0596` n `8`; equity avg `-0.4279` n `121`; fx avg `0.0664` n `6`; index avg `-0.0539` n `25`; metal avg `-0.0615` n `20`; unknown avg `1.6751` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1262`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
