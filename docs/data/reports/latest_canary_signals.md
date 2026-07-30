# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T22:02:45.641194+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0326` n `12`; crypto_alt avg `0.0608` n `230`; crypto_major avg `0.0514` n `8`; equity avg `0.0076` n `102`; fx avg `0.0168` n `6`; index avg `0.0088` n `25`; metal avg `-0.015` n `20`; unknown avg `-0.0101` n `779`
- 1h: commodity avg `-0.0198` n `12`; crypto_alt avg `0.0949` n `230`; crypto_major avg `0.0378` n `8`; equity avg `0.371` n `102`; fx avg `0.0163` n `6`; index avg `0.0634` n `25`; metal avg `-0.0028` n `20`; unknown avg `0.1218` n `779`
- 4h: commodity avg `-0.0536` n `12`; crypto_alt avg `-0.0818` n `230`; crypto_major avg `-0.1084` n `8`; equity avg `1.3352` n `102`; fx avg `0.0713` n `6`; index avg `0.1628` n `25`; metal avg `0.0947` n `20`; unknown avg `-0.0634` n `779`
- 24h: commodity avg `-0.0717` n `12`; crypto_alt avg `0.961` n `230`; crypto_major avg `1.5512` n `8`; equity avg `7.962` n `102`; fx avg `-0.3957` n `6`; index avg `0.9586` n `25`; metal avg `0.6115` n `20`; unknown avg `0.1365` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1438`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0654`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
