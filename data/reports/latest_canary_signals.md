# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-06T14:22:26.772587+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0603` n `13`; crypto_alt avg `0.1699` n `239`; crypto_major avg `0.1323` n `8`; equity avg `0.3894` n `158`; fx avg `0.0125` n `6`; index avg `0.0381` n `27`; metal avg `0.0204` n `20`; unknown avg `0.2807` n `1257`
- 1h: commodity avg `-0.1591` n `13`; crypto_alt avg `-0.1537` n `239`; crypto_major avg `-0.2864` n `8`; equity avg `0.1462` n `158`; fx avg `-0.0298` n `6`; index avg `-0.0239` n `27`; metal avg `-0.2534` n `20`; unknown avg `173.5425` n `1253`
- 4h: commodity avg `0.003` n `13`; crypto_alt avg `-0.0414` n `239`; crypto_major avg `-0.238` n `8`; equity avg `0.4435` n `158`; fx avg `0.0425` n `6`; index avg `0.0249` n `27`; metal avg `-0.1299` n `20`; unknown avg `269.6509` n `1176`
- 24h: commodity avg `0.2446` n `13`; crypto_alt avg `-2.2709` n `239`; crypto_major avg `-4.5153` n `8`; equity avg `-3.1835` n `158`; fx avg `-0.0426` n `6`; index avg `-0.5104` n `27`; metal avg `-0.77` n `20`; unknown avg `95.1754` n `1076`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2231`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1424`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1099`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1028`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
