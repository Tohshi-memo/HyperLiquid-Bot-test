# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T07:07:23.546207+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0782` n `12`; crypto_alt avg `0.0343` n `232`; crypto_major avg `-0.0212` n `8`; equity avg `-0.0681` n `128`; fx avg `-0.01` n `6`; index avg `-0.013` n `26`; metal avg `-0.0278` n `20`; unknown avg `0.0126` n `791`
- 1h: commodity avg `-0.2035` n `12`; crypto_alt avg `0.2216` n `232`; crypto_major avg `0.1722` n `8`; equity avg `0.2912` n `128`; fx avg `-0.0335` n `6`; index avg `0.0596` n `26`; metal avg `0.1076` n `20`; unknown avg `0.1774` n `789`
- 4h: commodity avg `-0.0516` n `12`; crypto_alt avg `1.0227` n `231`; crypto_major avg `0.8359` n `8`; equity avg `1.0982` n `128`; fx avg `-0.0592` n `6`; index avg `0.185` n `26`; metal avg `0.1645` n `20`; unknown avg `0.3353` n `773`
- 24h: commodity avg `0.2951` n `12`; crypto_alt avg `-0.0381` n `231`; crypto_major avg `-1.5428` n `8`; equity avg `-0.2093` n `128`; fx avg `-0.1112` n `6`; index avg `-0.0508` n `26`; metal avg `-0.2287` n `20`; unknown avg `-0.4369` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.124`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0609`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
