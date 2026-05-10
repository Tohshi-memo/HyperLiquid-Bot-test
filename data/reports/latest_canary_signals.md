# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-10T13:22:14.500683+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0241` n `12`; crypto_alt avg `0.2761` n `228`; crypto_major avg `0.2308` n `8`; equity avg `0.0179` n `65`; fx avg `0.0` n `5`; index avg `0.0071` n `23`; metal avg `0.1523` n `18`; unknown avg `-0.1375` n `376`
- 1h: commodity avg `-0.1615` n `12`; crypto_alt avg `0.4403` n `228`; crypto_major avg `0.2445` n `8`; equity avg `0.0063` n `65`; fx avg `-0.0002` n `5`; index avg `-0.0194` n `23`; metal avg `0.2241` n `18`; unknown avg `-0.2459` n `376`
- 4h: commodity avg `-0.0308` n `12`; crypto_alt avg `0.1124` n `228`; crypto_major avg `-0.1865` n `8`; equity avg `0.0299` n `65`; fx avg `-0.0102` n `5`; index avg `-0.0045` n `23`; metal avg `0.3127` n `18`; unknown avg `-0.1333` n `376`
- 24h: commodity avg `-0.027` n `12`; crypto_alt avg `0.5928` n `228`; crypto_major avg `0.0604` n `8`; equity avg `0.9084` n `65`; fx avg `-0.0276` n `5`; index avg `0.2712` n `23`; metal avg `0.7211` n `18`; unknown avg `0.2886` n `366`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1259`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1018`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
