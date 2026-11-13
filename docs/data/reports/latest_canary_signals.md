# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-13T06:07:32.022083+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.9686` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `-2.6905` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `2.6784` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0776` n `13`; crypto_alt avg `-0.1215` n `239`; crypto_major avg `-0.3682` n `8`; equity avg `-0.1096` n `162`; fx avg `0.0277` n `6`; index avg `-0.0133` n `27`; metal avg `0.0228` n `20`; unknown avg `162.889` n `1226`
- 1h: commodity avg `0.085` n `13`; crypto_alt avg `0.6823` n `239`; crypto_major avg `0.2038` n `8`; equity avg `-0.3817` n `162`; fx avg `0.0354` n `6`; index avg `-0.0449` n `27`; metal avg `-0.1477` n `20`; unknown avg `-0.0425` n `1226`
- 4h: commodity avg `0.0661` n `13`; crypto_alt avg `-2.2281` n `239`; crypto_major avg `-2.9025` n `8`; equity avg `-2.1116` n `162`; fx avg `0.0439` n `6`; index avg `-0.2241` n `27`; metal avg `-0.212` n `20`; unknown avg `0.7967` n `1216`
- 24h: commodity avg `0.7204` n `13`; crypto_alt avg `-2.4639` n `239`; crypto_major avg `-4.3145` n `8`; equity avg `-1.2118` n `162`; fx avg `0.0492` n `6`; index avg `-0.0028` n `27`; metal avg `-0.5574` n `20`; unknown avg `98.8763` n `1129`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1415`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1353`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0756`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0738`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0713`, n `668`, weak_sample_signal
