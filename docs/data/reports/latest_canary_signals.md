# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T00:22:28.988974+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0456` n `12`; crypto_alt avg `-0.0658` n `230`; crypto_major avg `-0.0845` n `8`; equity avg `0.1825` n `102`; fx avg `0.0091` n `6`; index avg `0.0471` n `25`; metal avg `0.0011` n `20`; unknown avg `0.1058` n `779`
- 1h: commodity avg `0.0501` n `12`; crypto_alt avg `-0.1209` n `230`; crypto_major avg `-0.27` n `8`; equity avg `0.6089` n `102`; fx avg `0.1066` n `6`; index avg `0.2265` n `25`; metal avg `0.0003` n `20`; unknown avg `0.0411` n `779`
- 4h: commodity avg `0.0486` n `12`; crypto_alt avg `-0.1694` n `230`; crypto_major avg `-0.1273` n `8`; equity avg `1.0914` n `102`; fx avg `0.1415` n `6`; index avg `0.215` n `25`; metal avg `-0.0377` n `20`; unknown avg `-0.296` n `779`
- 24h: commodity avg `0.1847` n `12`; crypto_alt avg `0.5297` n `230`; crypto_major avg `1.2198` n `8`; equity avg `7.5654` n `102`; fx avg `-0.2095` n `6`; index avg `1.0123` n `25`; metal avg `0.5501` n `20`; unknown avg `0.0828` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.142`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
