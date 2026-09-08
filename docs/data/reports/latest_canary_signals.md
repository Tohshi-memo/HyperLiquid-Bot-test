# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-08T06:52:29.049762+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0763` n `12`; crypto_alt avg `0.0071` n `232`; crypto_major avg `-0.014` n `8`; equity avg `0.1421` n `134`; fx avg `-0.0115` n `6`; index avg `0.034` n `26`; metal avg `0.0648` n `20`; unknown avg `-0.2081` n `797`
- 1h: commodity avg `0.0575` n `12`; crypto_alt avg `-0.6058` n `232`; crypto_major avg `-0.4708` n `8`; equity avg `-0.3364` n `134`; fx avg `0.05` n `6`; index avg `-0.0858` n `26`; metal avg `-0.0973` n `20`; unknown avg `0.6988` n `761`
- 4h: commodity avg `0.2937` n `12`; crypto_alt avg `-0.451` n `232`; crypto_major avg `-0.5751` n `8`; equity avg `-0.7231` n `134`; fx avg `0.1339` n `6`; index avg `-0.208` n `26`; metal avg `-0.08` n `20`; unknown avg `0.5195` n `747`
- 24h: commodity avg `0.3097` n `12`; crypto_alt avg `0.0701` n `232`; crypto_major avg `-1.4835` n `8`; equity avg `-0.3524` n `134`; fx avg `-0.1438` n `6`; index avg `-0.1027` n `26`; metal avg `0.1277` n `20`; unknown avg `7508.5875` n `666`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1343`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0982`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
