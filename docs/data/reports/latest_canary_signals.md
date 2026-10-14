# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T00:52:36.253672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0511` n `13`; crypto_alt avg `-0.2941` n `235`; crypto_major avg `-0.1858` n `8`; equity avg `-0.1433` n `151`; fx avg `-0.0063` n `6`; index avg `-0.0402` n `26`; metal avg `-0.0227` n `20`; unknown avg `0.0077` n `1135`
- 1h: commodity avg `0.1363` n `13`; crypto_alt avg `0.3155` n `235`; crypto_major avg `0.4364` n `8`; equity avg `0.2795` n `151`; fx avg `0.0214` n `6`; index avg `0.0551` n `26`; metal avg `-0.0164` n `20`; unknown avg `1.2635` n `1133`
- 4h: commodity avg `0.1028` n `13`; crypto_alt avg `0.1741` n `235`; crypto_major avg `0.2147` n `8`; equity avg `0.2113` n `151`; fx avg `0.0176` n `6`; index avg `0.0072` n `26`; metal avg `-0.0524` n `20`; unknown avg `0.3394` n `1065`
- 24h: commodity avg `0.9638` n `13`; crypto_alt avg `4.2072` n `235`; crypto_major avg `3.6151` n `8`; equity avg `0.8955` n `151`; fx avg `0.1723` n `6`; index avg `0.0556` n `26`; metal avg `-0.2031` n `20`; unknown avg `1.0025` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1557`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1417`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0967`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0776`, n `666`, weak_sample_signal
