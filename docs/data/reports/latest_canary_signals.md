# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T17:37:31.484229+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0444` n `12`; crypto_alt avg `-0.0658` n `232`; crypto_major avg `-0.0765` n `8`; equity avg `-0.0492` n `129`; fx avg `-0.0051` n `6`; index avg `-0.0137` n `26`; metal avg `-0.0077` n `20`; unknown avg `-0.2427` n `793`
- 1h: commodity avg `-0.0143` n `12`; crypto_alt avg `0.2697` n `232`; crypto_major avg `0.4329` n `8`; equity avg `0.0024` n `129`; fx avg `-0.0059` n `6`; index avg `-0.0213` n `26`; metal avg `-0.0058` n `20`; unknown avg `-0.3264` n `791`
- 4h: commodity avg `-0.0569` n `12`; crypto_alt avg `0.7311` n `232`; crypto_major avg `1.0496` n `8`; equity avg `0.0079` n `129`; fx avg `0.0043` n `6`; index avg `-0.1024` n `26`; metal avg `-0.1299` n `20`; unknown avg `-0.0011` n `789`
- 24h: commodity avg `0.5534` n `12`; crypto_alt avg `-1.2425` n `231`; crypto_major avg `-1.3682` n `8`; equity avg `-0.535` n `129`; fx avg `-0.1111` n `6`; index avg `-0.257` n `26`; metal avg `-0.584` n `20`; unknown avg `0.0409` n `758`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0521`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0506`, n `668`, weak_sample_signal
