# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-22T19:52:26.523075+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0024` n `13`; crypto_alt avg `0.0292` n `239`; crypto_major avg `0.0345` n `8`; equity avg `0.0321` n `166`; fx avg `0.0167` n `6`; index avg `0.0037` n `27`; metal avg `0.0048` n `20`; unknown avg `0.0688` n `1264`
- 1h: commodity avg `-0.016` n `13`; crypto_alt avg `-0.0403` n `239`; crypto_major avg `-0.1567` n `8`; equity avg `-0.0465` n `166`; fx avg `0.011` n `6`; index avg `-0.0262` n `27`; metal avg `-0.0165` n `20`; unknown avg `1.2762` n `1252`
- 4h: commodity avg `-0.0008` n `13`; crypto_alt avg `-0.3053` n `239`; crypto_major avg `-0.1851` n `8`; equity avg `0.1359` n `166`; fx avg `0.0172` n `6`; index avg `0.0084` n `27`; metal avg `-0.0399` n `20`; unknown avg `163.4191` n `1223`
- 24h: commodity avg `-0.1124` n `13`; crypto_alt avg `0.5825` n `239`; crypto_major avg `0.3649` n `8`; equity avg `0.9261` n `166`; fx avg `0.0011` n `6`; index avg `0.1169` n `27`; metal avg `-0.057` n `20`; unknown avg `189.201` n `1052`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1423`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
