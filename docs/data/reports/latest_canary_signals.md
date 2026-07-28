# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T11:52:36.358911+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0156` n `12`; crypto_alt avg `-0.0125` n `230`; crypto_major avg `-0.0444` n `8`; equity avg `0.0361` n `102`; fx avg `-0.0085` n `6`; index avg `0.0243` n `25`; metal avg `-0.0528` n `20`; unknown avg `-0.0069` n `774`
- 1h: commodity avg `0.0669` n `12`; crypto_alt avg `-0.1718` n `230`; crypto_major avg `-0.2006` n `8`; equity avg `-0.367` n `102`; fx avg `0.0008` n `6`; index avg `0.0009` n `25`; metal avg `-0.0338` n `20`; unknown avg `-0.0355` n `774`
- 4h: commodity avg `0.0965` n `12`; crypto_alt avg `-0.0582` n `230`; crypto_major avg `-0.3462` n `8`; equity avg `-0.6647` n `102`; fx avg `-0.0266` n `6`; index avg `-0.0482` n `25`; metal avg `-0.2619` n `20`; unknown avg `-0.1655` n `774`
- 24h: commodity avg `-0.4494` n `12`; crypto_alt avg `-3.6445` n `230`; crypto_major avg `-3.7697` n `8`; equity avg `-4.5004` n `102`; fx avg `-0.1802` n `6`; index avg `-0.8849` n `25`; metal avg `-0.66` n `20`; unknown avg `1225.2144` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1271`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0826`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
