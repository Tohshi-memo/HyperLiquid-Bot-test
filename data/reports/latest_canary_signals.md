# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T12:07:28.111270+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0217` n `12`; crypto_alt avg `-0.1284` n `232`; crypto_major avg `-0.064` n `8`; equity avg `0.0086` n `134`; fx avg `0.0033` n `6`; index avg `0.0097` n `26`; metal avg `-0.0026` n `20`; unknown avg `-0.155` n `790`
- 1h: commodity avg `-0.0466` n `12`; crypto_alt avg `0.0887` n `232`; crypto_major avg `0.022` n `8`; equity avg `-0.0005` n `134`; fx avg `-0.006` n `6`; index avg `-0.0019` n `26`; metal avg `0.0044` n `20`; unknown avg `0.4898` n `790`
- 4h: commodity avg `-0.038` n `12`; crypto_alt avg `0.7146` n `232`; crypto_major avg `0.301` n `8`; equity avg `0.177` n `134`; fx avg `-0.0092` n `6`; index avg `0.0204` n `26`; metal avg `0.0062` n `20`; unknown avg `-0.1065` n `784`
- 24h: commodity avg `0.0898` n `12`; crypto_alt avg `2.2577` n `232`; crypto_major avg `2.0099` n `8`; equity avg `0.5234` n `134`; fx avg `-0.019` n `6`; index avg `0.0767` n `26`; metal avg `0.0032` n `20`; unknown avg `492.6044` n `677`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1005`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0844`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
