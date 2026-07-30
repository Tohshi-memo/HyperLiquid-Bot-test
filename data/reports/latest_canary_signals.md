# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T21:07:37.706332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `-0.1365` n `230`; crypto_major avg `-0.0058` n `8`; equity avg `0.051` n `102`; fx avg `-0.0141` n `6`; index avg `-0.0214` n `25`; metal avg `0.0378` n `20`; unknown avg `0.0221` n `779`
- 1h: commodity avg `0.0605` n `12`; crypto_alt avg `-0.2959` n `230`; crypto_major avg `-0.2142` n `8`; equity avg `0.0956` n `102`; fx avg `0.0011` n `6`; index avg `-0.0708` n `25`; metal avg `-0.0517` n `20`; unknown avg `0.0318` n `779`
- 4h: commodity avg `-0.0438` n `12`; crypto_alt avg `0.2073` n `230`; crypto_major avg `0.0693` n `8`; equity avg `0.969` n `102`; fx avg `-0.04` n `6`; index avg `0.0891` n `25`; metal avg `0.1133` n `20`; unknown avg `-0.1145` n `779`
- 24h: commodity avg `-0.1351` n `12`; crypto_alt avg `2.0579` n `230`; crypto_major avg `2.5117` n `8`; equity avg `7.9779` n `102`; fx avg `-0.3951` n `6`; index avg `0.9871` n `25`; metal avg `0.688` n `20`; unknown avg `0.2586` n `738`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0836`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
