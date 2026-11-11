# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-11T17:52:33.042434+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0879` n `13`; crypto_alt avg `-0.0588` n `239`; crypto_major avg `0.019` n `8`; equity avg `-0.0577` n `161`; fx avg `0.0018` n `6`; index avg `-0.0156` n `27`; metal avg `-0.0519` n `20`; unknown avg `0.1659` n `1262`
- 1h: commodity avg `-0.2671` n `13`; crypto_alt avg `0.0342` n `239`; crypto_major avg `0.3645` n `8`; equity avg `0.2277` n `161`; fx avg `-0.0196` n `6`; index avg `0.0205` n `27`; metal avg `-0.0448` n `20`; unknown avg `0.4507` n `1256`
- 4h: commodity avg `-0.0493` n `13`; crypto_alt avg `0.4177` n `239`; crypto_major avg `1.0611` n `8`; equity avg `1.9454` n `161`; fx avg `-0.0214` n `6`; index avg `0.1728` n `27`; metal avg `-0.3931` n `20`; unknown avg `-0.417` n `1225`
- 24h: commodity avg `0.3745` n `13`; crypto_alt avg `1.7094` n `239`; crypto_major avg `2.439` n `8`; equity avg `7.0075` n `161`; fx avg `-0.1476` n `6`; index avg `0.6552` n `27`; metal avg `0.1849` n `20`; unknown avg `4.9067` n `1153`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1435`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1399`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1234`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1071`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0984`, n `668`, weak_sample_signal
