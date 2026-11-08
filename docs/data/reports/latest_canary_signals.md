# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T16:37:26.023157+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0013` n `13`; crypto_alt avg `-0.0158` n `239`; crypto_major avg `-0.0541` n `8`; equity avg `0.01` n `158`; fx avg `0.0159` n `6`; index avg `0.0052` n `27`; metal avg `0.004` n `20`; unknown avg `0.2503` n `1262`
- 1h: commodity avg `0.0159` n `13`; crypto_alt avg `-0.1538` n `239`; crypto_major avg `-0.1236` n `8`; equity avg `0.0512` n `158`; fx avg `0.0312` n `6`; index avg `0.0088` n `27`; metal avg `0.0133` n `20`; unknown avg `-0.6127` n `1242`
- 4h: commodity avg `0.0184` n `13`; crypto_alt avg `-0.267` n `239`; crypto_major avg `-0.0906` n `8`; equity avg `-0.0873` n `158`; fx avg `0.027` n `6`; index avg `-0.0064` n `27`; metal avg `-0.0309` n `20`; unknown avg `0.0586` n `1234`
- 24h: commodity avg `0.0769` n `13`; crypto_alt avg `-1.4041` n `239`; crypto_major avg `-0.048` n `8`; equity avg `0.2163` n `158`; fx avg `0.0838` n `6`; index avg `-0.0049` n `27`; metal avg `-0.0354` n `20`; unknown avg `7.6945` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1493`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
