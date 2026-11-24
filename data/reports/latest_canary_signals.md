# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-24T04:07:36.531111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0287` n `13`; crypto_alt avg `0.1957` n `239`; crypto_major avg `0.1396` n `8`; equity avg `0.0914` n `166`; fx avg `0.0124` n `6`; index avg `0.0191` n `27`; metal avg `-0.0449` n `20`; unknown avg `3.2209` n `1244`
- 1h: commodity avg `-0.1292` n `13`; crypto_alt avg `0.9363` n `239`; crypto_major avg `1.0854` n `8`; equity avg `0.5208` n `166`; fx avg `0.0112` n `6`; index avg `0.0654` n `27`; metal avg `-0.1112` n `20`; unknown avg `4.0767` n `1246`
- 4h: commodity avg `-0.1831` n `13`; crypto_alt avg `-0.3201` n `239`; crypto_major avg `-0.458` n `8`; equity avg `-0.2842` n `166`; fx avg `0.0652` n `6`; index avg `0.1157` n `27`; metal avg `-0.3165` n `20`; unknown avg `163.392` n `1246`
- 24h: commodity avg `-1.2947` n `13`; crypto_alt avg `0.3474` n `239`; crypto_major avg `-0.0184` n `8`; equity avg `4.7533` n `166`; fx avg `-0.2701` n `6`; index avg `0.6893` n `27`; metal avg `0.0387` n `20`; unknown avg `519.7455` n `1042`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1282`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
