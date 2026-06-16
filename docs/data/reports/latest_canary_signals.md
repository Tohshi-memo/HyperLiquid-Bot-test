# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T17:52:49.804515+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0541` n `12`; crypto_alt avg `0.49` n `228`; crypto_major avg `0.5644` n `8`; equity avg `0.29` n `77`; fx avg `0.0028` n `6`; index avg `0.1702` n `23`; metal avg `0.0519` n `18`; unknown avg `0.2399` n `687`
- 1h: commodity avg `-0.0183` n `12`; crypto_alt avg `0.7672` n `228`; crypto_major avg `0.6032` n `8`; equity avg `0.0395` n `77`; fx avg `0.0146` n `6`; index avg `0.069` n `23`; metal avg `-0.0373` n `18`; unknown avg `0.2411` n `687`
- 4h: commodity avg `-0.5876` n `12`; crypto_alt avg `-0.0423` n `228`; crypto_major avg `-0.2557` n `8`; equity avg `-1.2731` n `77`; fx avg `0.0812` n `6`; index avg `-0.7631` n `23`; metal avg `-0.1355` n `18`; unknown avg `0.4886` n `687`
- 24h: commodity avg `-1.074` n `12`; crypto_alt avg `-1.343` n `228`; crypto_major avg `-0.6803` n `8`; equity avg `-0.9656` n `77`; fx avg `-0.0048` n `6`; index avg `-0.6314` n `23`; metal avg `0.5897` n `18`; unknown avg `0.8537` n `623`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0627`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.059`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0539`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0462`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0438`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0436`, n `668`, weak_sample_signal
