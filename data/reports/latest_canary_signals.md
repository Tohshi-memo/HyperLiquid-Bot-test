# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T09:37:27.297017+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0034` n `12`; crypto_alt avg `0.0641` n `230`; crypto_major avg `0.0493` n `8`; equity avg `0.0659` n `92`; fx avg `-0.0065` n `6`; index avg `0.0125` n `25`; metal avg `-0.0296` n `20`; unknown avg `-0.0009` n `766`
- 1h: commodity avg `-0.1905` n `12`; crypto_alt avg `0.1584` n `230`; crypto_major avg `0.0525` n `8`; equity avg `0.242` n `92`; fx avg `-0.0356` n `6`; index avg `0.0316` n `25`; metal avg `-0.0073` n `20`; unknown avg `-0.0845` n `766`
- 4h: commodity avg `-0.4519` n `12`; crypto_alt avg `0.394` n `230`; crypto_major avg `0.13` n `8`; equity avg `0.4025` n `92`; fx avg `-0.0576` n `6`; index avg `0.1287` n `25`; metal avg `0.2241` n `20`; unknown avg `0.0064` n `750`
- 24h: commodity avg `-0.3982` n `12`; crypto_alt avg `-1.0015` n `230`; crypto_major avg `-0.9184` n `8`; equity avg `-1.8554` n `92`; fx avg `-0.034` n `6`; index avg `-0.3782` n `25`; metal avg `-0.1634` n `20`; unknown avg `-0.0399` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1773`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1303`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1296`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
