# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T19:07:27.992605+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0225` n `13`; crypto_alt avg `-0.1922` n `239`; crypto_major avg `-0.1842` n `8`; equity avg `-0.0884` n `158`; fx avg `0.0062` n `6`; index avg `-0.0052` n `27`; metal avg `0.0` n `20`; unknown avg `0.0926` n `1258`
- 1h: commodity avg `-0.0778` n `13`; crypto_alt avg `0.3724` n `239`; crypto_major avg `0.1289` n `8`; equity avg `0.2683` n `158`; fx avg `-0.0123` n `6`; index avg `0.0362` n `27`; metal avg `0.0135` n `20`; unknown avg `3.2651` n `1232`
- 4h: commodity avg `-0.1551` n `13`; crypto_alt avg `-0.1192` n `239`; crypto_major avg `-0.2581` n `8`; equity avg `0.2071` n `158`; fx avg `0.0209` n `6`; index avg `0.0315` n `27`; metal avg `0.004` n `20`; unknown avg `1.1733` n `1194`
- 24h: commodity avg `-0.0792` n `13`; crypto_alt avg `-1.701` n `239`; crypto_major avg `-0.3311` n `8`; equity avg `0.3205` n `158`; fx avg `0.0678` n `6`; index avg `-0.0019` n `27`; metal avg `-0.0317` n `20`; unknown avg `0.2701` n `1046`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
