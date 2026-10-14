# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T04:07:28.151786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0384` n `13`; crypto_alt avg `-0.2283` n `235`; crypto_major avg `-0.2259` n `8`; equity avg `0.035` n `151`; fx avg `0.0079` n `6`; index avg `0.0143` n `26`; metal avg `-0.029` n `20`; unknown avg `-0.1689` n `1127`
- 1h: commodity avg `-0.0676` n `13`; crypto_alt avg `-0.1509` n `235`; crypto_major avg `-0.1463` n `8`; equity avg `-0.0212` n `151`; fx avg `-0.0192` n `6`; index avg `0.0061` n `26`; metal avg `-0.0454` n `20`; unknown avg `-0.0734` n `1127`
- 4h: commodity avg `-0.0002` n `13`; crypto_alt avg `0.2884` n `235`; crypto_major avg `0.4361` n `8`; equity avg `0.2302` n `151`; fx avg `0.0081` n `6`; index avg `0.0746` n `26`; metal avg `0.0501` n `20`; unknown avg `0.3152` n `1127`
- 24h: commodity avg `1.0989` n `13`; crypto_alt avg `0.1767` n `235`; crypto_major avg `0.1168` n `8`; equity avg `0.6144` n `151`; fx avg `0.0523` n `6`; index avg `0.191` n `26`; metal avg `-0.3173` n `20`; unknown avg `0.8102` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1522`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1363`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1177`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1153`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0881`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0747`, n `666`, weak_sample_signal
