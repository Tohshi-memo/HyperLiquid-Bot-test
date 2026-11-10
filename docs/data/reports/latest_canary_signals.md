# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T03:52:24.496040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0231` n `13`; crypto_alt avg `-0.0062` n `239`; crypto_major avg `-0.0243` n `8`; equity avg `-0.1695` n `160`; fx avg `-0.0182` n `6`; index avg `-0.0129` n `27`; metal avg `-0.0402` n `20`; unknown avg `-0.0529` n `1257`
- 1h: commodity avg `-0.0657` n `13`; crypto_alt avg `-0.2228` n `239`; crypto_major avg `-0.4905` n `8`; equity avg `-0.662` n `160`; fx avg `-0.0274` n `6`; index avg `-0.0795` n `27`; metal avg `-0.04` n `20`; unknown avg `0.4399` n `1249`
- 4h: commodity avg `-0.2025` n `13`; crypto_alt avg `-0.3328` n `239`; crypto_major avg `-0.8183` n `8`; equity avg `-1.0088` n `160`; fx avg `0.0177` n `6`; index avg `-0.1504` n `27`; metal avg `-0.1424` n `20`; unknown avg `0.3521` n `1241`
- 24h: commodity avg `-0.7967` n `13`; crypto_alt avg `0.2821` n `239`; crypto_major avg `-0.9778` n `8`; equity avg `2.6931` n `160`; fx avg `0.008` n `6`; index avg `0.234` n `27`; metal avg `0.0044` n `20`; unknown avg `187.7377` n `1069`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1365`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
