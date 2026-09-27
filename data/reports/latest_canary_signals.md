# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T14:07:27.706320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0042` n `12`; crypto_alt avg `0.1681` n `234`; crypto_major avg `0.1605` n `8`; equity avg `0.0201` n `141`; fx avg `-0.0095` n `6`; index avg `-0.0092` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.0094` n `960`
- 1h: commodity avg `-0.0179` n `12`; crypto_alt avg `0.1488` n `234`; crypto_major avg `0.1545` n `8`; equity avg `0.0384` n `141`; fx avg `-0.0075` n `6`; index avg `-0.0103` n `26`; metal avg `0.0082` n `20`; unknown avg `1.5978` n `960`
- 4h: commodity avg `-0.0052` n `12`; crypto_alt avg `-0.6225` n `234`; crypto_major avg `-0.307` n `8`; equity avg `-0.0191` n `141`; fx avg `-0.0018` n `6`; index avg `-0.033` n `26`; metal avg `-0.0172` n `20`; unknown avg `2.6314` n `954`
- 24h: commodity avg `-0.0241` n `12`; crypto_alt avg `0.3618` n `234`; crypto_major avg `0.7001` n `8`; equity avg `0.3703` n `141`; fx avg `-0.0396` n `6`; index avg `0.0084` n `26`; metal avg `-0.0119` n `20`; unknown avg `65.0754` n `889`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1671`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.153`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1167`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
