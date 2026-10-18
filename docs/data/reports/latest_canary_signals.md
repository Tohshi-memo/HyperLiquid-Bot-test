# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T15:22:32.676282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3539` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.012` n `13`; crypto_alt avg `-0.2815` n `237`; crypto_major avg `-0.0829` n `8`; equity avg `-0.0786` n `151`; fx avg `0.0` n `6`; index avg `-0.0096` n `26`; metal avg `-0.0106` n `20`; unknown avg `-0.1613` n `1193`
- 1h: commodity avg `-0.0035` n `13`; crypto_alt avg `-0.6433` n `237`; crypto_major avg `-0.4216` n `8`; equity avg `-0.1347` n `151`; fx avg `0.0045` n `6`; index avg `-0.0133` n `26`; metal avg `-0.0035` n `20`; unknown avg `-0.4643` n `1191`
- 4h: commodity avg `0.0541` n `13`; crypto_alt avg `-1.4296` n `237`; crypto_major avg `-1.4517` n `8`; equity avg `-0.5189` n `151`; fx avg `0.0004` n `6`; index avg `-0.0978` n `26`; metal avg `-0.0418` n `20`; unknown avg `-0.334` n `1183`
- 24h: commodity avg `-0.0273` n `13`; crypto_alt avg `-3.2309` n `236`; crypto_major avg `-1.3016` n `8`; equity avg `-0.9191` n `151`; fx avg `-0.0429` n `6`; index avg `-0.1371` n `26`; metal avg `-0.067` n `20`; unknown avg `0.1191` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.21`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1399`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1294`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1093`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.08`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
