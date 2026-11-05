# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-05T09:07:38.537191+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0622` n `13`; crypto_alt avg `-0.1649` n `239`; crypto_major avg `-0.1773` n `8`; equity avg `-0.1478` n `158`; fx avg `0.014` n `6`; index avg `0.0097` n `27`; metal avg `0.0151` n `20`; unknown avg `0.981` n `1205`
- 1h: commodity avg `0.106` n `13`; crypto_alt avg `0.6479` n `239`; crypto_major avg `0.2343` n `8`; equity avg `-0.058` n `158`; fx avg `0.0453` n `6`; index avg `-0.0118` n `27`; metal avg `0.0659` n `20`; unknown avg `0.9891` n `1205`
- 4h: commodity avg `0.4048` n `13`; crypto_alt avg `0.4051` n `239`; crypto_major avg `0.22` n `8`; equity avg `0.0216` n `158`; fx avg `-0.0114` n `6`; index avg `0.0091` n `27`; metal avg `-0.0596` n `20`; unknown avg `0.6066` n `1159`
- 24h: commodity avg `-1.7007` n `13`; crypto_alt avg `0.9696` n `239`; crypto_major avg `1.8131` n `8`; equity avg `-2.6904` n `158`; fx avg `0.0047` n `6`; index avg `-0.1924` n `27`; metal avg `0.7159` n `20`; unknown avg `29.4024` n `1070`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2466`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1871`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1851`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1498`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1353`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1302`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
