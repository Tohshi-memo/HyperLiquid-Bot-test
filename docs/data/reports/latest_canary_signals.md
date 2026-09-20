# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-20T09:22:32.448777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0089` n `12`; crypto_alt avg `0.2508` n `234`; crypto_major avg `0.1983` n `8`; equity avg `0.0076` n `140`; fx avg `-0.0004` n `6`; index avg `-0.0045` n `26`; metal avg `0.0143` n `20`; unknown avg `0.6226` n `943`
- 1h: commodity avg `-0.0246` n `12`; crypto_alt avg `0.0491` n `234`; crypto_major avg `0.0694` n `8`; equity avg `-0.0412` n `140`; fx avg `0.0052` n `6`; index avg `-0.0075` n `26`; metal avg `0.0134` n `20`; unknown avg `1.4123` n `941`
- 4h: commodity avg `0.006` n `12`; crypto_alt avg `-0.3313` n `234`; crypto_major avg `-0.0409` n `8`; equity avg `-0.0347` n `140`; fx avg `0.0094` n `6`; index avg `-0.0176` n `26`; metal avg `0.0251` n `20`; unknown avg `1.3051` n `905`
- 24h: commodity avg `0.2313` n `12`; crypto_alt avg `-1.1299` n `234`; crypto_major avg `-2.0935` n `8`; equity avg `-0.2572` n `140`; fx avg `-0.0672` n `6`; index avg `-0.07` n `26`; metal avg `0.031` n `20`; unknown avg `0.6202` n `816`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1393`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1202`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1147`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0909`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0806`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0797`, n `668`, weak_sample_signal
