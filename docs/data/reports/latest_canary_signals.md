# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-29T03:37:15.583021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0758` n `12`; crypto_alt avg `-0.0987` n `228`; crypto_major avg `-0.0857` n `8`; equity avg `-0.0101` n `69`; fx avg `0.0035` n `6`; index avg `-0.0351` n `23`; metal avg `-0.0512` n `18`; unknown avg `-0.0958` n `417`
- 1h: commodity avg `-0.0397` n `12`; crypto_alt avg `-0.3366` n `228`; crypto_major avg `0.0549` n `8`; equity avg `0.1743` n `69`; fx avg `0.0077` n `6`; index avg `-0.0026` n `23`; metal avg `-0.1934` n `18`; unknown avg `-0.1018` n `417`
- 4h: commodity avg `-0.2113` n `12`; crypto_alt avg `-0.264` n `228`; crypto_major avg `-0.4556` n `8`; equity avg `-0.0462` n `69`; fx avg `0.0628` n `6`; index avg `-0.1119` n `23`; metal avg `-0.1509` n `18`; unknown avg `-0.3469` n `417`
- 24h: commodity avg `-0.2336` n `12`; crypto_alt avg `-0.2923` n `228`; crypto_major avg `1.1507` n `8`; equity avg `4.0198` n `69`; fx avg `0.0846` n `6`; index avg `1.3588` n `23`; metal avg `2.1346` n `18`; unknown avg `0.4835` n `407`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1624`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1614`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1486`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1268`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
