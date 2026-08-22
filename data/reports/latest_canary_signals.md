# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T17:32:52.253487+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `-0.0885` n `230`; crypto_major avg `-0.0807` n `8`; equity avg `-0.0126` n `121`; fx avg `-0.0092` n `6`; index avg `-0.0026` n `25`; metal avg `0.0007` n `20`; unknown avg `-0.0228` n `794`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `0.1381` n `230`; crypto_major avg `0.2557` n `8`; equity avg `-0.0024` n `121`; fx avg `-0.0108` n `6`; index avg `-0.0086` n `25`; metal avg `0.0087` n `20`; unknown avg `0.0402` n `794`
- 4h: commodity avg `0.0178` n `12`; crypto_alt avg `0.3189` n `230`; crypto_major avg `0.2997` n `8`; equity avg `-0.0329` n `121`; fx avg `0.0006` n `6`; index avg `-0.0031` n `25`; metal avg `0.0064` n `20`; unknown avg `0.2431` n `794`
- 24h: commodity avg `-0.1276` n `12`; crypto_alt avg `0.8319` n `230`; crypto_major avg `3.1071` n `8`; equity avg `-0.5476` n `121`; fx avg `0.0408` n `6`; index avg `-0.0614` n `25`; metal avg `-0.1628` n `20`; unknown avg `1.9358` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1361`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
