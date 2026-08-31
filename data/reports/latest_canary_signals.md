# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T19:07:26.846345+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.032` n `12`; crypto_alt avg `0.0887` n `232`; crypto_major avg `0.1555` n `8`; equity avg `0.0226` n `129`; fx avg `-0.0063` n `6`; index avg `-0.0032` n `26`; metal avg `-0.0062` n `20`; unknown avg `0.011` n `791`
- 1h: commodity avg `0.034` n `12`; crypto_alt avg `0.314` n `232`; crypto_major avg `0.3679` n `8`; equity avg `-0.1217` n `129`; fx avg `0.0003` n `6`; index avg `-0.0426` n `26`; metal avg `-0.0042` n `20`; unknown avg `0.6062` n `791`
- 4h: commodity avg `0.0612` n `12`; crypto_alt avg `0.817` n `232`; crypto_major avg `1.0782` n `8`; equity avg `0.1238` n `129`; fx avg `-0.0037` n `6`; index avg `-0.0627` n `26`; metal avg `-0.0249` n `20`; unknown avg `-0.2893` n `791`
- 24h: commodity avg `0.5277` n `12`; crypto_alt avg `-0.964` n `231`; crypto_major avg `-1.0354` n `8`; equity avg `-0.5401` n `129`; fx avg `-0.0907` n `6`; index avg `-0.2571` n `26`; metal avg `-0.5794` n `20`; unknown avg `0.3929` n `758`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0693`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0565`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0548`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.051`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
