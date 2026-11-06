# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T21:07:37.027357+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `13`; crypto_alt avg `0.1284` n `239`; crypto_major avg `0.0288` n `8`; equity avg `0.2642` n `158`; fx avg `0.0134` n `6`; index avg `0.0395` n `27`; metal avg `0.0171` n `20`; unknown avg `1.0517` n `1219`
- 1h: commodity avg `-0.1402` n `13`; crypto_alt avg `-0.2392` n `239`; crypto_major avg `-0.3033` n `8`; equity avg `-0.0339` n `158`; fx avg `0.0101` n `6`; index avg `-0.0235` n `27`; metal avg `0.0013` n `20`; unknown avg `107.808` n `1219`
- 4h: commodity avg `0.2077` n `13`; crypto_alt avg `-0.4749` n `239`; crypto_major avg `-0.5046` n `8`; equity avg `0.2173` n `158`; fx avg `0.0132` n `6`; index avg `-0.0368` n `27`; metal avg `0.0361` n `20`; unknown avg `18.9358` n `1211`
- 24h: commodity avg `0.1141` n `13`; crypto_alt avg `1.4127` n `239`; crypto_major avg `-0.3618` n `8`; equity avg `2.9471` n `158`; fx avg `-0.0764` n `6`; index avg `0.388` n `27`; metal avg `0.0143` n `20`; unknown avg `55.0955` n `1062`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2141`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1113`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1112`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
