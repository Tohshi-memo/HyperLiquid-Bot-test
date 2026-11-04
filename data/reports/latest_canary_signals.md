# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T13:37:32.188768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.154` n `13`; crypto_alt avg `0.0372` n `239`; crypto_major avg `-0.0069` n `8`; equity avg `0.3885` n `158`; fx avg `0.0003` n `6`; index avg `0.003` n `27`; metal avg `-0.0028` n `20`; unknown avg `0.2078` n `1264`
- 1h: commodity avg `-0.148` n `13`; crypto_alt avg `-0.2012` n `239`; crypto_major avg `-0.0066` n `8`; equity avg `-0.3091` n `158`; fx avg `0.0162` n `6`; index avg `-0.0268` n `27`; metal avg `-0.0955` n `20`; unknown avg `0.0881` n `1258`
- 4h: commodity avg `-0.4714` n `13`; crypto_alt avg `-0.503` n `239`; crypto_major avg `-0.4419` n `8`; equity avg `-1.0589` n `158`; fx avg `-0.0049` n `6`; index avg `-0.0475` n `27`; metal avg `-0.0657` n `20`; unknown avg `1.2085` n `1252`
- 24h: commodity avg `-0.0505` n `13`; crypto_alt avg `0.366` n `239`; crypto_major avg `-0.0395` n `8`; equity avg `-0.0046` n `158`; fx avg `0.1894` n `6`; index avg `0.0057` n `27`; metal avg `0.5811` n `20`; unknown avg `183.7701` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2513`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1693`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1579`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1501`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.144`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
