# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T19:37:29.232744+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0212` n `12`; crypto_alt avg `0.1576` n `230`; crypto_major avg `0.1346` n `8`; equity avg `-0.1617` n `102`; fx avg `-0.0031` n `6`; index avg `-0.0223` n `25`; metal avg `-0.0031` n `20`; unknown avg `-0.0784` n `776`
- 1h: commodity avg `-0.0917` n `12`; crypto_alt avg `0.2303` n `230`; crypto_major avg `0.2022` n `8`; equity avg `0.4217` n `102`; fx avg `0.0166` n `6`; index avg `0.0322` n `25`; metal avg `0.0115` n `20`; unknown avg `-0.087` n `775`
- 4h: commodity avg `-0.0025` n `12`; crypto_alt avg `-0.3638` n `230`; crypto_major avg `-0.2518` n `8`; equity avg `0.0474` n `102`; fx avg `-0.0105` n `6`; index avg `-0.0649` n `25`; metal avg `-0.0715` n `20`; unknown avg `-0.4239` n `774`
- 24h: commodity avg `-0.9589` n `12`; crypto_alt avg `-1.9438` n `230`; crypto_major avg `-1.8518` n `8`; equity avg `-3.1804` n `102`; fx avg `-0.0959` n `6`; index avg `-0.3872` n `25`; metal avg `-0.4726` n `20`; unknown avg `-0.5018` n `758`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
