# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T00:52:27.786249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0392` n `13`; crypto_alt avg `0.0871` n `239`; crypto_major avg `0.1479` n `8`; equity avg `-0.144` n `158`; fx avg `-0.0389` n `6`; index avg `-0.005` n `27`; metal avg `0.1029` n `20`; unknown avg `-0.2279` n `1264`
- 1h: commodity avg `-0.101` n `13`; crypto_alt avg `0.0062` n `239`; crypto_major avg `0.2156` n `8`; equity avg `-0.511` n `158`; fx avg `-0.018` n `6`; index avg `-0.1065` n `27`; metal avg `0.1398` n `20`; unknown avg `0.8755` n `1252`
- 4h: commodity avg `-0.1977` n `13`; crypto_alt avg `0.6672` n `239`; crypto_major avg `0.8315` n `8`; equity avg `-0.3088` n `158`; fx avg `-0.0187` n `6`; index avg `-0.0804` n `27`; metal avg `0.204` n `20`; unknown avg `0.3392` n `1172`
- 24h: commodity avg `-1.888` n `13`; crypto_alt avg `2.7596` n `239`; crypto_major avg `3.4784` n `8`; equity avg `-1.063` n `158`; fx avg `0.0044` n `6`; index avg `0.0817` n `27`; metal avg `1.4723` n `20`; unknown avg `30.8595` n `1036`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2651`, n `668`, moderate_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1472`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1467`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1349`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1296`, n `668`, weak_sample_signal
