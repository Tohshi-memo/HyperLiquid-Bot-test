# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T15:52:29.198114+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0806` n `12`; crypto_alt avg `0.0248` n `228`; crypto_major avg `-0.0141` n `8`; equity avg `0.0475` n `74`; fx avg `0.0065` n `6`; index avg `0.0036` n `23`; metal avg `-0.0314` n `18`; unknown avg `-0.1585` n `645`
- 1h: commodity avg `0.1359` n `12`; crypto_alt avg `0.4634` n `228`; crypto_major avg `0.4018` n `8`; equity avg `0.2592` n `74`; fx avg `-0.0204` n `6`; index avg `0.1539` n `23`; metal avg `-0.0274` n `18`; unknown avg `0.0792` n `645`
- 4h: commodity avg `0.3702` n `12`; crypto_alt avg `-0.9277` n `228`; crypto_major avg `-0.8697` n `8`; equity avg `-0.3073` n `74`; fx avg `-0.0213` n `6`; index avg `0.0967` n `23`; metal avg `-0.1507` n `18`; unknown avg `0.0304` n `645`
- 24h: commodity avg `0.0306` n `12`; crypto_alt avg `-1.6664` n `228`; crypto_major avg `-0.9217` n `8`; equity avg `0.3854` n `74`; fx avg `-0.0162` n `6`; index avg `0.1789` n `23`; metal avg `-0.1896` n `18`; unknown avg `1.3903` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
