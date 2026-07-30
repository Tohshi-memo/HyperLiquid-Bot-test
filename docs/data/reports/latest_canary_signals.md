# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T23:07:30.917279+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0046` n `12`; crypto_alt avg `0.0194` n `230`; crypto_major avg `0.0167` n `8`; equity avg `0.0261` n `102`; fx avg `-0.0215` n `6`; index avg `-0.0163` n `25`; metal avg `0.004` n `20`; unknown avg `-0.1527` n `779`
- 1h: commodity avg `-0.0276` n `12`; crypto_alt avg `-0.0308` n `230`; crypto_major avg `0.1287` n `8`; equity avg `0.1163` n `102`; fx avg `-0.0023` n `6`; index avg `0.0291` n `25`; metal avg `0.0276` n `20`; unknown avg `-0.2234` n `779`
- 4h: commodity avg `0.058` n `12`; crypto_alt avg `0.1443` n `230`; crypto_major avg `0.2146` n `8`; equity avg `1.1995` n `102`; fx avg `0.0467` n `6`; index avg `0.1249` n `25`; metal avg `0.0647` n `20`; unknown avg `-0.3412` n `779`
- 24h: commodity avg `-0.0514` n `12`; crypto_alt avg `0.9521` n `230`; crypto_major avg `1.8388` n `8`; equity avg `7.5562` n `102`; fx avg `-0.4286` n `6`; index avg `0.8648` n `25`; metal avg `0.4534` n `20`; unknown avg `0.1048` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0855`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
