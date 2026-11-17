# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T19:22:24.614422+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1264` n `13`; crypto_alt avg `0.2942` n `239`; crypto_major avg `0.1807` n `8`; equity avg `0.1156` n `163`; fx avg `-0.0195` n `6`; index avg `0.0171` n `27`; metal avg `0.0345` n `20`; unknown avg `0.1621` n `1263`
- 1h: commodity avg `-0.0947` n `13`; crypto_alt avg `0.2441` n `239`; crypto_major avg `0.1519` n `8`; equity avg `0.2399` n `163`; fx avg `-0.0175` n `6`; index avg `0.0195` n `27`; metal avg `-0.0214` n `20`; unknown avg `0.6428` n `1263`
- 4h: commodity avg `0.0918` n `13`; crypto_alt avg `-1.2696` n `239`; crypto_major avg `-1.033` n `8`; equity avg `-0.5704` n `163`; fx avg `0.028` n `6`; index avg `-0.0492` n `27`; metal avg `-0.0982` n `20`; unknown avg `0.1473` n `1245`
- 24h: commodity avg `0.2046` n `13`; crypto_alt avg `-0.4613` n `239`; crypto_major avg `0.0023` n `8`; equity avg `-1.8026` n `163`; fx avg `0.0298` n `6`; index avg `-0.2019` n `27`; metal avg `-0.0504` n `20`; unknown avg `8.2566` n `1099`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.167`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1207`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1034`, n `668`, weak_sample_signal
