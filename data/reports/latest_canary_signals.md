# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T21:37:24.189864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0077` n `12`; crypto_alt avg `0.0856` n `231`; crypto_major avg `0.1127` n `8`; equity avg `0.191` n `124`; fx avg `0.0133` n `6`; index avg `0.0813` n `25`; metal avg `0.024` n `20`; unknown avg `0.0282` n `795`
- 1h: commodity avg `0.0631` n `12`; crypto_alt avg `1.2314` n `231`; crypto_major avg `1.1381` n `8`; equity avg `1.1063` n `124`; fx avg `0.0052` n `6`; index avg `0.2353` n `25`; metal avg `0.0692` n `20`; unknown avg `0.5984` n `795`
- 4h: commodity avg `-0.1577` n `12`; crypto_alt avg `0.8697` n `231`; crypto_major avg `0.6178` n `8`; equity avg `1.533` n `124`; fx avg `-0.0103` n `6`; index avg `0.2624` n `25`; metal avg `0.0291` n `20`; unknown avg `0.2994` n `795`
- 24h: commodity avg `0.3437` n `12`; crypto_alt avg `0.7671` n `231`; crypto_major avg `0.5622` n `8`; equity avg `1.3262` n `124`; fx avg `-0.0514` n `6`; index avg `0.2544` n `25`; metal avg `-0.3241` n `20`; unknown avg `1.0004` n `777`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1278`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
