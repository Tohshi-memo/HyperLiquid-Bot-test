# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T19:37:31.026759+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0281` n `13`; crypto_alt avg `-0.153` n `235`; crypto_major avg `-0.1306` n `8`; equity avg `0.0356` n `151`; fx avg `-0.002` n `6`; index avg `-0.0009` n `26`; metal avg `0.027` n `20`; unknown avg `88.7761` n `1135`
- 1h: commodity avg `0.1054` n `13`; crypto_alt avg `0.4412` n `235`; crypto_major avg `0.2554` n `8`; equity avg `0.1513` n `151`; fx avg `-0.0012` n `6`; index avg `0.0176` n `26`; metal avg `0.0295` n `20`; unknown avg `14.624` n `1133`
- 4h: commodity avg `0.2361` n `13`; crypto_alt avg `0.5821` n `235`; crypto_major avg `0.2315` n `8`; equity avg `0.7661` n `151`; fx avg `0.0171` n `6`; index avg `0.1169` n `26`; metal avg `0.0006` n `20`; unknown avg `2.1066` n `1127`
- 24h: commodity avg `0.697` n `13`; crypto_alt avg `-1.5277` n `235`; crypto_major avg `-0.5141` n `8`; equity avg `-0.9179` n `151`; fx avg `0.1757` n `6`; index avg `-0.1679` n `26`; metal avg `-0.2045` n `20`; unknown avg `0.9869` n `1006`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1605`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.144`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1187`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0923`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0862`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0818`, n `666`, weak_sample_signal
