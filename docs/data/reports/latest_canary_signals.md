# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-28T16:37:27.667557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.003` n `13`; crypto_alt avg `0.0152` n `239`; crypto_major avg `-0.0636` n `8`; equity avg `-0.0041` n `168`; fx avg `0.0102` n `6`; index avg `0.0002` n `27`; metal avg `-0.0043` n `20`; unknown avg `7.1868` n `1267`
- 1h: commodity avg `-0.0093` n `13`; crypto_alt avg `-0.3157` n `239`; crypto_major avg `0.0058` n `8`; equity avg `-0.0035` n `168`; fx avg `0.0119` n `6`; index avg `0.003` n `27`; metal avg `0.004` n `20`; unknown avg `3.7797` n `1245`
- 4h: commodity avg `-0.0133` n `13`; crypto_alt avg `-1.1176` n `239`; crypto_major avg `-0.2554` n `8`; equity avg `-0.2227` n `168`; fx avg `0.0073` n `6`; index avg `-0.0099` n `27`; metal avg `-0.0471` n `20`; unknown avg `0.4789` n `1239`
- 24h: commodity avg `-0.0276` n `13`; crypto_alt avg `-3.1637` n `239`; crypto_major avg `-1.9018` n `8`; equity avg `0.1208` n `168`; fx avg `-0.0051` n `6`; index avg `0.032` n `27`; metal avg `0.272` n `20`; unknown avg `539.8724` n `1084`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1591`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1431`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0871`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
