# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-03T05:52:28.160198+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0336` n `12`; crypto_alt avg `-0.0566` n `229`; crypto_major avg `-0.1048` n `8`; equity avg `-0.0693` n `88`; fx avg `0.0089` n `6`; index avg `-0.0313` n `25`; metal avg `-0.0432` n `20`; unknown avg `-0.1923` n `765`
- 1h: commodity avg `0.0671` n `12`; crypto_alt avg `0.2174` n `229`; crypto_major avg `0.5989` n `8`; equity avg `-0.1306` n `88`; fx avg `0.0151` n `6`; index avg `-0.0268` n `25`; metal avg `-0.0224` n `20`; unknown avg `-0.2034` n `765`
- 4h: commodity avg `0.1586` n `12`; crypto_alt avg `-0.1491` n `229`; crypto_major avg `0.0962` n `8`; equity avg `0.5348` n `88`; fx avg `0.0485` n `6`; index avg `0.1782` n `25`; metal avg `0.0336` n `20`; unknown avg `-0.61` n `761`
- 24h: commodity avg `0.4345` n `12`; crypto_alt avg `2.098` n `228`; crypto_major avg `3.3454` n `8`; equity avg `-0.3251` n `88`; fx avg `-0.0483` n `6`; index avg `0.0411` n `25`; metal avg `1.2621` n `20`; unknown avg `5.8163` n `737`

## Correlations

- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1269`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0664`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
