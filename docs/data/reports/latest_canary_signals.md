# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T22:22:32.014709+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0198` n `13`; crypto_alt avg `-0.0847` n `239`; crypto_major avg `-0.1093` n `8`; equity avg `-0.0954` n `168`; fx avg `-0.0047` n `6`; index avg `-0.0222` n `27`; metal avg `0.021` n `20`; unknown avg `0.7965` n `1263`
- 1h: commodity avg `0.0294` n `13`; crypto_alt avg `-0.2701` n `239`; crypto_major avg `-0.481` n `8`; equity avg `-0.2495` n `168`; fx avg `-0.0022` n `6`; index avg `-0.0151` n `27`; metal avg `0.0047` n `20`; unknown avg `0.6867` n `1229`
- 4h: commodity avg `0.0614` n `13`; crypto_alt avg `-0.231` n `239`; crypto_major avg `-0.5182` n `8`; equity avg `-0.3778` n `168`; fx avg `-0.0051` n `6`; index avg `-0.0115` n `27`; metal avg `0.1215` n `20`; unknown avg `180.7747` n `1154`
- 24h: commodity avg `-0.4438` n `13`; crypto_alt avg `-0.1451` n `239`; crypto_major avg `-0.2114` n `8`; equity avg `2.9818` n `168`; fx avg `-0.1654` n `6`; index avg `0.3028` n `27`; metal avg `0.973` n `20`; unknown avg `270.5015` n `1003`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1303`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1056`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.093`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0691`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
