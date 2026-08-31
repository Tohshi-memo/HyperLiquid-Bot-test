# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T12:22:28.733575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1078` n `12`; crypto_alt avg `-0.0373` n `232`; crypto_major avg `-0.0112` n `8`; equity avg `0.0133` n `128`; fx avg `0.0184` n `6`; index avg `0.0011` n `26`; metal avg `-0.0948` n `20`; unknown avg `0.7612` n `794`
- 1h: commodity avg `-0.1447` n `12`; crypto_alt avg `-0.0851` n `232`; crypto_major avg `-0.1303` n `8`; equity avg `0.0695` n `128`; fx avg `0.0235` n `6`; index avg `0.0037` n `26`; metal avg `-0.0912` n `20`; unknown avg `0.4222` n `792`
- 4h: commodity avg `0.1222` n `12`; crypto_alt avg `0.2547` n `232`; crypto_major avg `0.5946` n `8`; equity avg `-0.1716` n `128`; fx avg `0.0253` n `6`; index avg `-0.0361` n `26`; metal avg `0.0331` n `20`; unknown avg `0.0809` n `791`
- 24h: commodity avg `0.5499` n `12`; crypto_alt avg `-0.632` n `231`; crypto_major avg `-1.1465` n `8`; equity avg `-0.4148` n `128`; fx avg `-0.1171` n `6`; index avg `-0.069` n `26`; metal avg `-0.1905` n `20`; unknown avg `0.0414` n `761`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0647`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0521`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0509`, n `668`, weak_sample_signal
