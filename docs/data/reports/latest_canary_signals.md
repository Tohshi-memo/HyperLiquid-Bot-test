# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T01:07:26.248490+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0005` n `12`; crypto_alt avg `-0.1629` n `234`; crypto_major avg `-0.095` n `8`; equity avg `-0.0053` n `140`; fx avg `0.0083` n `6`; index avg `0.0051` n `26`; metal avg `-0.0004` n `20`; unknown avg `1.0997` n `941`
- 1h: commodity avg `-0.0156` n `12`; crypto_alt avg `0.2272` n `234`; crypto_major avg `-0.0342` n `8`; equity avg `0.035` n `140`; fx avg `0.0194` n `6`; index avg `-0.0069` n `26`; metal avg `-0.0012` n `20`; unknown avg `0.9304` n `941`
- 4h: commodity avg `0.0934` n `12`; crypto_alt avg `0.4675` n `234`; crypto_major avg `-0.2964` n `8`; equity avg `0.0153` n `140`; fx avg `0.0146` n `6`; index avg `-0.0316` n `26`; metal avg `-0.0026` n `20`; unknown avg `0.6896` n `911`
- 24h: commodity avg `0.003` n `12`; crypto_alt avg `1.1242` n `234`; crypto_major avg `-0.6167` n `8`; equity avg `0.0116` n `140`; fx avg `-0.0317` n `6`; index avg `-0.0153` n `26`; metal avg `0.0251` n `20`; unknown avg `0.2727` n `822`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1734`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1587`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1347`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1153`, n `668`, weak_sample_signal
