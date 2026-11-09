# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T04:22:32.835389+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0295` n `13`; crypto_alt avg `-0.1619` n `239`; crypto_major avg `-0.0821` n `8`; equity avg `-0.2135` n `158`; fx avg `-0.0115` n `6`; index avg `-0.0296` n `27`; metal avg `0.0214` n `20`; unknown avg `-0.0826` n `1261`
- 1h: commodity avg `0.0748` n `13`; crypto_alt avg `0.0362` n `239`; crypto_major avg `0.1786` n `8`; equity avg `-0.2465` n `158`; fx avg `-0.0183` n `6`; index avg `-0.0126` n `27`; metal avg `0.0222` n `20`; unknown avg `19.3279` n `1246`
- 4h: commodity avg `0.3405` n `13`; crypto_alt avg `0.5288` n `239`; crypto_major avg `0.1872` n `8`; equity avg `1.1562` n `158`; fx avg `-0.0187` n `6`; index avg `0.1608` n `27`; metal avg `0.3695` n `20`; unknown avg `0.9287` n `1234`
- 24h: commodity avg `0.1984` n `13`; crypto_alt avg `-1.9083` n `239`; crypto_major avg `-2.3997` n `8`; equity avg `0.3341` n `158`; fx avg `-0.0865` n `6`; index avg `0.0435` n `27`; metal avg `0.4979` n `20`; unknown avg `1.289` n `986`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1358`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1289`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
