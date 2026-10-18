# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T17:18:23.935285+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1406` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.009` n `13`; crypto_alt avg `-0.0131` n `237`; crypto_major avg `0.0716` n `8`; equity avg `-0.0263` n `151`; fx avg `0.0131` n `6`; index avg `-0.0014` n `26`; metal avg `0.0005` n `20`; unknown avg `-0.0018` n `1194`
- 1h: commodity avg `0.0103` n `13`; crypto_alt avg `-0.0586` n `237`; crypto_major avg `0.1906` n `8`; equity avg `-0.0695` n `151`; fx avg `0.0124` n `6`; index avg `0.0064` n `26`; metal avg `0.0119` n `20`; unknown avg `-0.1732` n `1192`
- 4h: commodity avg `0.0449` n `13`; crypto_alt avg `-1.6202` n `237`; crypto_major avg `-1.2234` n `8`; equity avg `-0.4605` n `151`; fx avg `0.0142` n `6`; index avg `-0.0828` n `26`; metal avg `-0.0455` n `20`; unknown avg `-0.1134` n `1159`
- 24h: commodity avg `0.0343` n `13`; crypto_alt avg `-2.5158` n `236`; crypto_major avg `-0.8758` n `8`; equity avg `-0.8039` n `151`; fx avg `-0.0032` n `6`; index avg `-0.0891` n `26`; metal avg `-0.0279` n `20`; unknown avg `0.6651` n `1017`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2107`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1406`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1289`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
