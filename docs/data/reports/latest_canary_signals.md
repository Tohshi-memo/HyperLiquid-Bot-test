# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-17T08:22:30.092049+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0299` n `13`; crypto_alt avg `-0.0457` n `239`; crypto_major avg `-0.0888` n `8`; equity avg `-0.0412` n `162`; fx avg `0.0089` n `6`; index avg `0.0047` n `27`; metal avg `0.0287` n `20`; unknown avg `-0.0257` n `1266`
- 1h: commodity avg `0.1299` n `13`; crypto_alt avg `-0.1247` n `239`; crypto_major avg `-0.1401` n `8`; equity avg `0.0163` n `162`; fx avg `-0.0138` n `6`; index avg `0.0252` n `27`; metal avg `-0.0915` n `20`; unknown avg `0.2858` n `1238`
- 4h: commodity avg `0.2287` n `13`; crypto_alt avg `-0.3255` n `239`; crypto_major avg `-0.4016` n `8`; equity avg `-0.3881` n `162`; fx avg `-0.004` n `6`; index avg `0.003` n `27`; metal avg `-0.0576` n `20`; unknown avg `-0.2649` n `1172`
- 24h: commodity avg `-1.059` n `13`; crypto_alt avg `1.0793` n `239`; crypto_major avg `1.279` n `8`; equity avg `-2.6368` n `162`; fx avg `-0.041` n `6`; index avg `-0.2771` n `27`; metal avg `-0.1003` n `20`; unknown avg `24.095` n `1113`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1178`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1037`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
