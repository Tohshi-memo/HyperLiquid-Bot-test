# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-29T02:37:25.753278+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.21` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0604` n `12`; crypto_alt avg `0.3584` n `230`; crypto_major avg `0.3464` n `8`; equity avg `0.1346` n `102`; fx avg `-0.0051` n `6`; index avg `-0.0225` n `25`; metal avg `0.0306` n `20`; unknown avg `-0.0513` n `777`
- 1h: commodity avg `-0.1612` n `12`; crypto_alt avg `-0.1757` n `230`; crypto_major avg `0.1556` n `8`; equity avg `-0.7729` n `102`; fx avg `-0.0348` n `6`; index avg `-0.313` n `25`; metal avg `0.0266` n `20`; unknown avg `2.4704` n `777`
- 4h: commodity avg `-0.0733` n `12`; crypto_alt avg `-0.5435` n `230`; crypto_major avg `0.1265` n `8`; equity avg `-0.9117` n `102`; fx avg `-0.0224` n `6`; index avg `-0.3377` n `25`; metal avg `0.1774` n `20`; unknown avg `0.2193` n `776`
- 24h: commodity avg `-0.0914` n `12`; crypto_alt avg `-0.4193` n `230`; crypto_major avg `0.7772` n `8`; equity avg `-1.8047` n `102`; fx avg `-0.1121` n `6`; index avg `-0.3609` n `25`; metal avg `-0.0057` n `20`; unknown avg `0.0741` n `758`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1281`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
