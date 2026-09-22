# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T08:37:27.390908+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0624` n `12`; crypto_alt avg `0.3211` n `234`; crypto_major avg `0.2677` n `8`; equity avg `0.0083` n `140`; fx avg `-0.0583` n `6`; index avg `-0.0007` n `26`; metal avg `0.0413` n `20`; unknown avg `0.0141` n `944`
- 1h: commodity avg `-0.035` n `12`; crypto_alt avg `0.6293` n `234`; crypto_major avg `0.5273` n `8`; equity avg `-0.3297` n `140`; fx avg `-0.0845` n `6`; index avg `-0.0586` n `26`; metal avg `-0.0342` n `20`; unknown avg `0.5435` n `936`
- 4h: commodity avg `-0.0781` n `12`; crypto_alt avg `0.5376` n `234`; crypto_major avg `0.1934` n `8`; equity avg `-0.8102` n `140`; fx avg `-0.0443` n `6`; index avg `-0.1409` n `26`; metal avg `-0.2484` n `20`; unknown avg `8.9021` n `908`
- 24h: commodity avg `-0.2087` n `12`; crypto_alt avg `2.2121` n `234`; crypto_major avg `2.7252` n `8`; equity avg `0.4039` n `140`; fx avg `-0.2038` n `6`; index avg `0.1608` n `26`; metal avg `-0.3119` n `20`; unknown avg `1125.4627` n `792`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1398`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1288`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0901`, n `668`, weak_sample_signal
