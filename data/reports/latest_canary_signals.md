# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T20:07:25.716399+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0008` n `12`; crypto_alt avg `-0.1296` n `234`; crypto_major avg `-0.1186` n `8`; equity avg `0.0222` n `140`; fx avg `0.0031` n `6`; index avg `0.0012` n `26`; metal avg `-0.0006` n `20`; unknown avg `0.1871` n `927`
- 1h: commodity avg `-0.0397` n `12`; crypto_alt avg `0.0769` n `234`; crypto_major avg `-0.1841` n `8`; equity avg `0.0609` n `140`; fx avg `-0.0027` n `6`; index avg `-0.0002` n `26`; metal avg `-0.0069` n `20`; unknown avg `53.6609` n `919`
- 4h: commodity avg `0.0394` n `12`; crypto_alt avg `0.2009` n `234`; crypto_major avg `-0.2931` n `8`; equity avg `0.1224` n `140`; fx avg `-0.0054` n `6`; index avg `0.021` n `26`; metal avg `0.0077` n `20`; unknown avg `178.8902` n `879`
- 24h: commodity avg `0.0042` n `12`; crypto_alt avg `1.784` n `234`; crypto_major avg `0.1194` n `8`; equity avg `-0.0514` n `140`; fx avg `0.0029` n `6`; index avg `0.0009` n `26`; metal avg `-0.0302` n `20`; unknown avg `6.4517` n `796`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1694`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1539`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1478`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1428`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1232`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1216`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
