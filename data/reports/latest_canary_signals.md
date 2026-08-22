# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T15:22:25.498267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0161` n `12`; crypto_alt avg `-0.4329` n `230`; crypto_major avg `-0.1972` n `8`; equity avg `-0.0423` n `121`; fx avg `0.0016` n `6`; index avg `0.006` n `25`; metal avg `0.0024` n `20`; unknown avg `-0.062` n `794`
- 1h: commodity avg `0.0115` n `12`; crypto_alt avg `-0.7389` n `230`; crypto_major avg `-0.8685` n `8`; equity avg `-0.0987` n `121`; fx avg `0.0116` n `6`; index avg `0.0041` n `25`; metal avg `-0.001` n `20`; unknown avg `-0.0853` n `794`
- 4h: commodity avg `-0.05` n `12`; crypto_alt avg `-0.4398` n `230`; crypto_major avg `-0.2571` n `8`; equity avg `-0.0122` n `121`; fx avg `-0.027` n `6`; index avg `0.0058` n `25`; metal avg `0.0435` n `20`; unknown avg `0.0655` n `794`
- 24h: commodity avg `-0.1122` n `12`; crypto_alt avg `-0.9408` n `230`; crypto_major avg `1.2193` n `8`; equity avg `-0.5242` n `121`; fx avg `0.0497` n `6`; index avg `-0.0337` n `25`; metal avg `-0.037` n `20`; unknown avg `1.1393` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1562`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1348`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1336`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.12`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1198`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
