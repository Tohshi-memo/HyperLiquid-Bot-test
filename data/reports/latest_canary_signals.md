# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T14:07:23.993407+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.48` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.006` n `13`; crypto_alt avg `0.012` n `239`; crypto_major avg `0.0911` n `8`; equity avg `-0.0411` n `168`; fx avg `-0.008` n `6`; index avg `-0.003` n `27`; metal avg `0.0113` n `20`; unknown avg `4.0934` n `1253`
- 1h: commodity avg `0.015` n `13`; crypto_alt avg `-0.4083` n `239`; crypto_major avg `-0.3391` n `8`; equity avg `-0.2013` n `168`; fx avg `0.0021` n `6`; index avg `-0.0139` n `27`; metal avg `-0.0311` n `20`; unknown avg `1.5323` n `1255`
- 4h: commodity avg `0.0053` n `13`; crypto_alt avg `-0.7451` n `239`; crypto_major avg `-0.639` n `8`; equity avg `-0.3996` n `168`; fx avg `-0.0098` n `6`; index avg `-0.0334` n `27`; metal avg `-0.0319` n `20`; unknown avg `1.9472` n `1245`
- 24h: commodity avg `-0.2749` n `13`; crypto_alt avg `-4.1032` n `239`; crypto_major avg `-3.5609` n `8`; equity avg `-0.2` n `168`; fx avg `-0.0876` n `6`; index avg `0.0302` n `27`; metal avg `0.1656` n `20`; unknown avg `192.7011` n `1088`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.156`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1491`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1455`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
