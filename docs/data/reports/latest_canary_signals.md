# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T06:07:31.685596+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0348` n `13`; crypto_alt avg `-0.3067` n `239`; crypto_major avg `-0.227` n `8`; equity avg `-0.2504` n `158`; fx avg `-0.0242` n `6`; index avg `-0.0482` n `27`; metal avg `0.0164` n `20`; unknown avg `-0.1713` n `1226`
- 1h: commodity avg `0.0992` n `13`; crypto_alt avg `-0.1548` n `239`; crypto_major avg `-0.2101` n `8`; equity avg `-0.5429` n `158`; fx avg `0.005` n `6`; index avg `-0.0797` n `27`; metal avg `-0.0635` n `20`; unknown avg `-0.085` n `1222`
- 4h: commodity avg `0.1462` n `13`; crypto_alt avg `-0.0863` n `239`; crypto_major avg `-0.7842` n `8`; equity avg `-0.3016` n `158`; fx avg `-0.018` n `6`; index avg `-0.0249` n `27`; metal avg `-0.1517` n `20`; unknown avg `-0.1371` n `1212`
- 24h: commodity avg `1.3741` n `13`; crypto_alt avg `-4.2804` n `239`; crypto_major avg `-5.8398` n `8`; equity avg `-5.859` n `158`; fx avg `0.0231` n `6`; index avg `-0.7572` n `27`; metal avg `-0.4507` n `20`; unknown avg `231.0251` n `1031`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1739`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1736`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1573`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1532`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
