# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-13T12:07:29.314100+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3283` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0457` n `13`; crypto_alt avg `-0.0064` n `235`; crypto_major avg `-0.1129` n `8`; equity avg `-0.1991` n `151`; fx avg `0.0091` n `6`; index avg `-0.0023` n `26`; metal avg `-0.0037` n `20`; unknown avg `0.0881` n `1127`
- 1h: commodity avg `0.1119` n `13`; crypto_alt avg `-0.1746` n `235`; crypto_major avg `0.085` n `8`; equity avg `-0.146` n `151`; fx avg `0.0165` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0118` n `20`; unknown avg `-0.1733` n `1127`
- 4h: commodity avg `0.0926` n `13`; crypto_alt avg `-2.1034` n `235`; crypto_major avg `-1.3631` n `8`; equity avg `-0.5161` n `151`; fx avg `-0.0108` n `6`; index avg `-0.0348` n `26`; metal avg `-0.0612` n `20`; unknown avg `0.5884` n `1127`
- 24h: commodity avg `0.0025` n `13`; crypto_alt avg `-4.598` n `235`; crypto_major avg `-2.4105` n `8`; equity avg `-3.1048` n `151`; fx avg `0.0763` n `6`; index avg `-0.3654` n `26`; metal avg `-0.032` n `20`; unknown avg `0.0582` n `990`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1688`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1678`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1495`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1451`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0843`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
