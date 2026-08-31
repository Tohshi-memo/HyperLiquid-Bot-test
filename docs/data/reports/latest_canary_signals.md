# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T20:52:31.032732+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0009` n `12`; crypto_alt avg `0.1427` n `232`; crypto_major avg `0.1482` n `8`; equity avg `0.0038` n `129`; fx avg `-0.0069` n `6`; index avg `0.0093` n `26`; metal avg `-0.0045` n `20`; unknown avg `-0.2152` n `793`
- 1h: commodity avg `0.0336` n `12`; crypto_alt avg `0.1238` n `232`; crypto_major avg `0.0144` n `8`; equity avg `-0.0002` n `129`; fx avg `-0.0125` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0516` n `20`; unknown avg `0.4589` n `779`
- 4h: commodity avg `0.1344` n `12`; crypto_alt avg `0.3844` n `232`; crypto_major avg `0.4027` n `8`; equity avg `0.3527` n `129`; fx avg `-0.0007` n `6`; index avg `0.0527` n `26`; metal avg `0.0413` n `20`; unknown avg `-0.3392` n `779`
- 24h: commodity avg `0.2001` n `12`; crypto_alt avg `-0.4782` n `231`; crypto_major avg `-0.457` n `8`; equity avg `0.0412` n `129`; fx avg `-0.0971` n `6`; index avg `-0.1335` n `26`; metal avg `-0.4371` n `20`; unknown avg `-0.1764` n `746`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1019`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0576`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0565`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0492`, n `668`, weak_sample_signal
