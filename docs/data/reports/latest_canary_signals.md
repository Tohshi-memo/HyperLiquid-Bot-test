# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-11T02:07:25.525018+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.0013` n `229`; crypto_major avg `-0.0953` n `8`; equity avg `0.0144` n `92`; fx avg `0.0` n `6`; index avg `-0.004` n `25`; metal avg `-0.0011` n `20`; unknown avg `-0.0335` n `765`
- 1h: commodity avg `-0.0823` n `12`; crypto_alt avg `0.0757` n `229`; crypto_major avg `-0.2104` n `8`; equity avg `-0.0758` n `92`; fx avg `0.0015` n `6`; index avg `-0.0147` n `25`; metal avg `-0.0064` n `20`; unknown avg `0.1641` n `765`
- 4h: commodity avg `-0.0317` n `12`; crypto_alt avg `-0.0582` n `229`; crypto_major avg `-0.2972` n `8`; equity avg `-0.0071` n `92`; fx avg `0.0031` n `6`; index avg `-0.0321` n `25`; metal avg `-0.0041` n `20`; unknown avg `3.2278` n `765`
- 24h: commodity avg `-0.3662` n `12`; crypto_alt avg `0.3697` n `229`; crypto_major avg `-0.1723` n `8`; equity avg `-0.7174` n `92`; fx avg `-0.1713` n `6`; index avg `0.0467` n `25`; metal avg `0.0565` n `20`; unknown avg `4.1228` n `732`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1149`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.111`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
