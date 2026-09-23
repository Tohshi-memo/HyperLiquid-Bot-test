# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T07:37:36.716927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `12`; crypto_alt avg `-0.404` n `234`; crypto_major avg `-0.2897` n `8`; equity avg `-0.0004` n `140`; fx avg `0.0224` n `6`; index avg `0.0016` n `26`; metal avg `-0.0672` n `20`; unknown avg `0.0072` n `945`
- 1h: commodity avg `0.0872` n `12`; crypto_alt avg `-0.5482` n `234`; crypto_major avg `-0.4457` n `8`; equity avg `-0.1606` n `140`; fx avg `0.0806` n `6`; index avg `-0.0367` n `26`; metal avg `-0.1629` n `20`; unknown avg `0.1727` n `943`
- 4h: commodity avg `0.1062` n `12`; crypto_alt avg `-0.2247` n `234`; crypto_major avg `-0.57` n `8`; equity avg `0.1874` n `140`; fx avg `0.1326` n `6`; index avg `0.026` n `26`; metal avg `-0.2128` n `20`; unknown avg `0.398` n `921`
- 24h: commodity avg `0.0126` n `12`; crypto_alt avg `3.9351` n `234`; crypto_major avg `2.1125` n `8`; equity avg `1.366` n `140`; fx avg `-0.0727` n `6`; index avg `0.1622` n `26`; metal avg `0.0968` n `20`; unknown avg `1.923` n `840`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1351`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1346`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1225`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1136`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0967`, n `668`, weak_sample_signal
