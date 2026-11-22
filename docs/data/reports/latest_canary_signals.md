# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T12:22:31.943079+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0191` n `13`; crypto_alt avg `-0.1472` n `239`; crypto_major avg `-0.0474` n `8`; equity avg `0.0267` n `166`; fx avg `-0.0043` n `6`; index avg `-0.0018` n `27`; metal avg `0.0058` n `20`; unknown avg `0.1866` n `1257`
- 1h: commodity avg `-0.0112` n `13`; crypto_alt avg `-0.2395` n `239`; crypto_major avg `-0.1063` n `8`; equity avg `0.0486` n `166`; fx avg `0.0046` n `6`; index avg `-0.0052` n `27`; metal avg `0.0196` n `20`; unknown avg `-0.0227` n `1253`
- 4h: commodity avg `0.0058` n `13`; crypto_alt avg `0.7948` n `239`; crypto_major avg `1.2088` n `8`; equity avg `0.9551` n `166`; fx avg `-0.0123` n `6`; index avg `0.0652` n `27`; metal avg `0.1293` n `20`; unknown avg `177.4246` n `1151`
- 24h: commodity avg `0.0144` n `13`; crypto_alt avg `2.5387` n `239`; crypto_major avg `3.0066` n `8`; equity avg `1.8261` n `166`; fx avg `-0.0118` n `6`; index avg `0.2068` n `27`; metal avg `0.1662` n `20`; unknown avg `0.7695` n `1084`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1253`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1155`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
