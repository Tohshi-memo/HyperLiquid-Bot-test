# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-14T20:52:36.752130+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5005` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.2872` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0036` n `13`; crypto_alt avg `-0.4512` n `239`; crypto_major avg `-0.4561` n `8`; equity avg `-0.1361` n `162`; fx avg `-0.0072` n `6`; index avg `-0.0041` n `27`; metal avg `-0.0189` n `20`; unknown avg `40.1919` n `1260`
- 1h: commodity avg `0.0233` n `13`; crypto_alt avg `-1.5663` n `239`; crypto_major avg `-1.3029` n `8`; equity avg `-0.3664` n `162`; fx avg `-0.0034` n `6`; index avg `-0.0157` n `27`; metal avg `-0.1313` n `20`; unknown avg `-0.1522` n `1230`
- 4h: commodity avg `0.0376` n `13`; crypto_alt avg `-2.263` n `239`; crypto_major avg `-1.4932` n `8`; equity avg `-0.2799` n `162`; fx avg `-0.0056` n `6`; index avg `0.0073` n `27`; metal avg `-0.1368` n `20`; unknown avg `1.2716` n `1230`
- 24h: commodity avg `-0.0185` n `13`; crypto_alt avg `-8.7713` n `239`; crypto_major avg `-8.0626` n `8`; equity avg `-2.5682` n `162`; fx avg `-0.0255` n `6`; index avg `-0.2155` n `27`; metal avg `-0.3821` n `20`; unknown avg `1.8596` n `1082`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1414`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
