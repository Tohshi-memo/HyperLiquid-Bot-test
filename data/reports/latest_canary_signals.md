# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T14:37:28.033421+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.4495` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.004` n `13`; crypto_alt avg `-0.6951` n `237`; crypto_major avg `-0.4792` n `8`; equity avg `-0.1063` n `151`; fx avg `-0.0037` n `6`; index avg `0.0018` n `26`; metal avg `-0.0096` n `20`; unknown avg `-0.2112` n `1193`
- 1h: commodity avg `0.0074` n `13`; crypto_alt avg `-0.8541` n `237`; crypto_major avg `-0.4092` n `8`; equity avg `-0.1712` n `151`; fx avg `-0.0133` n `6`; index avg `-0.0319` n `26`; metal avg `-0.0286` n `20`; unknown avg `-0.3851` n `1191`
- 4h: commodity avg `0.0675` n `13`; crypto_alt avg `-1.4269` n `237`; crypto_major avg `-1.5525` n `8`; equity avg `-0.5531` n `151`; fx avg `-0.0014` n `6`; index avg `-0.103` n `26`; metal avg `-0.053` n `20`; unknown avg `-0.1719` n `1183`
- 24h: commodity avg `0.0385` n `13`; crypto_alt avg `-3.5013` n `236`; crypto_major avg `-1.5464` n `8`; equity avg `-1.0164` n `151`; fx avg `-0.0426` n `6`; index avg `-0.1391` n `26`; metal avg `-0.0802` n `20`; unknown avg `0.5699` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2088`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1387`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1239`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1056`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.088`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0797`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
