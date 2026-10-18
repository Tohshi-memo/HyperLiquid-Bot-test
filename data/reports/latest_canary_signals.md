# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T17:07:25.031686+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.3022` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0062` n `13`; crypto_alt avg `0.2058` n `237`; crypto_major avg `0.1771` n `8`; equity avg `0.0118` n `151`; fx avg `-0.0032` n `6`; index avg `-0.0005` n `26`; metal avg `0.0077` n `20`; unknown avg `-0.0057` n `1192`
- 1h: commodity avg `0.0041` n `13`; crypto_alt avg `0.0685` n `237`; crypto_major avg `0.0997` n `8`; equity avg `0.0313` n `151`; fx avg `0.0022` n `6`; index avg `0.0144` n `26`; metal avg `0.0072` n `20`; unknown avg `-0.2101` n `1192`
- 4h: commodity avg `0.0348` n `13`; crypto_alt avg `-1.6265` n `237`; crypto_major avg `-1.3933` n `8`; equity avg `-0.5131` n `151`; fx avg `-0.0012` n `6`; index avg `-0.0911` n `26`; metal avg `-0.0476` n `20`; unknown avg `-0.5119` n `1159`
- 24h: commodity avg `0.0225` n `13`; crypto_alt avg `-2.1694` n `236`; crypto_major avg `-0.7461` n `8`; equity avg `-0.7758` n `151`; fx avg `-0.0232` n `6`; index avg `-0.0844` n `26`; metal avg `-0.0296` n `20`; unknown avg `0.7232` n `1017`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2108`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1406`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1288`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.08`, n `666`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0631`, n `668`, weak_sample_signal
