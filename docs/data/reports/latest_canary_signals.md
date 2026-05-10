# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T05:22:15.590263+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0089` n `12`; crypto_alt avg `0.1729` n `228`; crypto_major avg `0.0551` n `8`; equity avg `0.0004` n `65`; fx avg `-0.0008` n `5`; index avg `0.0013` n `23`; metal avg `0.0208` n `18`; unknown avg `0.0299` n `376`
- 1h: commodity avg `0.0308` n `12`; crypto_alt avg `0.2097` n `228`; crypto_major avg `0.0468` n `8`; equity avg `0.016` n `65`; fx avg `-0.0002` n `5`; index avg `0.0089` n `23`; metal avg `0.0451` n `18`; unknown avg `0.1096` n `376`
- 4h: commodity avg `-0.1336` n `12`; crypto_alt avg `0.7319` n `228`; crypto_major avg `0.4383` n `8`; equity avg `0.3543` n `65`; fx avg `0.0023` n `5`; index avg `0.0632` n `23`; metal avg `0.2238` n `18`; unknown avg `0.0645` n `376`
- 24h: commodity avg `0.2271` n `12`; crypto_alt avg `-1.4231` n `228`; crypto_major avg `-0.6767` n `8`; equity avg `1.001` n `65`; fx avg `-0.0064` n `5`; index avg `0.3155` n `23`; metal avg `0.3803` n `18`; unknown avg `-0.1661` n `356`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0985`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `668`, weak_sample_signal
