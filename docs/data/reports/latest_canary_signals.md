# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-16T16:37:28.104589+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0607` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.2259` n `13`; crypto_alt avg `-0.0755` n `236`; crypto_major avg `-0.0131` n `8`; equity avg `-0.0419` n `151`; fx avg `-0.0041` n `6`; index avg `-0.0349` n `26`; metal avg `-0.0388` n `20`; unknown avg `-0.1816` n `1174`
- 1h: commodity avg `0.5756` n `13`; crypto_alt avg `-0.2871` n `236`; crypto_major avg `-0.1299` n `8`; equity avg `-0.2806` n `151`; fx avg `-0.0239` n `6`; index avg `-0.0869` n `26`; metal avg `-0.1153` n `20`; unknown avg `0.4166` n `1140`
- 4h: commodity avg `0.5035` n `13`; crypto_alt avg `-1.7359` n `236`; crypto_major avg `-1.4068` n `8`; equity avg `-2.1529` n `151`; fx avg `0.002` n `6`; index avg `-0.3461` n `26`; metal avg `-0.1827` n `20`; unknown avg `1.3173` n `996`
- 24h: commodity avg `0.1123` n `13`; crypto_alt avg `-0.2635` n `236`; crypto_major avg `-0.6658` n `8`; equity avg `-1.2477` n `151`; fx avg `0.0087` n `6`; index avg `-0.2668` n `26`; metal avg `0.0703` n `20`; unknown avg `-0.1039` n `904`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1223`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0931`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0886`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0885`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0796`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0791`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0746`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
