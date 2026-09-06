# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T15:57:19.148696+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `12`; crypto_alt avg `0.2345` n `232`; crypto_major avg `-0.021` n `8`; equity avg `0.0199` n `134`; fx avg `-0.0031` n `6`; index avg `-0.0052` n `26`; metal avg `-0.0032` n `20`; unknown avg `0.8265` n `792`
- 1h: commodity avg `-0.0126` n `12`; crypto_alt avg `0.2744` n `232`; crypto_major avg `-0.1534` n `8`; equity avg `0.0399` n `134`; fx avg `-0.0214` n `6`; index avg `0.0211` n `26`; metal avg `-0.0141` n `20`; unknown avg `147.3921` n `790`
- 4h: commodity avg `0.0438` n `12`; crypto_alt avg `-0.751` n `232`; crypto_major avg `-0.6723` n `8`; equity avg `-0.2239` n `134`; fx avg `-0.0044` n `6`; index avg `-0.0264` n `26`; metal avg `-0.0221` n `20`; unknown avg `67.5045` n `720`
- 24h: commodity avg `0.0924` n `12`; crypto_alt avg `1.5738` n `232`; crypto_major avg `0.6653` n `8`; equity avg `0.2419` n `134`; fx avg `-0.0354` n `6`; index avg `0.0329` n `26`; metal avg `-0.0191` n `20`; unknown avg `1.842` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1465`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1362`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
