# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T07:22:28.741694+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.005` n `13`; crypto_alt avg `-0.2075` n `235`; crypto_major avg `-0.1227` n `8`; equity avg `-0.1492` n `151`; fx avg `-0.0101` n `6`; index avg `-0.0242` n `26`; metal avg `-0.0513` n `20`; unknown avg `0.0541` n `1135`
- 1h: commodity avg `0.0083` n `13`; crypto_alt avg `-0.017` n `235`; crypto_major avg `0.0312` n `8`; equity avg `0.0266` n `151`; fx avg `-0.0521` n `6`; index avg `0.0175` n `26`; metal avg `-0.1206` n `20`; unknown avg `0.248` n `1133`
- 4h: commodity avg `-0.0517` n `13`; crypto_alt avg `-0.6444` n `235`; crypto_major avg `-0.3166` n `8`; equity avg `-0.8275` n `151`; fx avg `-0.0476` n `6`; index avg `-0.1203` n `26`; metal avg `-0.1917` n `20`; unknown avg `0.1595` n `1111`
- 24h: commodity avg `1.0552` n `13`; crypto_alt avg `-1.1505` n `235`; crypto_major avg `-0.5517` n `8`; equity avg `-0.0132` n `151`; fx avg `-0.0008` n `6`; index avg `0.0213` n `26`; metal avg `-0.5356` n `20`; unknown avg `0.2707` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1553`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1356`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1275`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1117`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1007`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.083`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0692`, n `666`, weak_sample_signal
