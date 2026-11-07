# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-07T18:37:25.768545+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `-0.1429` n `239`; crypto_major avg `-0.0897` n `8`; equity avg `-0.0297` n `158`; fx avg `0.0012` n `6`; index avg `-0.0003` n `27`; metal avg `-0.0005` n `20`; unknown avg `0.178` n `1262`
- 1h: commodity avg `-0.035` n `13`; crypto_alt avg `0.0744` n `239`; crypto_major avg `0.0713` n `8`; equity avg `0.1042` n `158`; fx avg `-0.0097` n `6`; index avg `0.0158` n `27`; metal avg `0.0033` n `20`; unknown avg `1.3743` n `1238`
- 4h: commodity avg `0.0164` n `13`; crypto_alt avg `-0.1153` n `239`; crypto_major avg `-0.2026` n `8`; equity avg `0.0588` n `158`; fx avg `-0.0149` n `6`; index avg `0.0313` n `27`; metal avg `-0.0182` n `20`; unknown avg `165.6864` n `1209`
- 24h: commodity avg `0.1366` n `13`; crypto_alt avg `-1.4176` n `239`; crypto_major avg `-0.593` n `8`; equity avg `0.5342` n `158`; fx avg `-0.0015` n `6`; index avg `0.0556` n `27`; metal avg `-0.0042` n `20`; unknown avg `0.1864` n `1077`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1612`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.106`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
