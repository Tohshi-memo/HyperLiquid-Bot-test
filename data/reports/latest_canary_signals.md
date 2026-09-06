# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T02:22:24.657611+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0023` n `12`; crypto_alt avg `-0.3286` n `232`; crypto_major avg `-0.119` n `8`; equity avg `0.0199` n `134`; fx avg `0.0075` n `6`; index avg `0.0104` n `26`; metal avg `-0.0098` n `20`; unknown avg `2.3057` n `792`
- 1h: commodity avg `0.0134` n `12`; crypto_alt avg `-0.0608` n `232`; crypto_major avg `-0.0301` n `8`; equity avg `-0.0053` n `134`; fx avg `-0.0213` n `6`; index avg `0.0026` n `26`; metal avg `-0.0078` n `20`; unknown avg `2.4952` n `790`
- 4h: commodity avg `0.0035` n `12`; crypto_alt avg `0.5235` n `232`; crypto_major avg `0.0258` n `8`; equity avg `0.1037` n `134`; fx avg `-0.0012` n `6`; index avg `-0.0106` n `26`; metal avg `-0.021` n `20`; unknown avg `2.4247` n `784`
- 24h: commodity avg `0.1582` n `12`; crypto_alt avg `3.1025` n `232`; crypto_major avg `2.5017` n `8`; equity avg `0.4026` n `134`; fx avg `-0.0548` n `6`; index avg `0.0689` n `26`; metal avg `0.0258` n `20`; unknown avg `0.7214` n `692`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1541`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0847`, n `668`, weak_sample_signal
