# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T05:52:27.272806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0142` n `13`; crypto_alt avg `-0.1787` n `235`; crypto_major avg `-0.112` n `8`; equity avg `-0.1714` n `151`; fx avg `-0.0025` n `6`; index avg `-0.0214` n `26`; metal avg `-0.0268` n `20`; unknown avg `1.8095` n `1135`
- 1h: commodity avg `-0.0226` n `13`; crypto_alt avg `-1.0452` n `235`; crypto_major avg `-0.5823` n `8`; equity avg `-0.684` n `151`; fx avg `0.0157` n `6`; index avg `-0.1082` n `26`; metal avg `-0.075` n `20`; unknown avg `1.6163` n `1133`
- 4h: commodity avg `-0.1568` n `13`; crypto_alt avg `-0.6126` n `235`; crypto_major avg `-0.2556` n `8`; equity avg `-0.6268` n `151`; fx avg `-0.0002` n `6`; index avg `-0.0697` n `26`; metal avg `0.0901` n `20`; unknown avg `-0.3935` n `1127`
- 24h: commodity avg `0.9635` n `13`; crypto_alt avg `-1.4494` n `235`; crypto_major avg `-0.7184` n `8`; equity avg `-0.2697` n `151`; fx avg `0.0402` n `6`; index avg `0.0438` n `26`; metal avg `-0.3558` n `20`; unknown avg `0.5097` n `979`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1551`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1378`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1201`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1145`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0847`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0824`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `666`, weak_sample_signal
