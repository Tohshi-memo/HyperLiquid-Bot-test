# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T13:07:31.435792+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1423` n `13`; crypto_alt avg `-0.047` n `239`; crypto_major avg `0.0817` n `8`; equity avg `-0.06` n `158`; fx avg `0.0035` n `6`; index avg `-0.0019` n `27`; metal avg `-0.0636` n `20`; unknown avg `0.05` n `1258`
- 1h: commodity avg `-0.0501` n `13`; crypto_alt avg `-0.3815` n `239`; crypto_major avg `-0.3163` n `8`; equity avg `-1.1489` n `158`; fx avg `0.0221` n `6`; index avg `-0.0805` n `27`; metal avg `-0.0125` n `20`; unknown avg `0.1356` n `1258`
- 4h: commodity avg `-0.3762` n `13`; crypto_alt avg `-0.4926` n `239`; crypto_major avg `-0.4038` n `8`; equity avg `-1.1786` n `158`; fx avg `0.028` n `6`; index avg `0.0128` n `27`; metal avg `0.0452` n `20`; unknown avg `18.1184` n `1244`
- 24h: commodity avg `-0.582` n `13`; crypto_alt avg `0.6538` n `239`; crypto_major avg `0.2471` n `8`; equity avg `0.2052` n `158`; fx avg `0.1712` n `6`; index avg `0.0968` n `27`; metal avg `0.7546` n `20`; unknown avg `-0.1555` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2513`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1654`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1381`, n `668`, weak_sample_signal
