# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-24T01:22:28.630280+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0084` n `13`; crypto_alt avg `0.308` n `237`; crypto_major avg `0.1812` n `8`; equity avg `0.0317` n `152`; fx avg `0.005` n `6`; index avg `0.0001` n `26`; metal avg `-0.0005` n `20`; unknown avg `-0.1632` n `1230`
- 1h: commodity avg `-0.0529` n `13`; crypto_alt avg `0.618` n `237`; crypto_major avg `0.2803` n `8`; equity avg `0.1244` n `152`; fx avg `-0.0007` n `6`; index avg `0.0019` n `26`; metal avg `0.0197` n `20`; unknown avg `3.6887` n `1230`
- 4h: commodity avg `0.0901` n `13`; crypto_alt avg `-0.9146` n `237`; crypto_major avg `-0.8271` n `8`; equity avg `-0.151` n `152`; fx avg `-0.0044` n `6`; index avg `-0.0437` n `26`; metal avg `-0.0605` n `20`; unknown avg `4.8642` n `1208`
- 24h: commodity avg `0.4557` n `13`; crypto_alt avg `-0.7053` n `237`; crypto_major avg `-0.57` n `8`; equity avg `0.827` n `152`; fx avg `-0.0011` n `6`; index avg `0.0499` n `26`; metal avg `-0.1286` n `20`; unknown avg `205.1022` n `1018`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1968`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1544`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1435`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1305`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
