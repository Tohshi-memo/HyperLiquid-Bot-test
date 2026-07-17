# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-17T07:37:26.714507+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1462` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0366` n `12`; crypto_alt avg `-0.0793` n `230`; crypto_major avg `-0.1309` n `8`; equity avg `-0.0442` n `96`; fx avg `0.0041` n `6`; index avg `0.0045` n `25`; metal avg `0.0158` n `20`; unknown avg `0.1837` n `768`
- 1h: commodity avg `0.0816` n `12`; crypto_alt avg `-0.4292` n `230`; crypto_major avg `-0.415` n `8`; equity avg `-0.3052` n `96`; fx avg `-0.0271` n `6`; index avg `-0.0349` n `25`; metal avg `-0.1004` n `20`; unknown avg `0.1269` n `768`
- 4h: commodity avg `-0.0642` n `12`; crypto_alt avg `-1.0718` n `230`; crypto_major avg `-1.3075` n `8`; equity avg `-1.0331` n `96`; fx avg `-0.0052` n `6`; index avg `-0.1613` n `25`; metal avg `-0.1686` n `20`; unknown avg `-0.1878` n `736`
- 24h: commodity avg `-0.1106` n `12`; crypto_alt avg `-2.1557` n `230`; crypto_major avg `-3.5111` n `8`; equity avg `-5.5378` n `94`; fx avg `-0.0804` n `6`; index avg `-0.743` n `25`; metal avg `-0.7322` n `20`; unknown avg `-0.5871` n `730`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1376`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0868`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0747`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0746`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
