# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T17:37:29.586874+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0103` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0495` n `13`; crypto_alt avg `-0.2181` n `235`; crypto_major avg `-0.0798` n `8`; equity avg `-0.2663` n `151`; fx avg `0.0049` n `6`; index avg `-0.0336` n `26`; metal avg `0.0087` n `20`; unknown avg `1.3251` n `1137`
- 1h: commodity avg `0.0765` n `13`; crypto_alt avg `0.1274` n `235`; crypto_major avg `0.0505` n `8`; equity avg `-0.2823` n `151`; fx avg `0.0334` n `6`; index avg `-0.0385` n `26`; metal avg `0.0125` n `20`; unknown avg `0.6331` n `1135`
- 4h: commodity avg `0.0262` n `13`; crypto_alt avg `-0.9918` n `235`; crypto_major avg `-1.2927` n `8`; equity avg `-1.7469` n `151`; fx avg `-0.0185` n `6`; index avg `-0.2824` n `26`; metal avg `-0.3974` n `20`; unknown avg `0.2277` n `1102`
- 24h: commodity avg `0.0724` n `13`; crypto_alt avg `-2.1521` n `235`; crypto_major avg `-1.8331` n `8`; equity avg `-3.5319` n `151`; fx avg `-0.1289` n `6`; index avg `-0.4863` n `26`; metal avg `-0.8202` n `20`; unknown avg `1261.3935` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0995`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0799`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0729`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0625`, n `666`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0575`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0544`, n `666`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0532`, n `666`, weak_sample_signal
