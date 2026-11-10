# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T03:29:22.839561+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0228` n `13`; crypto_alt avg `-0.1093` n `239`; crypto_major avg `-0.2581` n `8`; equity avg `-0.2181` n `160`; fx avg `-0.0116` n `6`; index avg `-0.0121` n `27`; metal avg `0.0284` n `20`; unknown avg `0.8139` n `1253`
- 1h: commodity avg `-0.0897` n `13`; crypto_alt avg `0.0444` n `239`; crypto_major avg `-0.2238` n `8`; equity avg `-0.355` n `160`; fx avg `-0.0108` n `6`; index avg `-0.0525` n `27`; metal avg `-0.0277` n `20`; unknown avg `0.0897` n `1249`
- 4h: commodity avg `-0.1184` n `13`; crypto_alt avg `-0.3024` n `239`; crypto_major avg `-0.6533` n `8`; equity avg `-0.4579` n `160`; fx avg `0.0322` n `6`; index avg `-0.1332` n `27`; metal avg `-0.1126` n `20`; unknown avg `0.1115` n `1243`
- 24h: commodity avg `-0.7623` n `13`; crypto_alt avg `0.5556` n `239`; crypto_major avg `-0.5869` n `8`; equity avg `3.2987` n `160`; fx avg `0.022` n `6`; index avg `0.3403` n `27`; metal avg `0.1018` n `20`; unknown avg `184.4227` n `1064`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1418`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1289`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1071`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
