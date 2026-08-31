# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T18:07:29.371717+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0444` n `12`; crypto_alt avg `-0.1304` n `232`; crypto_major avg `-0.1035` n `8`; equity avg `0.0244` n `129`; fx avg `0.0081` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0476` n `20`; unknown avg `-0.2425` n `791`
- 1h: commodity avg `-0.0734` n `12`; crypto_alt avg `0.3305` n `232`; crypto_major avg `0.3432` n `8`; equity avg `0.0448` n `129`; fx avg `0.0166` n `6`; index avg `0.002` n `26`; metal avg `-0.0151` n `20`; unknown avg `-0.4219` n `791`
- 4h: commodity avg `0.0728` n `12`; crypto_alt avg `1.0014` n `232`; crypto_major avg `1.3745` n `8`; equity avg `0.2731` n `129`; fx avg `0.0262` n `6`; index avg `-0.036` n `26`; metal avg `-0.0426` n `20`; unknown avg `0.0295` n `789`
- 24h: commodity avg `0.5057` n `12`; crypto_alt avg `-0.9768` n `231`; crypto_major avg `-1.1609` n `8`; equity avg `-0.4126` n `129`; fx avg `-0.0938` n `6`; index avg `-0.2187` n `26`; metal avg `-0.5685` n `20`; unknown avg `0.077` n `758`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1003`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0585`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0498`, n `668`, weak_sample_signal
