# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-08T16:22:24.138790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `13`; crypto_alt avg `-0.1704` n `239`; crypto_major avg `-0.0663` n `8`; equity avg `-0.0113` n `158`; fx avg `-0.0076` n `6`; index avg `0.0009` n `27`; metal avg `0.0034` n `20`; unknown avg `-0.1115` n `1262`
- 1h: commodity avg `0.0144` n `13`; crypto_alt avg `-0.1038` n `239`; crypto_major avg `0.0402` n `8`; equity avg `0.0424` n `158`; fx avg `0.0165` n `6`; index avg `0.0026` n `27`; metal avg `0.0092` n `20`; unknown avg `-0.9684` n `1242`
- 4h: commodity avg `0.0218` n `13`; crypto_alt avg `-0.4087` n `239`; crypto_major avg `-0.0971` n `8`; equity avg `-0.1039` n `158`; fx avg `0.0155` n `6`; index avg `-0.0071` n `27`; metal avg `-0.0353` n `20`; unknown avg `0.0633` n `1234`
- 24h: commodity avg `0.0904` n `13`; crypto_alt avg `-1.3674` n `239`; crypto_major avg `-0.0076` n `8`; equity avg `0.2035` n `158`; fx avg `0.0584` n `6`; index avg `-0.0163` n `27`; metal avg `-0.0511` n `20`; unknown avg `7.6106` n `1083`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1607`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
