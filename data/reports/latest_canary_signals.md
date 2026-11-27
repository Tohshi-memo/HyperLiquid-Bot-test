# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-27T11:07:31.758246+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0003` n `13`; crypto_alt avg `-0.1602` n `239`; crypto_major avg `-0.1975` n `8`; equity avg `-0.224` n `168`; fx avg `0.015` n `6`; index avg `-0.0162` n `27`; metal avg `-0.0137` n `20`; unknown avg `0.2088` n `1247`
- 1h: commodity avg `-0.0554` n `13`; crypto_alt avg `-0.1712` n `239`; crypto_major avg `-0.0651` n `8`; equity avg `0.2405` n `168`; fx avg `0.0103` n `6`; index avg `0.033` n `27`; metal avg `0.0485` n `20`; unknown avg `1.8723` n `1253`
- 4h: commodity avg `-0.342` n `13`; crypto_alt avg `-0.1862` n `239`; crypto_major avg `-0.0934` n `8`; equity avg `0.1008` n `168`; fx avg `-0.0191` n `6`; index avg `-0.0095` n `27`; metal avg `-0.0044` n `20`; unknown avg `1.134` n `1113`
- 24h: commodity avg `0.0608` n `13`; crypto_alt avg `1.8698` n `239`; crypto_major avg `3.1365` n `8`; equity avg `4.2022` n `168`; fx avg `-0.0881` n `6`; index avg `0.3376` n `27`; metal avg `1.3386` n `20`; unknown avg `236.1576` n `1019`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1128`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0915`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
