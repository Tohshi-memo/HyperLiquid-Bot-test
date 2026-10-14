# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-14T15:52:38.784593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.8104` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0319` n `13`; crypto_alt avg `-0.4034` n `235`; crypto_major avg `-0.3574` n `8`; equity avg `-0.1049` n `151`; fx avg `0.0147` n `6`; index avg `-0.018` n `26`; metal avg `-0.0412` n `20`; unknown avg `1.8641` n `1137`
- 1h: commodity avg `-0.0135` n `13`; crypto_alt avg `-0.1477` n `235`; crypto_major avg `0.0677` n `8`; equity avg `-0.7004` n `151`; fx avg `-0.0103` n `6`; index avg `-0.1037` n `26`; metal avg `-0.1032` n `20`; unknown avg `1.2733` n `1111`
- 4h: commodity avg `-0.2508` n `13`; crypto_alt avg `-2.4675` n `235`; crypto_major avg `-2.1761` n `8`; equity avg `-2.528` n `151`; fx avg `-0.1282` n `6`; index avg `-0.3657` n `26`; metal avg `-0.7137` n `20`; unknown avg `2.2968` n `1102`
- 24h: commodity avg `-0.0713` n `13`; crypto_alt avg `-2.2303` n `235`; crypto_major avg `-1.9504` n `8`; equity avg `-2.543` n `151`; fx avg `-0.1555` n `6`; index avg `-0.312` n `26`; metal avg `-0.8285` n `20`; unknown avg `1260.7443` n `981`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0915`, n `666`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0812`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.072`, n `666`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0677`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0595`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0542`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0539`, n `666`, weak_sample_signal
