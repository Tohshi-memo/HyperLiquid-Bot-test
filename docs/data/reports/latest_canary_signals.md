# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-19T17:22:31.872551+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1263` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0876` n `13`; crypto_alt avg `0.2581` n `239`; crypto_major avg `0.5224` n `8`; equity avg `0.6751` n `165`; fx avg `0.0145` n `6`; index avg `0.0994` n `27`; metal avg `0.1499` n `20`; unknown avg `2.4656` n `1264`
- 1h: commodity avg `-0.093` n `13`; crypto_alt avg `-0.5549` n `239`; crypto_major avg `-0.2461` n `8`; equity avg `-1.4426` n `165`; fx avg `-0.0266` n `6`; index avg `-0.1471` n `27`; metal avg `-0.0214` n `20`; unknown avg `11.5009` n `1263`
- 4h: commodity avg `-0.0675` n `13`; crypto_alt avg `-2.0453` n `239`; crypto_major avg `-1.5186` n `8`; equity avg `-2.8257` n `165`; fx avg `-0.0262` n `6`; index avg `-0.3923` n `27`; metal avg `-0.3461` n `20`; unknown avg `161.5849` n `1257`
- 24h: commodity avg `0.4095` n `13`; crypto_alt avg `-0.7432` n `239`; crypto_major avg `-0.002` n `8`; equity avg `-0.59` n `165`; fx avg `-0.0023` n `6`; index avg `-0.0123` n `27`; metal avg `-0.457` n `20`; unknown avg `3.9129` n `1160`

## Correlations

- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1605`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0602`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0561`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0508`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
