# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T03:22:34.414159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0401` n `13`; crypto_alt avg `0.2612` n `239`; crypto_major avg `0.2368` n `8`; equity avg `0.0531` n `162`; fx avg `0.0064` n `6`; index avg `-0.0019` n `27`; metal avg `0.0187` n `20`; unknown avg `-0.1792` n `1264`
- 1h: commodity avg `-0.0134` n `13`; crypto_alt avg `0.5592` n `239`; crypto_major avg `0.4183` n `8`; equity avg `0.6546` n `162`; fx avg `0.0017` n `6`; index avg `0.0646` n `27`; metal avg `0.1437` n `20`; unknown avg `0.2899` n `1264`
- 4h: commodity avg `-0.1768` n `13`; crypto_alt avg `0.3703` n `239`; crypto_major avg `-0.0993` n `8`; equity avg `0.8344` n `162`; fx avg `0.0586` n `6`; index avg `0.0714` n `27`; metal avg `0.2974` n `20`; unknown avg `2.403` n `1258`
- 24h: commodity avg `-0.9934` n `13`; crypto_alt avg `-0.0701` n `239`; crypto_major avg `0.3102` n `8`; equity avg `-2.6652` n `162`; fx avg `-0.0403` n `6`; index avg `-0.2555` n `27`; metal avg `-0.0185` n `20`; unknown avg `563.4723` n `999`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1139`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1087`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
