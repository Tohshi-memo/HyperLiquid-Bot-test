# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T17:37:30.644448+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0373` n `13`; crypto_alt avg `0.1544` n `239`; crypto_major avg `-0.029` n `8`; equity avg `-0.0372` n `168`; fx avg `-0.0002` n `6`; index avg `0.011` n `27`; metal avg `-0.0266` n `20`; unknown avg `-0.0885` n `1267`
- 1h: commodity avg `-0.0547` n `13`; crypto_alt avg `0.2979` n `239`; crypto_major avg `0.2731` n `8`; equity avg `0.0063` n `168`; fx avg `-0.0117` n `6`; index avg `0.003` n `27`; metal avg `-0.0326` n `20`; unknown avg `0.9841` n `1261`
- 4h: commodity avg `0.0237` n `13`; crypto_alt avg `-0.1758` n `239`; crypto_major avg `-0.4324` n `8`; equity avg `-0.3384` n `168`; fx avg `-0.017` n `6`; index avg `-0.0387` n `27`; metal avg `-0.0529` n `20`; unknown avg `-0.4771` n `1239`
- 24h: commodity avg `0.0318` n `13`; crypto_alt avg `2.6535` n `239`; crypto_major avg `1.9243` n `8`; equity avg `3.7765` n `168`; fx avg `-0.0086` n `6`; index avg `0.3067` n `27`; metal avg `0.8093` n `20`; unknown avg `13.9606` n `1053`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1033`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0997`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
