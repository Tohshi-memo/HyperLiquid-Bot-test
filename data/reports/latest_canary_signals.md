# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T03:37:36.655251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0167` n `13`; crypto_alt avg `0.1845` n `235`; crypto_major avg `0.1977` n `8`; equity avg `-0.0877` n `151`; fx avg `-0.0078` n `6`; index avg `-0.0183` n `26`; metal avg `-0.0212` n `20`; unknown avg `0.3489` n `1135`
- 1h: commodity avg `-0.0762` n `13`; crypto_alt avg `0.5112` n `235`; crypto_major avg `0.5422` n `8`; equity avg `0.0232` n `151`; fx avg `-0.0003` n `6`; index avg `0.0136` n `26`; metal avg `0.0438` n `20`; unknown avg `1.8693` n `1133`
- 4h: commodity avg `0.07` n `13`; crypto_alt avg `0.7194` n `235`; crypto_major avg `0.8003` n `8`; equity avg `0.2502` n `151`; fx avg `-0.0094` n `6`; index avg `0.0706` n `26`; metal avg `0.1213` n `20`; unknown avg `1.2685` n `1127`
- 24h: commodity avg `0.9766` n `13`; crypto_alt avg `0.7742` n `235`; crypto_major avg `0.5213` n `8`; equity avg `0.7925` n `151`; fx avg `0.0347` n `6`; index avg `0.1925` n `26`; metal avg `-0.1901` n `20`; unknown avg `1.1449` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1515`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1361`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1126`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0897`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0745`, n `666`, weak_sample_signal
