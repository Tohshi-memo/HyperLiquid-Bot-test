# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-20T06:52:25.627251+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1595` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0891` n `12`; crypto_alt avg `0.2902` n `230`; crypto_major avg `0.1214` n `8`; equity avg `0.1153` n `98`; fx avg `0.0185` n `6`; index avg `0.0034` n `25`; metal avg `0.0061` n `20`; unknown avg `-0.0741` n `769`
- 1h: commodity avg `-0.0314` n `12`; crypto_alt avg `0.1797` n `230`; crypto_major avg `-0.2279` n `8`; equity avg `-0.0575` n `98`; fx avg `-0.0053` n `6`; index avg `-0.0149` n `25`; metal avg `0.0388` n `20`; unknown avg `-0.1837` n `753`
- 4h: commodity avg `0.0204` n `12`; crypto_alt avg `-0.9701` n `230`; crypto_major avg `-1.2729` n `8`; equity avg `-0.411` n `98`; fx avg `-0.0232` n `6`; index avg `-0.1134` n `25`; metal avg `-0.168` n `20`; unknown avg `-0.3924` n `753`
- 24h: commodity avg `-0.1124` n `12`; crypto_alt avg `-0.6986` n `230`; crypto_major avg `-0.9257` n `8`; equity avg `-0.1324` n `97`; fx avg `-0.0394` n `6`; index avg `-0.0285` n `25`; metal avg `-0.0577` n `20`; unknown avg `-0.1509` n `751`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.11`, n `666`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `666`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0983`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0923`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0917`, n `666`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0897`, n `666`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
