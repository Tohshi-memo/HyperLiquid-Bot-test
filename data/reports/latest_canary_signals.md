# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T06:07:30.580866+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0242` n `13`; crypto_alt avg `-0.0957` n `239`; crypto_major avg `0.0003` n `8`; equity avg `-0.0753` n `158`; fx avg `0.0177` n `6`; index avg `0.0029` n `27`; metal avg `-0.0055` n `20`; unknown avg `-0.1049` n `1231`
- 1h: commodity avg `-0.0311` n `13`; crypto_alt avg `0.0158` n `239`; crypto_major avg `0.2126` n `8`; equity avg `-0.1181` n `158`; fx avg `-0.005` n `6`; index avg `-0.0029` n `27`; metal avg `-0.0018` n `20`; unknown avg `-0.0282` n `1229`
- 4h: commodity avg `-0.0874` n `13`; crypto_alt avg `-0.3924` n `239`; crypto_major avg `-0.3025` n `8`; equity avg `-0.2002` n `158`; fx avg `-0.0077` n `6`; index avg `0.0025` n `27`; metal avg `-0.0058` n `20`; unknown avg `0.0249` n `1207`
- 24h: commodity avg `-0.3151` n `13`; crypto_alt avg `0.7974` n `239`; crypto_major avg `0.5659` n `8`; equity avg `1.4966` n `158`; fx avg `-0.0649` n `6`; index avg `0.2118` n `27`; metal avg `0.2578` n `20`; unknown avg `8.4539` n `1008`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2129`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.162`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
