# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T17:51:43.151390+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0247` n `12`; crypto_alt avg `0.0497` n `234`; crypto_major avg `0.2108` n `8`; equity avg `0.0568` n `140`; fx avg `0.0056` n `6`; index avg `0.0042` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.2795` n `940`
- 1h: commodity avg `0.0083` n `12`; crypto_alt avg `0.2807` n `234`; crypto_major avg `0.2527` n `8`; equity avg `0.1801` n `140`; fx avg `0.0025` n `6`; index avg `0.0252` n `26`; metal avg `0.0623` n `20`; unknown avg `10.3657` n `920`
- 4h: commodity avg `-0.2448` n `12`; crypto_alt avg `0.5336` n `234`; crypto_major avg `0.6637` n `8`; equity avg `0.1249` n `140`; fx avg `-0.0505` n `6`; index avg `-0.0508` n `26`; metal avg `0.1801` n `20`; unknown avg `0.4279` n `884`
- 24h: commodity avg `-0.1991` n `12`; crypto_alt avg `5.7869` n `234`; crypto_major avg `6.3777` n `8`; equity avg `0.7762` n `140`; fx avg `0.1951` n `6`; index avg `-0.1144` n `26`; metal avg `0.326` n `20`; unknown avg `1.6503` n `717`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1495`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1331`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1299`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1093`, n `668`, weak_sample_signal
