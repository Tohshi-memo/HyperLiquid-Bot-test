# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T09:52:28.263323+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.08` n `13`; crypto_alt avg `-0.0332` n `239`; crypto_major avg `-0.1589` n `8`; equity avg `-0.2604` n `158`; fx avg `-0.0028` n `6`; index avg `-0.0209` n `27`; metal avg `-0.0612` n `20`; unknown avg `0.0712` n `1256`
- 1h: commodity avg `-0.2538` n `13`; crypto_alt avg `0.3088` n `239`; crypto_major avg `0.4426` n `8`; equity avg `1.0287` n `158`; fx avg `-0.034` n `6`; index avg `0.1322` n `27`; metal avg `-0.0579` n `20`; unknown avg `30.7506` n `1250`
- 4h: commodity avg `-0.4589` n `13`; crypto_alt avg `0.7097` n `239`; crypto_major avg `0.4513` n `8`; equity avg `1.643` n `158`; fx avg `-0.1488` n `6`; index avg `0.2036` n `27`; metal avg `0.2391` n `20`; unknown avg `16.2121` n `1172`
- 24h: commodity avg `0.5163` n `13`; crypto_alt avg `-3.9011` n `239`; crypto_major avg `-5.5858` n `8`; equity avg `-4.91` n `158`; fx avg `-0.033` n `6`; index avg `-0.6199` n `27`; metal avg `-0.2608` n `20`; unknown avg `227.3473` n `1071`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2203`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1738`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.169`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1039`, n `668`, weak_sample_signal
