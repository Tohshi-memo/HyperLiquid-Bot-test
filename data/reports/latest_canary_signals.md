# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T22:22:30.496887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `-0.0442` n `232`; crypto_major avg `-0.1481` n `8`; equity avg `-0.0018` n `134`; fx avg `-0.0002` n `6`; index avg `0.0279` n `26`; metal avg `-0.0014` n `20`; unknown avg `-0.2292` n `794`
- 1h: commodity avg `0.04` n `12`; crypto_alt avg `0.2238` n `232`; crypto_major avg `-0.1359` n `8`; equity avg `0.0227` n `134`; fx avg `-0.0007` n `6`; index avg `0.0221` n `26`; metal avg `0.0019` n `20`; unknown avg `-0.0767` n `792`
- 4h: commodity avg `0.0659` n `12`; crypto_alt avg `0.4857` n `232`; crypto_major avg `-0.5491` n `8`; equity avg `0.0109` n `134`; fx avg `-0.0194` n `6`; index avg `0.0356` n `26`; metal avg `-0.0068` n `20`; unknown avg `-0.4863` n `770`
- 24h: commodity avg `0.1546` n `12`; crypto_alt avg `3.5156` n `232`; crypto_major avg `2.5543` n `8`; equity avg `0.2697` n `134`; fx avg `-0.05` n `6`; index avg `0.0794` n `26`; metal avg `0.058` n `20`; unknown avg `1281.0973` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1356`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1235`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1076`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0955`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
