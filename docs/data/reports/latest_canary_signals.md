# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-10T20:07:38.084776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0347` n `13`; crypto_alt avg `-0.208` n `239`; crypto_major avg `-0.2643` n `8`; equity avg `-0.2339` n `160`; fx avg `0.0041` n `6`; index avg `-0.0247` n `27`; metal avg `-0.0333` n `20`; unknown avg `20.448` n `1250`
- 1h: commodity avg `0.143` n `13`; crypto_alt avg `-0.178` n `239`; crypto_major avg `-0.081` n `8`; equity avg `-0.1726` n `160`; fx avg `-0.0016` n `6`; index avg `-0.0158` n `27`; metal avg `0.0015` n `20`; unknown avg `39.9552` n `1248`
- 4h: commodity avg `0.4955` n `13`; crypto_alt avg `-0.3021` n `239`; crypto_major avg `0.3635` n `8`; equity avg `-0.8623` n `160`; fx avg `0.023` n `6`; index avg `-0.0914` n `27`; metal avg `-0.0539` n `20`; unknown avg `18.476` n `1248`
- 24h: commodity avg `0.2287` n `13`; crypto_alt avg `-1.9401` n `239`; crypto_major avg `-2.8675` n `8`; equity avg `-2.099` n `160`; fx avg `-0.0619` n `6`; index avg `-0.2318` n `27`; metal avg `-0.6842` n `20`; unknown avg `0.2809` n `1161`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.2536`, n `668`, moderate_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1314`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
