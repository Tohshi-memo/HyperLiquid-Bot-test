# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T09:22:28.362841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0645` n `13`; crypto_alt avg `0.1635` n `239`; crypto_major avg `0.2629` n `8`; equity avg `0.024` n `165`; fx avg `0.0251` n `6`; index avg `0.0119` n `27`; metal avg `0.0822` n `20`; unknown avg `0.6592` n `1262`
- 1h: commodity avg `-0.1258` n `13`; crypto_alt avg `-0.1509` n `239`; crypto_major avg `-0.2835` n `8`; equity avg `-0.6476` n `165`; fx avg `-0.0031` n `6`; index avg `-0.0482` n `27`; metal avg `0.0583` n `20`; unknown avg `0.8378` n `1244`
- 4h: commodity avg `-0.3882` n `13`; crypto_alt avg `0.8752` n `239`; crypto_major avg `0.596` n `8`; equity avg `0.048` n `165`; fx avg `-0.0153` n `6`; index avg `0.062` n `27`; metal avg `0.5738` n `20`; unknown avg `0.5399` n `1176`
- 24h: commodity avg `-0.4444` n `13`; crypto_alt avg `-3.2872` n `239`; crypto_major avg `-2.8633` n `8`; equity avg `-7.2726` n `165`; fx avg `-0.1025` n `6`; index avg `-0.6393` n `27`; metal avg `-1.3121` n `20`; unknown avg `14.4978` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1619`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.161`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1406`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1257`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
