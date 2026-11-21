# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-21T19:22:37.928827+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0016` n `13`; crypto_alt avg `-0.1365` n `239`; crypto_major avg `-0.1364` n `8`; equity avg `-0.0315` n `166`; fx avg `-0.0007` n `6`; index avg `-0.0238` n `27`; metal avg `0.0094` n `20`; unknown avg `0.2632` n `1250`
- 1h: commodity avg `0.0157` n `13`; crypto_alt avg `-0.0765` n `239`; crypto_major avg `0.2166` n `8`; equity avg `0.0559` n `166`; fx avg `0.0077` n `6`; index avg `0.0723` n `27`; metal avg `0.0312` n `20`; unknown avg `41.1443` n `1248`
- 4h: commodity avg `0.0249` n `13`; crypto_alt avg `-0.5543` n `239`; crypto_major avg `0.2453` n `8`; equity avg `0.1338` n `166`; fx avg `0.0041` n `6`; index avg `0.0172` n `27`; metal avg `0.04` n `20`; unknown avg `0.8883` n `1192`
- 24h: commodity avg `0.1939` n `13`; crypto_alt avg `1.2547` n `239`; crypto_major avg `3.1554` n `8`; equity avg `0.8009` n `166`; fx avg `-0.0884` n `6`; index avg `0.0988` n `27`; metal avg `0.2801` n `20`; unknown avg `185.813` n `1088`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.149`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1474`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0909`, n `668`, weak_sample_signal
