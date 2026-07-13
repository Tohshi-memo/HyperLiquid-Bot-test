# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T23:52:30.250527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0364` n `12`; crypto_alt avg `0.1596` n `230`; crypto_major avg `0.2115` n `8`; equity avg `-0.0293` n `92`; fx avg `0.0152` n `6`; index avg `-0.0134` n `25`; metal avg `0.0322` n `20`; unknown avg `0.0186` n `766`
- 1h: commodity avg `0.1177` n `12`; crypto_alt avg `0.2976` n `230`; crypto_major avg `0.4813` n `8`; equity avg `-0.5427` n `92`; fx avg `0.0212` n `6`; index avg `-0.0751` n `25`; metal avg `-0.0342` n `20`; unknown avg `0.3031` n `766`
- 4h: commodity avg `0.3156` n `12`; crypto_alt avg `-0.3043` n `230`; crypto_major avg `-0.0158` n `8`; equity avg `-0.7206` n `92`; fx avg `-0.0072` n `6`; index avg `-0.1531` n `25`; metal avg `-0.0128` n `20`; unknown avg `-0.2995` n `766`
- 24h: commodity avg `1.1307` n `12`; crypto_alt avg `-1.6951` n `230`; crypto_major avg `-2.0954` n `8`; equity avg `-3.418` n `92`; fx avg `-0.0374` n `6`; index avg `-0.6762` n `25`; metal avg `-0.3597` n `20`; unknown avg `-0.3691` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1753`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
