# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T10:37:47.175123+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0047` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0132` n `13`; crypto_alt avg `-0.5338` n `237`; crypto_major avg `-0.4459` n `8`; equity avg `-0.0963` n `151`; fx avg `0.0109` n `6`; index avg `0.0031` n `26`; metal avg `-0.0003` n `20`; unknown avg `0.2031` n `1195`
- 1h: commodity avg `0.1371` n `13`; crypto_alt avg `-1.0194` n `237`; crypto_major avg `-1.0025` n `8`; equity avg `-0.0717` n `151`; fx avg `0.0118` n `6`; index avg `0.0022` n `26`; metal avg `-0.015` n `20`; unknown avg `1.0354` n `1193`
- 4h: commodity avg `0.3871` n `13`; crypto_alt avg `-0.9449` n `237`; crypto_major avg `-0.8531` n `8`; equity avg `-0.3868` n `151`; fx avg `0.006` n `6`; index avg `-0.0709` n `26`; metal avg `-0.051` n `20`; unknown avg `1.6052` n `1146`
- 24h: commodity avg `-0.0541` n `13`; crypto_alt avg `-0.7418` n `237`; crypto_major avg `-0.1038` n `8`; equity avg `2.2599` n `151`; fx avg `-0.0342` n `6`; index avg `0.4181` n `26`; metal avg `0.2041` n `20`; unknown avg `1.779` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1982`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1449`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1316`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0617`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
