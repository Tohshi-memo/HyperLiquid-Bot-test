# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T15:22:23.758785+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.38` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0013` n `13`; crypto_alt avg `0.1405` n `239`; crypto_major avg `0.1353` n `8`; equity avg `0.047` n `168`; fx avg `0.0001` n `6`; index avg `0.0001` n `27`; metal avg `-0.0136` n `20`; unknown avg `0.3915` n `1265`
- 1h: commodity avg `-0.0201` n `13`; crypto_alt avg `-0.0702` n `239`; crypto_major avg `0.1744` n `8`; equity avg `0.1152` n `168`; fx avg `0.0061` n `6`; index avg `0.0112` n `27`; metal avg `-0.0162` n `20`; unknown avg `0.2855` n `1255`
- 4h: commodity avg `0.004` n `13`; crypto_alt avg `-0.4524` n `239`; crypto_major avg `0.241` n `8`; equity avg `-0.0545` n `168`; fx avg `0.0021` n `6`; index avg `-0.0013` n `27`; metal avg `-0.033` n `20`; unknown avg `11.9608` n `1247`
- 24h: commodity avg `-0.3051` n `13`; crypto_alt avg `-1.8154` n `239`; crypto_major avg `-0.5772` n `8`; equity avg `1.3123` n `168`; fx avg `-0.0433` n `6`; index avg `0.1363` n `27`; metal avg `0.2747` n `20`; unknown avg `191.5489` n `1092`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1571`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1497`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1356`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.126`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1217`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `668`, weak_sample_signal
