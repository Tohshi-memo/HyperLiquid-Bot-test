# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T04:07:26.241808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0493` n `13`; crypto_alt avg `-0.0579` n `239`; crypto_major avg `-0.0572` n `8`; equity avg `-0.2158` n `158`; fx avg `-0.0028` n `6`; index avg `-0.046` n `27`; metal avg `-0.0166` n `20`; unknown avg `19.6546` n `1253`
- 1h: commodity avg `0.0525` n `13`; crypto_alt avg `-0.0713` n `239`; crypto_major avg `0.0003` n `8`; equity avg `-0.1774` n `158`; fx avg `-0.0026` n `6`; index avg `-0.0086` n `27`; metal avg `0.0174` n `20`; unknown avg `19.4409` n `1246`
- 4h: commodity avg `0.2967` n `13`; crypto_alt avg `1.1634` n `239`; crypto_major avg `0.5871` n `8`; equity avg `1.5401` n `158`; fx avg `-0.0278` n `6`; index avg `0.2154` n `27`; metal avg `0.4031` n `20`; unknown avg `0.8134` n `1236`
- 24h: commodity avg `0.1948` n `13`; crypto_alt avg `-1.8476` n `239`; crypto_major avg `-2.3701` n `8`; equity avg `0.5114` n `158`; fx avg `-0.0765` n `6`; index avg `0.0688` n `27`; metal avg `0.4756` n `20`; unknown avg `1.3074` n `988`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.17`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1588`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1284`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1137`, n `668`, weak_sample_signal
