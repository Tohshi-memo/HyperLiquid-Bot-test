# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T08:37:31.408240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0809` n `13`; crypto_alt avg `0.2914` n `239`; crypto_major avg `0.4823` n `8`; equity avg `0.5157` n `168`; fx avg `0.0219` n `6`; index avg `0.0824` n `27`; metal avg `0.1183` n `20`; unknown avg `158.7017` n `1265`
- 1h: commodity avg `0.0301` n `13`; crypto_alt avg `0.8774` n `239`; crypto_major avg `0.8486` n `8`; equity avg `1.1128` n `168`; fx avg `0.0573` n `6`; index avg `0.1399` n `27`; metal avg `0.1715` n `20`; unknown avg `422.8737` n `1241`
- 4h: commodity avg `-0.2335` n `13`; crypto_alt avg `0.4575` n `239`; crypto_major avg `-0.1589` n `8`; equity avg `-0.5885` n `168`; fx avg `-0.0133` n `6`; index avg `-0.021` n `27`; metal avg `-0.0792` n `20`; unknown avg `2.25` n `1207`
- 24h: commodity avg `0.1536` n `13`; crypto_alt avg `-2.4134` n `239`; crypto_major avg `-2.7482` n `8`; equity avg `-4.8894` n `167`; fx avg `0.0983` n `6`; index avg `-0.4157` n `27`; metal avg `-0.8059` n `20`; unknown avg `702.6364` n `1029`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1299`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1287`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
