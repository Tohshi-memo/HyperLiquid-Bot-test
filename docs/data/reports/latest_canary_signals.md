# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T05:52:15.514366+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0173` n `12`; crypto_alt avg `-0.0041` n `228`; crypto_major avg `-0.0438` n `8`; equity avg `0.0045` n `65`; fx avg `0.0013` n `5`; index avg `0.0031` n `23`; metal avg `0.2041` n `18`; unknown avg `0.1592` n `376`
- 1h: commodity avg `-0.0136` n `12`; crypto_alt avg `0.2611` n `228`; crypto_major avg `-0.0114` n `8`; equity avg `-0.0483` n `65`; fx avg `0.0004` n `5`; index avg `-0.006` n `23`; metal avg `0.3328` n `18`; unknown avg `-0.2616` n `376`
- 4h: commodity avg `-0.1338` n `12`; crypto_alt avg `0.7074` n `228`; crypto_major avg `0.2441` n `8`; equity avg `0.3505` n `65`; fx avg `0.0036` n `5`; index avg `0.0709` n `23`; metal avg `0.5618` n `18`; unknown avg `-0.2687` n `376`
- 24h: commodity avg `0.1867` n `12`; crypto_alt avg `-1.3804` n `228`; crypto_major avg `-0.6703` n `8`; equity avg `0.9783` n `65`; fx avg `-0.0246` n `5`; index avg `0.3448` n `23`; metal avg `0.7174` n `18`; unknown avg `-0.5005` n `356`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0996`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0966`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.09`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0692`, n `668`, weak_sample_signal
