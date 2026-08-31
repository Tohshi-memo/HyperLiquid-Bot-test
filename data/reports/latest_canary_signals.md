# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-31T22:07:25.379550+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0122` n `12`; crypto_alt avg `-0.1688` n `232`; crypto_major avg `-0.1183` n `8`; equity avg `-0.0196` n `129`; fx avg `-0.0002` n `6`; index avg `-0.0047` n `26`; metal avg `0.0141` n `20`; unknown avg `-0.0056` n `791`
- 1h: commodity avg `-0.0398` n `12`; crypto_alt avg `0.311` n `232`; crypto_major avg `0.1674` n `8`; equity avg `0.0683` n `129`; fx avg `0.0001` n `6`; index avg `-0.0223` n `26`; metal avg `0.0248` n `20`; unknown avg `-0.13` n `791`
- 4h: commodity avg `0.111` n `12`; crypto_alt avg `0.2963` n `232`; crypto_major avg `0.1954` n `8`; equity avg `0.3885` n `129`; fx avg `0.0029` n `6`; index avg `0.0499` n `26`; metal avg `0.1095` n `20`; unknown avg `1.0528` n `773`
- 24h: commodity avg `0.1903` n `12`; crypto_alt avg `-0.3296` n `231`; crypto_major avg `-0.0353` n `8`; equity avg `0.2539` n `129`; fx avg `-0.0754` n `6`; index avg `-0.0516` n `26`; metal avg `-0.1881` n `20`; unknown avg `0.0442` n `740`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0993`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0591`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0553`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0497`, n `668`, weak_sample_signal
