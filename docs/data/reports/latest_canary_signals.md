# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T19:52:25.259653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0956` n `12`; crypto_alt avg `-0.0765` n `228`; crypto_major avg `0.0904` n `8`; equity avg `-0.0022` n `69`; fx avg `0.0074` n `6`; index avg `-0.0253` n `23`; metal avg `-0.079` n `18`; unknown avg `-0.1493` n `417`
- 1h: commodity avg `-0.2399` n `12`; crypto_alt avg `-0.442` n `228`; crypto_major avg `-0.2738` n `8`; equity avg `0.0217` n `69`; fx avg `0.0` n `6`; index avg `0.0295` n `23`; metal avg `-0.0443` n `18`; unknown avg `0.0465` n `417`
- 4h: commodity avg `-0.2863` n `12`; crypto_alt avg `1.6435` n `228`; crypto_major avg `1.6259` n `8`; equity avg `0.8402` n `69`; fx avg `-0.015` n `6`; index avg `0.2064` n `23`; metal avg `0.3737` n `18`; unknown avg `0.4535` n `417`
- 24h: commodity avg `0.8457` n `12`; crypto_alt avg `-3.6609` n `228`; crypto_major avg `-1.0607` n `8`; equity avg `1.6748` n `69`; fx avg `-0.024` n `6`; index avg `0.9507` n `23`; metal avg `0.5259` n `18`; unknown avg `-0.8201` n `407`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.191`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1339`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
