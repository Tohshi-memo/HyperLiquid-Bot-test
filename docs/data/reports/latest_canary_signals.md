# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T17:37:37.149722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0694` n `13`; crypto_alt avg `0.4088` n `239`; crypto_major avg `0.5584` n `8`; equity avg `0.4545` n `168`; fx avg `0.0068` n `6`; index avg `0.0456` n `27`; metal avg `-0.001` n `20`; unknown avg `163.3872` n `1265`
- 1h: commodity avg `0.2481` n `13`; crypto_alt avg `0.9291` n `239`; crypto_major avg `1.0225` n `8`; equity avg `1.2319` n `168`; fx avg `0.014` n `6`; index avg `0.1651` n `27`; metal avg `0.0324` n `20`; unknown avg `19.6555` n `1263`
- 4h: commodity avg `0.2921` n `13`; crypto_alt avg `-0.236` n `239`; crypto_major avg `-0.4117` n `8`; equity avg `-1.0738` n `168`; fx avg `0.0532` n `6`; index avg `0.0308` n `27`; metal avg `-0.5702` n `20`; unknown avg `160.693` n `1241`
- 24h: commodity avg `0.5243` n `13`; crypto_alt avg `-3.9654` n `239`; crypto_major avg `-3.7902` n `8`; equity avg `-4.2361` n `167`; fx avg `0.2656` n `6`; index avg `-0.2673` n `27`; metal avg `-1.2724` n `20`; unknown avg `-0.6228` n `1133`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
