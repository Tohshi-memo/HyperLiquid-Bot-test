# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T00:22:27.893731+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0246` n `12`; crypto_alt avg `0.2641` n `232`; crypto_major avg `0.0938` n `8`; equity avg `-0.0103` n `134`; fx avg `-0.0107` n `6`; index avg `-0.0037` n `26`; metal avg `-0.0031` n `20`; unknown avg `5.7083` n `794`
- 1h: commodity avg `-0.0012` n `12`; crypto_alt avg `0.281` n `232`; crypto_major avg `0.1554` n `8`; equity avg `0.0221` n `134`; fx avg `-0.0174` n `6`; index avg `-0.0` n `26`; metal avg `-0.0123` n `20`; unknown avg `-0.4431` n `792`
- 4h: commodity avg `-0.0139` n `12`; crypto_alt avg `0.591` n `232`; crypto_major avg `-0.0494` n `8`; equity avg `0.1014` n `134`; fx avg `-0.0215` n `6`; index avg `0.0144` n `26`; metal avg `-0.0082` n `20`; unknown avg `18.1838` n `788`
- 24h: commodity avg `0.1397` n `12`; crypto_alt avg `3.0689` n `232`; crypto_major avg `2.2832` n `8`; equity avg `0.3121` n `134`; fx avg `-0.0823` n `6`; index avg `0.0662` n `26`; metal avg `0.0538` n `20`; unknown avg `0.1278` n `694`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1639`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
