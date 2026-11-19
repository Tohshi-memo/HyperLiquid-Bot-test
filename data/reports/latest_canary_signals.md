# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T22:22:27.084259+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.6667` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0073` n `13`; crypto_alt avg `0.1905` n `239`; crypto_major avg `0.3468` n `8`; equity avg `0.1953` n `165`; fx avg `0.0017` n `6`; index avg `0.0115` n `27`; metal avg `0.0258` n `20`; unknown avg `0.2093` n `1260`
- 1h: commodity avg `-0.0078` n `13`; crypto_alt avg `0.1044` n `239`; crypto_major avg `0.1777` n `8`; equity avg `0.1434` n `165`; fx avg `-0.0138` n `6`; index avg `0.0115` n `27`; metal avg `-0.1478` n `20`; unknown avg `-0.0727` n `1250`
- 4h: commodity avg `-0.0963` n `13`; crypto_alt avg `-0.8808` n `239`; crypto_major avg `-1.803` n `8`; equity avg `-2.1649` n `165`; fx avg `-0.0303` n `6`; index avg `-0.1363` n `27`; metal avg `-0.4071` n `20`; unknown avg `5.7377` n `1230`
- 24h: commodity avg `0.0904` n `13`; crypto_alt avg `-0.6441` n `239`; crypto_major avg `-0.3869` n `8`; equity avg `-3.0595` n `165`; fx avg `-0.0337` n `6`; index avg `-0.1683` n `27`; metal avg `-0.8433` n `20`; unknown avg `8.3307` n `1172`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1323`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
