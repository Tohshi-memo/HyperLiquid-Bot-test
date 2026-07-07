# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T19:37:31.899517+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0035` n `12`; crypto_alt avg `0.254` n `229`; crypto_major avg `0.3792` n `8`; equity avg `0.1127` n `91`; fx avg `-0.0164` n `6`; index avg `0.0271` n `25`; metal avg `0.1214` n `20`; unknown avg `0.0261` n `763`
- 1h: commodity avg `0.406` n `12`; crypto_alt avg `-0.8572` n `229`; crypto_major avg `-0.6624` n `8`; equity avg `-0.5976` n `91`; fx avg `0.0008` n `6`; index avg `-0.137` n `25`; metal avg `-0.3525` n `20`; unknown avg `0.3619` n `761`
- 4h: commodity avg `0.4322` n `12`; crypto_alt avg `-1.1803` n `229`; crypto_major avg `-0.8632` n `8`; equity avg `0.0558` n `91`; fx avg `-0.0412` n `6`; index avg `0.068` n `25`; metal avg `-0.3117` n `20`; unknown avg `0.1098` n `761`
- 24h: commodity avg `0.8841` n `12`; crypto_alt avg `-2.0409` n `229`; crypto_major avg `-1.1873` n `8`; equity avg `-3.487` n `91`; fx avg `-0.2524` n `6`; index avg `-0.6615` n `25`; metal avg `-0.5462` n `20`; unknown avg `-0.3548` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1211`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0704`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
