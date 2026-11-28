# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T15:07:32.886575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.35` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0019` n `13`; crypto_alt avg `-0.2428` n `239`; crypto_major avg `-0.0698` n `8`; equity avg `-0.0158` n `168`; fx avg `0.0` n `6`; index avg `0.0025` n `27`; metal avg `-0.0067` n `20`; unknown avg `0.5273` n `1253`
- 1h: commodity avg `-0.0242` n `13`; crypto_alt avg `-0.0426` n `239`; crypto_major avg `0.3316` n `8`; equity avg `0.1471` n `168`; fx avg `0.0181` n `6`; index avg `0.0148` n `27`; metal avg `0.0148` n `20`; unknown avg `5.1938` n `1253`
- 4h: commodity avg `-0.013` n `13`; crypto_alt avg `-0.6103` n `239`; crypto_major avg `0.0832` n `8`; equity avg `-0.0791` n `168`; fx avg `0.0039` n `6`; index avg `0.0016` n `27`; metal avg `-0.0179` n `20`; unknown avg `12.6567` n `1241`
- 24h: commodity avg `-0.2269` n `13`; crypto_alt avg `-1.5268` n `239`; crypto_major avg `0.0664` n `8`; equity avg `1.9504` n `168`; fx avg `-0.0565` n `6`; index avg `0.1854` n `27`; metal avg `0.2338` n `20`; unknown avg `191.8304` n `1090`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1531`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1374`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1307`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1209`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
