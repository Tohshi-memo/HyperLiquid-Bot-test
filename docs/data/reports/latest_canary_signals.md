# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T15:37:33.825077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0099` n `13`; crypto_alt avg `-0.3238` n `239`; crypto_major avg `-0.2831` n `8`; equity avg `-0.1189` n `168`; fx avg `-0.0006` n `6`; index avg `-0.0073` n `27`; metal avg `-0.0136` n `20`; unknown avg `-0.1043` n `1267`
- 1h: commodity avg `-0.0286` n `13`; crypto_alt avg `-0.4729` n `239`; crypto_major avg `-0.1651` n `8`; equity avg `-0.0715` n `168`; fx avg `0.0079` n `6`; index avg `-0.0042` n `27`; metal avg `-0.0294` n `20`; unknown avg `0.4529` n `1259`
- 4h: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.8364` n `239`; crypto_major avg `-0.1663` n `8`; equity avg `-0.2238` n `168`; fx avg `-0.0002` n `6`; index avg `-0.0092` n `27`; metal avg `-0.0462` n `20`; unknown avg `8.2322` n `1241`
- 24h: commodity avg `-0.3395` n `13`; crypto_alt avg `-2.8097` n `239`; crypto_major avg `-1.6673` n `8`; equity avg `0.4586` n `168`; fx avg `-0.0478` n `6`; index avg `0.0577` n `27`; metal avg `0.2171` n `20`; unknown avg `233.5643` n `1092`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1574`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1254`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
