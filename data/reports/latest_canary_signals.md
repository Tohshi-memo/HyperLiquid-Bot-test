# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T00:07:26.877054+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0173` n `13`; crypto_alt avg `0.0552` n `236`; crypto_major avg `-0.0485` n `8`; equity avg `0.1194` n `151`; fx avg `0.0111` n `6`; index avg `0.0219` n `26`; metal avg `0.0131` n `20`; unknown avg `0.7804` n `1185`
- 1h: commodity avg `0.0571` n `13`; crypto_alt avg `0.2233` n `236`; crypto_major avg `-0.0645` n `8`; equity avg `0.3075` n `151`; fx avg `0.0111` n `6`; index avg `0.0124` n `26`; metal avg `0.0141` n `20`; unknown avg `2.4087` n `1185`
- 4h: commodity avg `0.1031` n `13`; crypto_alt avg `0.6403` n `236`; crypto_major avg `0.428` n `8`; equity avg `-0.1279` n `151`; fx avg `0.0105` n `6`; index avg `-0.0096` n `26`; metal avg `0.0155` n `20`; unknown avg `1.8963` n `1127`
- 24h: commodity avg `0.5131` n `13`; crypto_alt avg `-1.1314` n `236`; crypto_major avg `-1.0518` n `8`; equity avg `-3.5232` n `151`; fx avg `0.0429` n `6`; index avg `-0.5434` n `26`; metal avg `-0.0045` n `20`; unknown avg `42.1077` n `910`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1689`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1125`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1014`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.089`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0769`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0706`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
