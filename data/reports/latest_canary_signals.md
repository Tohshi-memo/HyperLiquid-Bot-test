# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T21:52:27.811429+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0166` n `12`; crypto_alt avg `-0.0743` n `230`; crypto_major avg `-0.021` n `8`; equity avg `0.114` n `102`; fx avg `0.008` n `6`; index avg `0.0178` n `25`; metal avg `0.0159` n `20`; unknown avg `-0.0098` n `779`
- 1h: commodity avg `0.0203` n `12`; crypto_alt avg `-0.1008` n `230`; crypto_major avg `-0.019` n `8`; equity avg `0.4149` n `102`; fx avg `-0.0147` n `6`; index avg `0.0332` n `25`; metal avg `0.05` n `20`; unknown avg `0.1086` n `779`
- 4h: commodity avg `0.0106` n `12`; crypto_alt avg `-0.0636` n `230`; crypto_major avg `-0.1531` n `8`; equity avg `1.2205` n `102`; fx avg `0.0437` n `6`; index avg `0.1529` n `25`; metal avg `0.1383` n `20`; unknown avg `-0.0337` n `779`
- 24h: commodity avg `-0.1977` n `12`; crypto_alt avg `1.3305` n `230`; crypto_major avg `1.9101` n `8`; equity avg `8.7668` n `102`; fx avg `-0.3937` n `6`; index avg `1.1097` n `25`; metal avg `0.7162` n `20`; unknown avg `0.2142` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1439`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0614`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
