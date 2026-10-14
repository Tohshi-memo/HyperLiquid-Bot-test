# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T15:28:17.798806+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3893` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.083` n `13`; crypto_alt avg `0.3596` n `235`; crypto_major avg `0.5812` n `8`; equity avg `0.1365` n `151`; fx avg `-0.0038` n `6`; index avg `0.0106` n `26`; metal avg `0.0291` n `20`; unknown avg `0.2723` n `1113`
- 1h: commodity avg `-0.0285` n `13`; crypto_alt avg `0.1546` n `235`; crypto_major avg `0.369` n `8`; equity avg `-0.2806` n `151`; fx avg `-0.0107` n `6`; index avg `-0.0545` n `26`; metal avg `-0.0782` n `20`; unknown avg `0.0098` n `1110`
- 4h: commodity avg `-0.2651` n `13`; crypto_alt avg `-2.0886` n `235`; crypto_major avg `-1.6885` n `8`; equity avg `-2.0958` n `151`; fx avg `-0.1287` n `6`; index avg `-0.2992` n `26`; metal avg `-0.641` n `20`; unknown avg `3.3264` n `1102`
- 24h: commodity avg `0.0708` n `13`; crypto_alt avg `-2.6598` n `235`; crypto_major avg `-1.9409` n `8`; equity avg `-2.2173` n `151`; fx avg `-0.1674` n `6`; index avg `-0.27` n `26`; metal avg `-0.8001` n `20`; unknown avg `1263.1565` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0926`, n `666`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0864`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0798`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0792`, n `666`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0787`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0673`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0595`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0535`, n `668`, weak_sample_signal
