# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T17:37:25.141292+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.062` n `230`; crypto_major avg `-0.0473` n `8`; equity avg `-0.0058` n `121`; fx avg `-0.0097` n `6`; index avg `-0.0022` n `25`; metal avg `0.0024` n `20`; unknown avg `0.0078` n `794`
- 1h: commodity avg `0.0031` n `12`; crypto_alt avg `0.1643` n `230`; crypto_major avg `0.2893` n `8`; equity avg `0.0044` n `121`; fx avg `-0.0113` n `6`; index avg `-0.0081` n `25`; metal avg `0.0103` n `20`; unknown avg `0.0777` n `794`
- 4h: commodity avg `0.0135` n `12`; crypto_alt avg `0.3444` n `230`; crypto_major avg `0.3336` n `8`; equity avg `-0.0261` n `121`; fx avg `0.0001` n `6`; index avg `-0.0026` n `25`; metal avg `0.008` n `20`; unknown avg `0.2812` n `794`
- 24h: commodity avg `-0.1319` n `12`; crypto_alt avg `0.8561` n `230`; crypto_major avg `3.1405` n `8`; equity avg `-0.5408` n `121`; fx avg `0.0403` n `6`; index avg `-0.0609` n `25`; metal avg `-0.1612` n `20`; unknown avg `1.9475` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1434`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
