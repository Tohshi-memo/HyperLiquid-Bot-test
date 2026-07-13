# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-13T11:37:28.045842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0187` n `12`; crypto_alt avg `-0.0928` n `230`; crypto_major avg `-0.0857` n `8`; equity avg `0.0791` n `92`; fx avg `-0.0086` n `6`; index avg `-0.0018` n `25`; metal avg `0.0889` n `20`; unknown avg `-0.0482` n `766`
- 1h: commodity avg `0.0069` n `12`; crypto_alt avg `0.0313` n `230`; crypto_major avg `0.1299` n `8`; equity avg `0.2887` n `92`; fx avg `0.0002` n `6`; index avg `0.0497` n `25`; metal avg `0.1117` n `20`; unknown avg `-0.0289` n `766`
- 4h: commodity avg `-0.0735` n `12`; crypto_alt avg `-0.0033` n `230`; crypto_major avg `-0.2817` n `8`; equity avg `0.579` n `92`; fx avg `-0.0797` n `6`; index avg `0.0664` n `25`; metal avg `0.1343` n `20`; unknown avg `-0.1465` n `766`
- 24h: commodity avg `-0.162` n `12`; crypto_alt avg `-1.0079` n `230`; crypto_major avg `-1.3547` n `8`; equity avg `-1.8478` n `92`; fx avg `-0.0634` n `6`; index avg `-0.412` n `25`; metal avg `-0.171` n `20`; unknown avg `-0.1329` n `743`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1942`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1759`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1317`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1309`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1026`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
