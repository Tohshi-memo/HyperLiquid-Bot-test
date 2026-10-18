# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T15:52:31.420902+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3208` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0027` n `13`; crypto_alt avg `0.0305` n `237`; crypto_major avg `-0.005` n `8`; equity avg `-0.0066` n `151`; fx avg `0.0015` n `6`; index avg `0.008` n `26`; metal avg `-0.0037` n `20`; unknown avg `1.278` n `1194`
- 1h: commodity avg `0.0073` n `13`; crypto_alt avg `-0.1505` n `237`; crypto_major avg `-0.084` n `8`; equity avg `-0.0909` n `151`; fx avg `0.0042` n `6`; index avg `-0.0268` n `26`; metal avg `-0.0077` n `20`; unknown avg `-0.4306` n `1191`
- 4h: commodity avg `0.0063` n `13`; crypto_alt avg `-1.2357` n `237`; crypto_major avg `-1.4411` n `8`; equity avg `-0.5479` n `151`; fx avg `0.0082` n `6`; index avg `-0.1203` n `26`; metal avg `-0.0474` n `20`; unknown avg `-0.4912` n `1183`
- 24h: commodity avg `-0.0063` n `13`; crypto_alt avg `-2.6637` n `236`; crypto_major avg `-1.0125` n `8`; equity avg `-0.8496` n `151`; fx avg `-0.0191` n `6`; index avg `-0.1263` n `26`; metal avg `-0.0646` n `20`; unknown avg `0.023` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2113`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1408`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1303`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1098`, n `666`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0806`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
