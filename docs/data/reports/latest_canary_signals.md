# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T02:52:28.723391+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0074` n `12`; crypto_alt avg `0.1023` n `233`; crypto_major avg `0.1052` n `8`; equity avg `-0.0242` n `136`; fx avg `-0.0025` n `6`; index avg `-0.0125` n `26`; metal avg `0.0013` n `20`; unknown avg `1.0854` n `838`
- 1h: commodity avg `0.0091` n `12`; crypto_alt avg `-0.1456` n `233`; crypto_major avg `0.013` n `8`; equity avg `-0.0542` n `136`; fx avg `0.0037` n `6`; index avg `-0.0197` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.974` n `812`
- 4h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.6129` n `233`; crypto_major avg `0.2179` n `8`; equity avg `-0.1012` n `136`; fx avg `0.0042` n `6`; index avg `-0.0303` n `26`; metal avg `0.002` n `20`; unknown avg `3.6199` n `806`
- 24h: commodity avg `0.0026` n `12`; crypto_alt avg `0.9902` n `233`; crypto_major avg `0.334` n `8`; equity avg `-0.4857` n `136`; fx avg `-0.0118` n `6`; index avg `-0.0493` n `26`; metal avg `0.0303` n `20`; unknown avg `0.0082` n `706`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0668`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0578`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0523`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.049`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0447`, n `668`, weak_sample_signal
