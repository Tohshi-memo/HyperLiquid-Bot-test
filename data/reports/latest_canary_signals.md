# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T15:55:12.108527+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0186` n `12`; crypto_alt avg `-0.0957` n `230`; crypto_major avg `-0.161` n `8`; equity avg `0.0115` n `121`; fx avg `0.0111` n `6`; index avg `0.0044` n `25`; metal avg `0.0022` n `20`; unknown avg `-0.0246` n `794`
- 1h: commodity avg `0.0016` n `12`; crypto_alt avg `0.0507` n `230`; crypto_major avg `0.0091` n `8`; equity avg `-0.0411` n `121`; fx avg `0.017` n `6`; index avg `0.008` n `25`; metal avg `0.0115` n `20`; unknown avg `0.1257` n `794`
- 4h: commodity avg `-0.0482` n `12`; crypto_alt avg `-0.6532` n `230`; crypto_major avg `-0.4515` n `8`; equity avg `-0.0626` n `121`; fx avg `-0.0112` n `6`; index avg `0.0032` n `25`; metal avg `0.0163` n `20`; unknown avg `0.1266` n `794`
- 24h: commodity avg `-0.0851` n `12`; crypto_alt avg `-0.2534` n `230`; crypto_major avg `1.8465` n `8`; equity avg `-0.829` n `121`; fx avg `0.0636` n `6`; index avg `-0.1291` n `25`; metal avg `-0.1013` n `20`; unknown avg `1.7403` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1449`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1232`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1157`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
