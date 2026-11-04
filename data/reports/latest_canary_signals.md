# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T12:37:26.024501+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.022` n `13`; crypto_alt avg `0.1431` n `239`; crypto_major avg `-0.0003` n `8`; equity avg `0.0495` n `158`; fx avg `-0.005` n `6`; index avg `0.0071` n `27`; metal avg `0.0235` n `20`; unknown avg `-0.0643` n `1264`
- 1h: commodity avg `-0.0581` n `13`; crypto_alt avg `-0.8322` n `239`; crypto_major avg `-0.9608` n `8`; equity avg `-1.2148` n `158`; fx avg `0.0111` n `6`; index avg `-0.079` n `27`; metal avg `0.0042` n `20`; unknown avg `0.5827` n `1252`
- 4h: commodity avg `-0.4003` n `13`; crypto_alt avg `-0.6167` n `239`; crypto_major avg `-0.457` n `8`; equity avg `-0.5155` n `158`; fx avg `0.0504` n `6`; index avg `0.0718` n `27`; metal avg `0.1431` n `20`; unknown avg `11.6183` n `1208`
- 24h: commodity avg `-0.5256` n `13`; crypto_alt avg `0.6951` n `239`; crypto_major avg `0.1522` n `8`; equity avg `1.0501` n `158`; fx avg `0.156` n `6`; index avg `0.1534` n `27`; metal avg `0.972` n `20`; unknown avg `0.1338` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2505`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1597`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1402`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
