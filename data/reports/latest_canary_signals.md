# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T19:37:28.480011+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0158` n `13`; crypto_alt avg `-0.1174` n `239`; crypto_major avg `0.028` n `8`; equity avg `-0.0494` n `158`; fx avg `0.0035` n `6`; index avg `0.0092` n `27`; metal avg `-0.0389` n `20`; unknown avg `-0.1564` n `1261`
- 1h: commodity avg `0.1747` n `13`; crypto_alt avg `-0.3169` n `239`; crypto_major avg `-0.1687` n `8`; equity avg `0.0622` n `158`; fx avg `0.0128` n `6`; index avg `0.0044` n `27`; metal avg `-0.0426` n `20`; unknown avg `1.177` n `1255`
- 4h: commodity avg `0.4125` n `13`; crypto_alt avg `-0.1653` n `239`; crypto_major avg `0.2838` n `8`; equity avg `0.7835` n `158`; fx avg `0.0024` n `6`; index avg `0.0444` n `27`; metal avg `0.0586` n `20`; unknown avg `38.4893` n `1245`
- 24h: commodity avg `0.1695` n `13`; crypto_alt avg `0.8957` n `239`; crypto_major avg `-0.4601` n `8`; equity avg `1.6002` n `158`; fx avg `-0.0835` n `6`; index avg `0.1803` n `27`; metal avg `-0.1883` n `20`; unknown avg `41.7628` n `1080`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2098`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1335`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.107`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
