# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T18:22:28.510923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `13`; crypto_alt avg `-0.2375` n `239`; crypto_major avg `-0.0025` n `8`; equity avg `-0.1766` n `166`; fx avg `0.0116` n `6`; index avg `-0.0133` n `27`; metal avg `-0.0058` n `20`; unknown avg `0.0305` n `1254`
- 1h: commodity avg `-0.0241` n `13`; crypto_alt avg `-0.4242` n `239`; crypto_major avg `-0.1034` n `8`; equity avg `0.0565` n `166`; fx avg `0.0058` n `6`; index avg `0.0071` n `27`; metal avg `-0.0088` n `20`; unknown avg `39.7205` n `1251`
- 4h: commodity avg `-0.0443` n `13`; crypto_alt avg `-0.3501` n `239`; crypto_major avg `0.2204` n `8`; equity avg `0.1226` n `166`; fx avg `0.0243` n `6`; index avg `0.011` n `27`; metal avg `0.0633` n `20`; unknown avg `-0.6334` n `1223`
- 24h: commodity avg `-0.0869` n `13`; crypto_alt avg `0.4992` n `239`; crypto_major avg `0.8454` n `8`; equity avg `1.0525` n `166`; fx avg `0.0054` n `6`; index avg `0.2449` n `27`; metal avg `0.0556` n `20`; unknown avg `189.0257` n `1056`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1422`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
