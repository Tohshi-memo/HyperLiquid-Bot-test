# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T19:52:45.820356+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0396` n `12`; crypto_alt avg `0.1166` n `230`; crypto_major avg `0.0311` n `8`; equity avg `0.0634` n `102`; fx avg `0.0056` n `6`; index avg `0.0017` n `25`; metal avg `-0.0073` n `20`; unknown avg `-0.0123` n `779`
- 1h: commodity avg `0.0297` n `12`; crypto_alt avg `0.2328` n `230`; crypto_major avg `0.2506` n `8`; equity avg `0.5467` n `102`; fx avg `0.0445` n `6`; index avg `0.0719` n `25`; metal avg `0.1177` n `20`; unknown avg `-0.1362` n `779`
- 4h: commodity avg `-0.0898` n `12`; crypto_alt avg `0.1951` n `230`; crypto_major avg `0.4416` n `8`; equity avg `0.8334` n `102`; fx avg `-0.009` n `6`; index avg `0.1457` n `25`; metal avg `0.1554` n `20`; unknown avg `-0.1605` n `779`
- 24h: commodity avg `-0.1756` n `12`; crypto_alt avg `1.3822` n `230`; crypto_major avg `2.2734` n `8`; equity avg `6.036` n `102`; fx avg `-0.3793` n `6`; index avg `0.7955` n `25`; metal avg `0.6354` n `20`; unknown avg `0.1271` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0846`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
