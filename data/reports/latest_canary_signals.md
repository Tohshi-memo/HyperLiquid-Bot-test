# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-09T15:52:32.660995+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0707` n `12`; crypto_alt avg `-0.0143` n `229`; crypto_major avg `0.0761` n `8`; equity avg `0.1436` n `91`; fx avg `0.0021` n `6`; index avg `0.0238` n `25`; metal avg `0.0372` n `20`; unknown avg `0.036` n `765`
- 1h: commodity avg `-0.2359` n `12`; crypto_alt avg `-0.1189` n `229`; crypto_major avg `0.0613` n `8`; equity avg `0.5761` n `91`; fx avg `0.0093` n `6`; index avg `0.0985` n `25`; metal avg `0.1537` n `20`; unknown avg `0.1533` n `765`
- 4h: commodity avg `-0.8729` n `12`; crypto_alt avg `-0.0597` n `229`; crypto_major avg `0.1555` n `8`; equity avg `0.9593` n `91`; fx avg `-0.023` n `6`; index avg `0.1993` n `25`; metal avg `0.4311` n `20`; unknown avg `0.1645` n `764`
- 24h: commodity avg `-1.5038` n `12`; crypto_alt avg `1.669` n `229`; crypto_major avg `1.2792` n `8`; equity avg `3.8505` n `91`; fx avg `0.057` n `6`; index avg `0.6622` n `25`; metal avg `1.4141` n `20`; unknown avg `1.2442` n `748`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.0921`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0664`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0651`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
