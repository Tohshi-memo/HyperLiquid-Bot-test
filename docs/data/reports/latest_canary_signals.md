# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T07:37:27.696700+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0641` n `12`; crypto_alt avg `-0.1681` n `234`; crypto_major avg `-0.1332` n `8`; equity avg `-0.0681` n `140`; fx avg `-0.0001` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0891` n `20`; unknown avg `-0.0939` n `944`
- 1h: commodity avg `-0.1385` n `12`; crypto_alt avg `-0.3536` n `234`; crypto_major avg `-0.4782` n `8`; equity avg `-0.0792` n `140`; fx avg `0.0122` n `6`; index avg `-0.0235` n `26`; metal avg `-0.0548` n `20`; unknown avg `0.2177` n `942`
- 4h: commodity avg `-0.047` n `12`; crypto_alt avg `-0.2848` n `234`; crypto_major avg `-0.221` n `8`; equity avg `-1.0901` n `140`; fx avg `0.0384` n `6`; index avg `-0.142` n `26`; metal avg `-0.2414` n `20`; unknown avg `8.4185` n `908`
- 24h: commodity avg `-0.1663` n `12`; crypto_alt avg `2.5792` n `234`; crypto_major avg `3.6289` n `8`; equity avg `1.1619` n `140`; fx avg `-0.1789` n `6`; index avg `0.278` n `26`; metal avg `-0.2225` n `20`; unknown avg `1126.0119` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1046`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0896`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
