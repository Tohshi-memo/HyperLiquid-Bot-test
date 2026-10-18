# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T09:07:28.518664+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0123` n `13`; crypto_alt avg `0.4865` n `237`; crypto_major avg `0.4119` n `8`; equity avg `0.1469` n `151`; fx avg `-0.0117` n `6`; index avg `0.006` n `26`; metal avg `0.011` n `20`; unknown avg `0.7321` n `1167`
- 1h: commodity avg `0.0052` n `13`; crypto_alt avg `0.4033` n `237`; crypto_major avg `0.4191` n `8`; equity avg `0.2196` n `151`; fx avg `-0.012` n `6`; index avg `0.0206` n `26`; metal avg `0.0122` n `20`; unknown avg `1.4812` n `1127`
- 4h: commodity avg `0.0204` n `13`; crypto_alt avg `-0.0362` n `237`; crypto_major avg `0.1145` n `8`; equity avg `0.2236` n `151`; fx avg `-0.0081` n `6`; index avg `0.0324` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.7698` n `1095`
- 24h: commodity avg `0.0468` n `13`; crypto_alt avg `-2.3377` n `236`; crypto_major avg `-0.5906` n `8`; equity avg `-0.5981` n `151`; fx avg `-0.0336` n `6`; index avg `-0.0645` n `26`; metal avg `-0.0627` n `20`; unknown avg `5.087` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1829`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1331`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1158`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1119`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0848`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0758`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
