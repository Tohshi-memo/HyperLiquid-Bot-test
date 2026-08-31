# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T09:22:25.705731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.036` n `12`; crypto_alt avg `0.1337` n `232`; crypto_major avg `0.1235` n `8`; equity avg `0.0783` n `128`; fx avg `-0.0034` n `6`; index avg `0.0096` n `26`; metal avg `-0.0077` n `20`; unknown avg `0.1222` n `793`
- 1h: commodity avg `0.1736` n `12`; crypto_alt avg `0.1908` n `232`; crypto_major avg `0.492` n `8`; equity avg `-0.0277` n `128`; fx avg `0.0095` n `6`; index avg `0.0038` n `26`; metal avg `0.0154` n `20`; unknown avg `0.3309` n `791`
- 4h: commodity avg `0.1021` n `12`; crypto_alt avg `0.2317` n `232`; crypto_major avg `0.545` n `8`; equity avg `0.3004` n `128`; fx avg `-0.0849` n `6`; index avg `0.0599` n `26`; metal avg `0.0725` n `20`; unknown avg `0.5757` n `773`
- 24h: commodity avg `0.5746` n `12`; crypto_alt avg `0.1022` n `231`; crypto_major avg `-0.8882` n `8`; equity avg `-0.2385` n `128`; fx avg `-0.1331` n `6`; index avg `-0.02` n `26`; metal avg `-0.2203` n `20`; unknown avg `-0.2222` n `759`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0661`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
