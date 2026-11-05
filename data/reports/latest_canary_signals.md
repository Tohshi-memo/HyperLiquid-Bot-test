# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T11:37:33.818001+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0438` n `13`; crypto_alt avg `-0.0602` n `239`; crypto_major avg `-0.0779` n `8`; equity avg `0.0439` n `158`; fx avg `-0.0127` n `6`; index avg `0.0097` n `27`; metal avg `0.0088` n `20`; unknown avg `0.1208` n `1255`
- 1h: commodity avg `0.0474` n `13`; crypto_alt avg `-0.015` n `239`; crypto_major avg `-0.0823` n `8`; equity avg `-0.1088` n `158`; fx avg `-0.0129` n `6`; index avg `0.0003` n `27`; metal avg `0.1035` n `20`; unknown avg `37.3384` n `1247`
- 4h: commodity avg `0.2935` n `13`; crypto_alt avg `0.1556` n `239`; crypto_major avg `0.1505` n `8`; equity avg `0.1596` n `158`; fx avg `-0.0066` n `6`; index avg `0.0446` n `27`; metal avg `0.1967` n `20`; unknown avg `42.1744` n `1135`
- 24h: commodity avg `-1.185` n `13`; crypto_alt avg `0.004` n `239`; crypto_major avg `1.0606` n `8`; equity avg `-3.2773` n `158`; fx avg `-0.0333` n `6`; index avg `-0.2856` n `27`; metal avg `0.7132` n `20`; unknown avg `44.0703` n `1068`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2404`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.2004`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1415`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1413`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1328`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
