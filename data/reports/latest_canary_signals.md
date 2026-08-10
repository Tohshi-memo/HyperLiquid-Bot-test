# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T19:07:34.277007+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.073` n `12`; crypto_alt avg `-0.0544` n `230`; crypto_major avg `0.1337` n `8`; equity avg `0.0029` n `113`; fx avg `-0.015` n `6`; index avg `0.011` n `25`; metal avg `0.0565` n `20`; unknown avg `-0.017` n `785`
- 1h: commodity avg `-0.0407` n `12`; crypto_alt avg `-0.2161` n `230`; crypto_major avg `-0.0205` n `8`; equity avg `-0.0103` n `113`; fx avg `0.0004` n `6`; index avg `0.0218` n `25`; metal avg `0.184` n `20`; unknown avg `-0.1557` n `785`
- 4h: commodity avg `0.1629` n `12`; crypto_alt avg `-0.3534` n `230`; crypto_major avg `-0.3538` n `8`; equity avg `-0.2137` n `113`; fx avg `-0.0001` n `6`; index avg `-0.0168` n `25`; metal avg `0.2428` n `20`; unknown avg `-0.1264` n `784`
- 24h: commodity avg `1.091` n `12`; crypto_alt avg `-0.9593` n `230`; crypto_major avg `-1.2567` n `8`; equity avg `-1.3663` n `113`; fx avg `0.2454` n `6`; index avg `-0.068` n `25`; metal avg `0.1713` n `20`; unknown avg `103.6397` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1728`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1653`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1512`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1503`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
