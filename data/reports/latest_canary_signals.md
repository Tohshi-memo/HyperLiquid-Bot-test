# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-23T01:07:20.056749+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0038` n `12`; crypto_alt avg `-0.3956` n `230`; crypto_major avg `-0.4436` n `8`; equity avg `-0.0199` n `121`; fx avg `0.0064` n `6`; index avg `0.0069` n `25`; metal avg `0.0047` n `20`; unknown avg `0.6541` n `794`
- 1h: commodity avg `0.0021` n `12`; crypto_alt avg `0.4181` n `230`; crypto_major avg `0.859` n `8`; equity avg `0.1` n `121`; fx avg `0.0018` n `6`; index avg `0.0131` n `25`; metal avg `0.0192` n `20`; unknown avg `0.5119` n `794`
- 4h: commodity avg `0.0073` n `12`; crypto_alt avg `0.2352` n `230`; crypto_major avg `0.6268` n `8`; equity avg `0.1798` n `121`; fx avg `0.0487` n `6`; index avg `0.027` n `25`; metal avg `0.0182` n `20`; unknown avg `0.7921` n `794`
- 24h: commodity avg `0.1079` n `12`; crypto_alt avg `-2.6133` n `230`; crypto_major avg `0.8831` n `8`; equity avg `-0.2376` n `121`; fx avg `0.119` n `6`; index avg `-0.0449` n `25`; metal avg `-0.049` n `20`; unknown avg `2.9634` n `777`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1481`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
