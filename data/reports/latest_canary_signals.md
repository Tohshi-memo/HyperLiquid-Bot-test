# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T04:48:08.169542+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0112` n `12`; crypto_alt avg `0.2313` n `228`; crypto_major avg `0.2805` n `8`; equity avg `0.0708` n `66`; fx avg `0.0058` n `5`; index avg `0.0377` n `23`; metal avg `-0.0805` n `18`; unknown avg `-0.2657` n `383`
- 1h: commodity avg `0.0425` n `12`; crypto_alt avg `0.3325` n `228`; crypto_major avg `0.2785` n `8`; equity avg `-0.0224` n `66`; fx avg `0.0082` n `5`; index avg `0.0369` n `23`; metal avg `0.1403` n `18`; unknown avg `-0.4467` n `383`
- 4h: commodity avg `0.2292` n `12`; crypto_alt avg `0.5626` n `228`; crypto_major avg `-0.0398` n `8`; equity avg `0.7105` n `66`; fx avg `0.065` n `5`; index avg `0.2813` n `23`; metal avg `0.636` n `18`; unknown avg `-0.7799` n `383`
- 24h: commodity avg `2.7151` n `12`; crypto_alt avg `-10.7482` n `228`; crypto_major avg `-3.1854` n `8`; equity avg `-3.057` n `65`; fx avg `-0.061` n `5`; index avg `-1.7404` n `23`; metal avg `-6.1679` n `18`; unknown avg `550.05` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1077`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0848`, n `668`, weak_sample_signal
