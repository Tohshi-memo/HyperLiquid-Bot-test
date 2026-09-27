# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T17:52:49.084256+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0006` n `12`; crypto_alt avg `0.191` n `234`; crypto_major avg `0.1223` n `8`; equity avg `0.0258` n `141`; fx avg `0.0006` n `6`; index avg `0.0025` n `26`; metal avg `-0.0021` n `20`; unknown avg `-0.5412` n `962`
- 1h: commodity avg `0.0125` n `12`; crypto_alt avg `0.4733` n `234`; crypto_major avg `0.2341` n `8`; equity avg `0.0939` n `141`; fx avg `-0.0052` n `6`; index avg `0.0167` n `26`; metal avg `0.0017` n `20`; unknown avg `0.0416` n `960`
- 4h: commodity avg `-0.1309` n `12`; crypto_alt avg `0.2999` n `234`; crypto_major avg `-0.3992` n `8`; equity avg `0.0685` n `141`; fx avg `0.0008` n `6`; index avg `0.0149` n `26`; metal avg `-0.0018` n `20`; unknown avg `5.3453` n `954`
- 24h: commodity avg `-0.1326` n `12`; crypto_alt avg `-0.1423` n `234`; crypto_major avg `0.0216` n `8`; equity avg `0.3259` n `141`; fx avg `-0.0228` n `6`; index avg `0.0248` n `26`; metal avg `-0.0118` n `20`; unknown avg `3.4314` n `897`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1644`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1514`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1479`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1436`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1325`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.103`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0902`, n `668`, weak_sample_signal
