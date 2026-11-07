# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T18:16:38.760177+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0197` n `13`; crypto_alt avg `0.1019` n `239`; crypto_major avg `0.1183` n `8`; equity avg `0.0461` n `158`; fx avg `-0.0011` n `6`; index avg `0.0085` n `27`; metal avg `0.0028` n `20`; unknown avg `-0.0015` n `1262`
- 1h: commodity avg `-0.0458` n `13`; crypto_alt avg `0.3024` n `239`; crypto_major avg `0.2296` n `8`; equity avg `0.1219` n `158`; fx avg `-0.0108` n `6`; index avg `0.0037` n `27`; metal avg `0.0036` n `20`; unknown avg `0.5975` n `1224`
- 4h: commodity avg `0.0002` n `13`; crypto_alt avg `0.0911` n `239`; crypto_major avg `-0.0933` n `8`; equity avg `-0.0126` n `158`; fx avg `-0.0133` n `6`; index avg `0.025` n `27`; metal avg `-0.0218` n `20`; unknown avg `165.6307` n `1209`
- 24h: commodity avg `0.1442` n `13`; crypto_alt avg `-1.1677` n `239`; crypto_major avg `-0.3874` n `8`; equity avg `0.9177` n `158`; fx avg `0.0036` n `6`; index avg `0.0989` n `27`; metal avg `0.0292` n `20`; unknown avg `0.1091` n `1077`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2136`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1649`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
