# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-14T00:52:24.059841+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `-0.0231` n `230`; crypto_major avg `0.0113` n `8`; equity avg `0.0685` n `92`; fx avg `-0.0013` n `6`; index avg `0.0192` n `25`; metal avg `0.0049` n `20`; unknown avg `-0.0681` n `766`
- 1h: commodity avg `0.1058` n `12`; crypto_alt avg `0.336` n `230`; crypto_major avg `0.1629` n `8`; equity avg `0.7705` n `92`; fx avg `-0.0071` n `6`; index avg `0.0816` n `25`; metal avg `0.0069` n `20`; unknown avg `0.0856` n `766`
- 4h: commodity avg `0.3369` n `12`; crypto_alt avg `0.4345` n `230`; crypto_major avg `0.5455` n `8`; equity avg `0.2104` n `92`; fx avg `-0.0021` n `6`; index avg `0.0084` n `25`; metal avg `-0.0031` n `20`; unknown avg `0.1001` n `766`
- 24h: commodity avg `1.0937` n `12`; crypto_alt avg `-1.7246` n `230`; crypto_major avg `-2.3389` n `8`; equity avg `-2.3056` n `92`; fx avg `-0.0951` n `6`; index avg `-0.4701` n `25`; metal avg `-0.328` n `20`; unknown avg `-0.3492` n `750`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1956`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1129`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
