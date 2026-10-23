# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-23T13:22:33.740525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0148` n `13`; crypto_alt avg `-0.0056` n `237`; crypto_major avg `0.1461` n `8`; equity avg `-0.0277` n `152`; fx avg `-0.0072` n `6`; index avg `-0.0062` n `26`; metal avg `0.0176` n `20`; unknown avg `39.2293` n `1233`
- 1h: commodity avg `-0.1907` n `13`; crypto_alt avg `-0.1319` n `237`; crypto_major avg `0.032` n `8`; equity avg `-0.2151` n `152`; fx avg `-0.001` n `6`; index avg `-0.0364` n `26`; metal avg `0.0626` n `20`; unknown avg `6.2968` n `1231`
- 4h: commodity avg `-0.1359` n `13`; crypto_alt avg `-0.2577` n `237`; crypto_major avg `-0.1739` n `8`; equity avg `-0.9471` n `152`; fx avg `-0.0115` n `6`; index avg `-0.1229` n `26`; metal avg `-0.018` n `20`; unknown avg `3.7051` n `1225`
- 24h: commodity avg `0.0098` n `13`; crypto_alt avg `0.2512` n `237`; crypto_major avg `0.337` n `8`; equity avg `-1.62` n `152`; fx avg `-0.1115` n `6`; index avg `-0.2472` n `26`; metal avg `-0.3673` n `20`; unknown avg `49.8612` n `950`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.2178`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1778`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1666`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1508`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1404`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1349`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1301`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1175`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
