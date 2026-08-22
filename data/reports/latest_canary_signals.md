# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-22T06:07:34.366616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.543` n `230`; crypto_major avg `-0.4384` n `8`; equity avg `-0.0757` n `121`; fx avg `0.0022` n `6`; index avg `-0.0105` n `25`; metal avg `-0.052` n `20`; unknown avg `-0.272` n `778`
- 1h: commodity avg `0.058` n `12`; crypto_alt avg `0.2142` n `230`; crypto_major avg `0.3127` n `8`; equity avg `0.3279` n `121`; fx avg `0.0075` n `6`; index avg `0.0453` n `25`; metal avg `0.1416` n `20`; unknown avg `0.2697` n `778`
- 4h: commodity avg `0.0819` n `12`; crypto_alt avg `-1.8088` n `230`; crypto_major avg `-0.0252` n `8`; equity avg `-0.4341` n `121`; fx avg `0.0323` n `6`; index avg `-0.0494` n `25`; metal avg `-0.1149` n `20`; unknown avg `0.0113` n `777`
- 24h: commodity avg `0.2143` n `12`; crypto_alt avg `5.6716` n `230`; crypto_major avg `5.8052` n `8`; equity avg `-0.1642` n `121`; fx avg `0.029` n `6`; index avg `-0.0529` n `25`; metal avg `0.0672` n `20`; unknown avg `0.9845` n `777`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.146`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1448`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1419`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1417`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1358`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
