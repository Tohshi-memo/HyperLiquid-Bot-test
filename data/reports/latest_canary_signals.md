# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T01:07:27.901159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0288` n `13`; crypto_alt avg `-0.1926` n `235`; crypto_major avg `-0.1348` n `8`; equity avg `-0.1404` n `151`; fx avg `0.0093` n `6`; index avg `-0.0167` n `26`; metal avg `0.0362` n `20`; unknown avg `0.4598` n `1133`
- 1h: commodity avg `0.1807` n `13`; crypto_alt avg `0.0491` n `235`; crypto_major avg `0.2274` n `8`; equity avg `0.0474` n `151`; fx avg `0.0387` n `6`; index avg `0.0075` n `26`; metal avg `-0.0129` n `20`; unknown avg `0.634` n `1133`
- 4h: commodity avg `0.1582` n `13`; crypto_alt avg `-0.0377` n `235`; crypto_major avg `0.052` n `8`; equity avg `0.0703` n `151`; fx avg `0.0433` n `6`; index avg `-0.0129` n `26`; metal avg `-0.0373` n `20`; unknown avg `0.8055` n `1071`
- 24h: commodity avg `1.033` n `13`; crypto_alt avg `2.6788` n `235`; crypto_major avg `2.361` n `8`; equity avg `0.7501` n `151`; fx avg `0.1503` n `6`; index avg `0.0623` n `26`; metal avg `-0.2128` n `20`; unknown avg `0.4958` n `947`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1559`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1422`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1124`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1035`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0978`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0857`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0769`, n `666`, weak_sample_signal
