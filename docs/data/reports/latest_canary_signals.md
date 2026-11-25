# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T08:52:24.139931+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1804` n `13`; crypto_alt avg `-0.0106` n `239`; crypto_major avg `-0.0001` n `8`; equity avg `-0.2359` n `168`; fx avg `0.0094` n `6`; index avg `-0.0309` n `27`; metal avg `-0.0528` n `20`; unknown avg `0.7791` n `1265`
- 1h: commodity avg `0.2336` n `13`; crypto_alt avg `0.3719` n `239`; crypto_major avg `0.6027` n `8`; equity avg `0.5401` n `168`; fx avg `0.0542` n `6`; index avg `0.0867` n `27`; metal avg `0.1032` n `20`; unknown avg `1.1456` n `1243`
- 4h: commodity avg `-0.0555` n `13`; crypto_alt avg `0.4187` n `239`; crypto_major avg `-0.0051` n `8`; equity avg `-0.6772` n `168`; fx avg `0.0012` n `6`; index avg `-0.0467` n `27`; metal avg `-0.1503` n `20`; unknown avg `366.6111` n `1209`
- 24h: commodity avg `0.383` n `13`; crypto_alt avg `-2.5208` n `239`; crypto_major avg `-3.0219` n `8`; equity avg `-5.1449` n `167`; fx avg `0.1127` n `6`; index avg `-0.4512` n `27`; metal avg `-0.9002` n `20`; unknown avg `724.8296` n `1033`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.13`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
