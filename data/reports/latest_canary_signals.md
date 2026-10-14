# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T12:52:29.486402+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0301` n `13`; crypto_alt avg `-0.2081` n `235`; crypto_major avg `-0.0383` n `8`; equity avg `-0.1063` n `151`; fx avg `-0.0165` n `6`; index avg `0.0088` n `26`; metal avg `-0.0341` n `20`; unknown avg `19.7526` n `1136`
- 1h: commodity avg `-0.1599` n `13`; crypto_alt avg `-0.9149` n `235`; crypto_major avg `-0.7249` n `8`; equity avg `-0.8575` n `151`; fx avg `-0.0765` n `6`; index avg `-0.1603` n `26`; metal avg `-0.2261` n `20`; unknown avg `2.9601` n `1128`
- 4h: commodity avg `-0.1253` n `13`; crypto_alt avg `-1.3199` n `235`; crypto_major avg `-0.7199` n `8`; equity avg `-1.1785` n `151`; fx avg `-0.0565` n `6`; index avg `-0.1891` n `26`; metal avg `-0.2274` n `20`; unknown avg `3.097` n `1095`
- 24h: commodity avg `0.816` n `13`; crypto_alt avg `-1.0675` n `235`; crypto_major avg `-0.423` n `8`; equity avg `-0.7639` n `151`; fx avg `-0.0809` n `6`; index avg `-0.1172` n `26`; metal avg `-0.5631` n `20`; unknown avg `1270.9877` n `975`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1491`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1261`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1154`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1084`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1027`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0627`, n `666`, weak_sample_signal
