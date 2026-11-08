# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T16:52:27.272739+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `-0.4003` n `239`; crypto_major avg `-0.2694` n `8`; equity avg `-0.0507` n `158`; fx avg `-0.0015` n `6`; index avg `-0.0057` n `27`; metal avg `-0.0109` n `20`; unknown avg `0.3388` n `1262`
- 1h: commodity avg `0.0258` n `13`; crypto_alt avg `-0.6245` n `239`; crypto_major avg `-0.3863` n `8`; equity avg `-0.041` n `158`; fx avg `0.0269` n `6`; index avg `-0.0007` n `27`; metal avg `-0.0007` n `20`; unknown avg `-0.1335` n `1242`
- 4h: commodity avg `0.0198` n `13`; crypto_alt avg `-0.6619` n `239`; crypto_major avg `-0.4171` n `8`; equity avg `-0.1227` n `158`; fx avg `0.0309` n `6`; index avg `-0.011` n `27`; metal avg `-0.0376` n `20`; unknown avg `0.2654` n `1234`
- 24h: commodity avg `0.0741` n `13`; crypto_alt avg `-1.6922` n `239`; crypto_major avg `-0.2317` n `8`; equity avg `0.1886` n `158`; fx avg `0.0667` n `6`; index avg `-0.0039` n `27`; metal avg `-0.0449` n `20`; unknown avg `7.959` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1129`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
