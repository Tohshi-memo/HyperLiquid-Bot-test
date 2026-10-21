# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T02:22:28.628265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0151` n `13`; crypto_alt avg `-0.2371` n `237`; crypto_major avg `-0.2561` n `8`; equity avg `-0.174` n `151`; fx avg `-0.0006` n `6`; index avg `-0.017` n `26`; metal avg `-0.031` n `20`; unknown avg `0.0286` n `1199`
- 1h: commodity avg `0.0493` n `13`; crypto_alt avg `0.1465` n `237`; crypto_major avg `-0.0703` n `8`; equity avg `0.0026` n `151`; fx avg `0.0162` n `6`; index avg `0.0584` n `26`; metal avg `-0.0143` n `20`; unknown avg `0.4424` n `1197`
- 4h: commodity avg `0.1752` n `13`; crypto_alt avg `-0.1283` n `237`; crypto_major avg `-0.3321` n `8`; equity avg `0.0502` n `151`; fx avg `0.0058` n `6`; index avg `0.0295` n `26`; metal avg `-0.1758` n `20`; unknown avg `0.2202` n `1119`
- 24h: commodity avg `0.0965` n `13`; crypto_alt avg `2.8469` n `237`; crypto_major avg `1.9963` n `8`; equity avg `2.0471` n `151`; fx avg `0.0716` n `6`; index avg `0.2738` n `26`; metal avg `-0.0808` n `20`; unknown avg `212.392` n `988`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1673`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1251`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1218`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0995`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0815`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
