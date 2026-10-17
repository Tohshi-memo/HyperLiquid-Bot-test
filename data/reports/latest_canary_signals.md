# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T00:52:27.732722+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0127` n `13`; crypto_alt avg `-0.1234` n `236`; crypto_major avg `-0.1971` n `8`; equity avg `-0.0443` n `151`; fx avg `-0.0187` n `6`; index avg `-0.0124` n `26`; metal avg `-0.0051` n `20`; unknown avg `0.1279` n `1193`
- 1h: commodity avg `0.0494` n `13`; crypto_alt avg `-0.3381` n `236`; crypto_major avg `-0.3103` n `8`; equity avg `0.0666` n `151`; fx avg `-0.0079` n `6`; index avg `0.0069` n `26`; metal avg `-0.0067` n `20`; unknown avg `0.0351` n `1185`
- 4h: commodity avg `0.1262` n `13`; crypto_alt avg `0.1516` n `236`; crypto_major avg `-0.0273` n `8`; equity avg `-0.2775` n `151`; fx avg `-0.0083` n `6`; index avg `-0.0219` n `26`; metal avg `-0.0013` n `20`; unknown avg `0.2913` n `1177`
- 24h: commodity avg `0.511` n `13`; crypto_alt avg `-1.5094` n `236`; crypto_major avg `-1.3106` n `8`; equity avg `-3.8017` n `151`; fx avg `-0.0307` n `6`; index avg `-0.6186` n `26`; metal avg `-0.0002` n `20`; unknown avg `40.2238` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1697`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1174`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1142`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1046`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0919`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0768`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
