# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T22:07:33.095030+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.479` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0046` n `13`; crypto_alt avg `-0.1835` n `239`; crypto_major avg `-0.1874` n `8`; equity avg `0.1609` n `165`; fx avg `-0.0179` n `6`; index avg `0.0172` n `27`; metal avg `-0.0074` n `20`; unknown avg `-0.0559` n `1246`
- 1h: commodity avg `0.0297` n `13`; crypto_alt avg `-0.4853` n `239`; crypto_major avg `-0.7183` n `8`; equity avg `-1.1485` n `165`; fx avg `-0.0221` n `6`; index avg `-0.0133` n `27`; metal avg `-0.2764` n `20`; unknown avg `-0.4409` n `1248`
- 4h: commodity avg `-0.1241` n `13`; crypto_alt avg `-0.6585` n `239`; crypto_major avg `-1.614` n `8`; equity avg `-2.2301` n `165`; fx avg `-0.021` n `6`; index avg `-0.135` n `27`; metal avg `-0.4306` n `20`; unknown avg `5.8662` n `1226`
- 24h: commodity avg `0.0827` n `13`; crypto_alt avg `-0.8791` n `239`; crypto_major avg `-0.6741` n `8`; equity avg `-3.3248` n `165`; fx avg `-0.0304` n `6`; index avg `-0.1837` n `27`; metal avg `-0.8621` n `20`; unknown avg `8.4763` n `1168`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1613`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1591`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0859`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0616`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
