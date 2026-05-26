# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-26T03:37:18.062396+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `0.1744` n `228`; crypto_major avg `0.1957` n `8`; equity avg `0.0391` n `67`; fx avg `0.0157` n `6`; index avg `0.0143` n `23`; metal avg `0.0006` n `18`; unknown avg `0.5596` n `407`
- 1h: commodity avg `-0.0028` n `12`; crypto_alt avg `0.0162` n `228`; crypto_major avg `0.0373` n `8`; equity avg `0.0739` n `67`; fx avg `-0.0192` n `6`; index avg `-0.0069` n `23`; metal avg `0.0992` n `18`; unknown avg `-0.3317` n `407`
- 4h: commodity avg `0.2465` n `12`; crypto_alt avg `-1.4313` n `228`; crypto_major avg `-1.0244` n `8`; equity avg `-0.5974` n `67`; fx avg `-0.0606` n `6`; index avg `-0.1688` n `23`; metal avg `-0.3604` n `18`; unknown avg `0.4493` n `405`
- 24h: commodity avg `0.5643` n `12`; crypto_alt avg `-0.1546` n `228`; crypto_major avg `-0.7035` n `8`; equity avg `-0.3449` n `67`; fx avg `-0.0025` n `6`; index avg `0.2451` n `23`; metal avg `-0.1021` n `18`; unknown avg `0.3027` n `387`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1595`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1463`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1442`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1394`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
