# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T20:22:28.111077+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.017` n `12`; crypto_alt avg `0.0286` n `234`; crypto_major avg `-0.002` n `8`; equity avg `0.0086` n `140`; fx avg `-0.0404` n `6`; index avg `-0.0012` n `26`; metal avg `0.0042` n `20`; unknown avg `0.2967` n `943`
- 1h: commodity avg `-0.0235` n `12`; crypto_alt avg `0.1423` n `234`; crypto_major avg `-0.1077` n `8`; equity avg `0.0577` n `140`; fx avg `-0.0398` n `6`; index avg `-0.0002` n `26`; metal avg `0.0017` n `20`; unknown avg `2.9686` n `919`
- 4h: commodity avg `0.0796` n `12`; crypto_alt avg `0.0311` n `234`; crypto_major avg `-0.4158` n `8`; equity avg `0.1093` n `140`; fx avg `-0.0408` n `6`; index avg `0.0104` n `26`; metal avg `0.0131` n `20`; unknown avg `172.4822` n `879`
- 24h: commodity avg `0.051` n `12`; crypto_alt avg `1.6684` n `234`; crypto_major avg `0.0784` n `8`; equity avg `-0.0473` n `140`; fx avg `-0.0462` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0508` n `20`; unknown avg `7.6879` n `812`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1697`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1537`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1476`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.132`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1089`, n `668`, weak_sample_signal
