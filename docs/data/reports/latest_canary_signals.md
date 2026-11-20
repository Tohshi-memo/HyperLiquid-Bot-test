# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-20T19:52:27.725541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0725` n `13`; crypto_alt avg `-0.0506` n `239`; crypto_major avg `0.0068` n `8`; equity avg `-0.1686` n `166`; fx avg `-0.0143` n `6`; index avg `-0.0123` n `27`; metal avg `0.0182` n `20`; unknown avg `0.9968` n `1262`
- 1h: commodity avg `0.1531` n `13`; crypto_alt avg `-0.6482` n `239`; crypto_major avg `-0.9156` n `8`; equity avg `-1.1694` n `166`; fx avg `-0.027` n `6`; index avg `-0.1716` n `27`; metal avg `-0.0298` n `20`; unknown avg `3.7623` n `1254`
- 4h: commodity avg `0.4664` n `13`; crypto_alt avg `-0.2125` n `239`; crypto_major avg `-1.3537` n `8`; equity avg `-2.3003` n `166`; fx avg `-0.0264` n `6`; index avg `-0.3546` n `27`; metal avg `-0.2671` n `20`; unknown avg `25.4275` n `1247`
- 24h: commodity avg `0.1787` n `13`; crypto_alt avg `-6.4224` n `239`; crypto_major avg `-7.3485` n `8`; equity avg `-8.5941` n `166`; fx avg `-0.007` n `6`; index avg `-0.8471` n `27`; metal avg `-1.2552` n `20`; unknown avg `45.4742` n `1153`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1689`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1543`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1517`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1034`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0904`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0714`, n `668`, weak_sample_signal
