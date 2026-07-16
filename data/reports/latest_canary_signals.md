# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-16T13:07:32.626653+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0651` n `12`; crypto_alt avg `0.0987` n `230`; crypto_major avg `0.0623` n `8`; equity avg `0.1593` n `94`; fx avg `0.0079` n `6`; index avg `0.05` n `25`; metal avg `-0.0242` n `20`; unknown avg `-0.0332` n `768`
- 1h: commodity avg `0.0698` n `12`; crypto_alt avg `0.0055` n `230`; crypto_major avg `-0.2767` n `8`; equity avg `0.045` n `94`; fx avg `0.0073` n `6`; index avg `-0.0125` n `25`; metal avg `-0.3551` n `20`; unknown avg `-0.1273` n `768`
- 4h: commodity avg `0.395` n `12`; crypto_alt avg `0.0842` n `230`; crypto_major avg `-0.2566` n `8`; equity avg `-0.6952` n `94`; fx avg `0.0023` n `6`; index avg `-0.1831` n `25`; metal avg `-0.4334` n `20`; unknown avg `0.0134` n `768`
- 24h: commodity avg `0.2833` n `12`; crypto_alt avg `-1.9064` n `230`; crypto_major avg `-2.4917` n `8`; equity avg `-3.4813` n `93`; fx avg `0.0456` n `6`; index avg `-0.6296` n `25`; metal avg `-0.6922` n `20`; unknown avg `-0.1546` n `746`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0979`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0718`, n `668`, weak_sample_signal
