# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T07:50:12.723984+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0285` n `13`; crypto_alt avg `0.2059` n `239`; crypto_major avg `0.4054` n `8`; equity avg `0.3332` n `165`; fx avg `0.0117` n `6`; index avg `0.0503` n `27`; metal avg `0.1907` n `20`; unknown avg `0.9052` n `1262`
- 1h: commodity avg `-0.0823` n `13`; crypto_alt avg `0.0124` n `239`; crypto_major avg `-0.0977` n `8`; equity avg `0.0823` n `165`; fx avg `-0.0166` n `6`; index avg `0.0393` n `27`; metal avg `0.0337` n `20`; unknown avg `0.3819` n `1258`
- 4h: commodity avg `-0.2534` n `13`; crypto_alt avg `0.061` n `239`; crypto_major avg `-0.2203` n `8`; equity avg `-0.8663` n `165`; fx avg `-0.0189` n `6`; index avg `-0.0291` n `27`; metal avg `0.139` n `20`; unknown avg `-0.3214` n `1226`
- 24h: commodity avg `-0.2062` n `13`; crypto_alt avg `-3.0075` n `239`; crypto_major avg `-2.4792` n `8`; equity avg `-6.8664` n `165`; fx avg `-0.0282` n `6`; index avg `-0.6239` n `27`; metal avg `-1.4277` n `20`; unknown avg `61.9025` n `1179`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1615`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1609`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1388`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1266`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0768`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0765`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0593`, n `668`, weak_sample_signal
