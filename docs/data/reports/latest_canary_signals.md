# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T21:37:26.429074+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0165` n `12`; crypto_alt avg `0.1689` n `232`; crypto_major avg `0.0514` n `8`; equity avg `0.0018` n `134`; fx avg `-0.0007` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0059` n `20`; unknown avg `-0.0012` n `794`
- 1h: commodity avg `0.0146` n `12`; crypto_alt avg `0.43` n `232`; crypto_major avg `0.2531` n `8`; equity avg `0.0225` n `134`; fx avg `-0.0031` n `6`; index avg `-0.0133` n `26`; metal avg `-0.004` n `20`; unknown avg `-0.1905` n `788`
- 4h: commodity avg `0.0694` n `12`; crypto_alt avg `0.5965` n `232`; crypto_major avg `0.1788` n `8`; equity avg `-0.0032` n `134`; fx avg `-0.0239` n `6`; index avg `0.0107` n `26`; metal avg `-0.0042` n `20`; unknown avg `2.0698` n `770`
- 24h: commodity avg `0.1195` n `12`; crypto_alt avg `3.2495` n `232`; crypto_major avg `2.614` n `8`; equity avg `0.2102` n `134`; fx avg `-0.0289` n `6`; index avg `0.0663` n `26`; metal avg `0.0682` n `20`; unknown avg `1281.0004` n `700`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1662`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0867`, n `668`, weak_sample_signal
