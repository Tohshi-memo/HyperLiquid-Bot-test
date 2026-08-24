# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-24T04:11:13.938567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0175` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `0.0248` n `231`; crypto_major avg `-0.0141` n `8`; equity avg `0.0026` n `122`; fx avg `0.0023` n `6`; index avg `0.0003` n `25`; metal avg `-0.0508` n `20`; unknown avg `-0.0486` n `793`
- 1h: commodity avg `-0.0027` n `12`; crypto_alt avg `-0.0863` n `231`; crypto_major avg `-0.2146` n `8`; equity avg `-0.2338` n `122`; fx avg `0.0022` n `6`; index avg `-0.0499` n `25`; metal avg `-0.0131` n `20`; unknown avg `-0.1076` n `793`
- 4h: commodity avg `-0.0909` n `12`; crypto_alt avg `-1.4296` n `231`; crypto_major avg `-1.1985` n `8`; equity avg `-1.6656` n `122`; fx avg `-0.0261` n `6`; index avg `-0.181` n `25`; metal avg `-0.1227` n `20`; unknown avg `0.3869` n `793`
- 24h: commodity avg `-0.2977` n `12`; crypto_alt avg `3.6022` n `231`; crypto_major avg `0.6889` n `8`; equity avg `-1.1198` n `122`; fx avg `-0.1816` n `6`; index avg `-0.1065` n `25`; metal avg `0.1061` n `20`; unknown avg `5.9297` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1065`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0861`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
