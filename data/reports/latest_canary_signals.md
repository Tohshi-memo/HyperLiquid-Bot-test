# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T06:22:24.900416+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0584` n `12`; crypto_alt avg `0.1582` n `232`; crypto_major avg `0.1108` n `8`; equity avg `0.2773` n `128`; fx avg `-0.0435` n `6`; index avg `0.0456` n `26`; metal avg `0.0685` n `20`; unknown avg `0.2599` n `791`
- 1h: commodity avg `-0.0133` n `12`; crypto_alt avg `0.0864` n `232`; crypto_major avg `0.0326` n `8`; equity avg `0.3637` n `128`; fx avg `-0.0701` n `6`; index avg `0.033` n `26`; metal avg `0.0322` n `20`; unknown avg `0.2591` n `773`
- 4h: commodity avg `0.0551` n `12`; crypto_alt avg `0.8957` n `231`; crypto_major avg `0.5066` n `8`; equity avg `1.076` n `128`; fx avg `-0.0778` n `6`; index avg `0.2206` n `26`; metal avg `0.1691` n `20`; unknown avg `0.3956` n `773`
- 24h: commodity avg `0.4548` n `12`; crypto_alt avg `-0.0621` n `231`; crypto_major avg `-1.5366` n `8`; equity avg `-0.19` n `128`; fx avg `-0.1231` n `6`; index avg `-0.0648` n `26`; metal avg `-0.2609` n `20`; unknown avg `-0.3686` n `757`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1245`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1161`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0732`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0556`, n `668`, weak_sample_signal
