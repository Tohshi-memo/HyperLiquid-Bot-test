# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T12:22:34.019888+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0441` n `13`; crypto_alt avg `-0.3202` n `239`; crypto_major avg `-0.2805` n `8`; equity avg `-0.401` n `158`; fx avg `0.0108` n `6`; index avg `-0.0323` n `27`; metal avg `0.0433` n `20`; unknown avg `0.4341` n `1264`
- 1h: commodity avg `-0.1224` n `13`; crypto_alt avg `-0.9417` n `239`; crypto_major avg `-0.7976` n `8`; equity avg `-1.4163` n `158`; fx avg `0.0176` n `6`; index avg `-0.0718` n `27`; metal avg `-0.0345` n `20`; unknown avg `0.6618` n `1252`
- 4h: commodity avg `-0.3029` n `13`; crypto_alt avg `-0.7134` n `239`; crypto_major avg `-0.3948` n `8`; equity avg `-0.6374` n `158`; fx avg `0.0595` n `6`; index avg `0.0699` n `27`; metal avg `0.1387` n `20`; unknown avg `10.9966` n `1176`
- 24h: commodity avg `-0.6081` n `13`; crypto_alt avg `0.793` n `239`; crypto_major avg `0.1612` n `8`; equity avg `1.201` n `158`; fx avg `0.1442` n `6`; index avg `0.1747` n `27`; metal avg `1.0142` n `20`; unknown avg `1.4601` n `1087`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2519`, n `668`, moderate_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1528`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1525`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1395`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1384`, n `668`, weak_sample_signal
