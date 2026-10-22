# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-22T02:07:27.937889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.03` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.5298` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0088` n `13`; crypto_alt avg `-0.2636` n `237`; crypto_major avg `-0.2426` n `8`; equity avg `-0.1988` n `151`; fx avg `-0.0187` n `6`; index avg `-0.0106` n `26`; metal avg `-0.1017` n `20`; unknown avg `2.9588` n `1199`
- 1h: commodity avg `0.056` n `13`; crypto_alt avg `-1.1616` n `237`; crypto_major avg `-0.8866` n `8`; equity avg `-0.7826` n `151`; fx avg `-0.0427` n `6`; index avg `-0.084` n `26`; metal avg `-0.1851` n `20`; unknown avg `2.5163` n `1199`
- 4h: commodity avg `0.2117` n `13`; crypto_alt avg `-1.9154` n `237`; crypto_major avg `-1.7744` n `8`; equity avg `-1.821` n `151`; fx avg `-0.068` n `6`; index avg `-0.2446` n `26`; metal avg `-0.3782` n `20`; unknown avg `8.4291` n `1042`
- 24h: commodity avg `-0.5935` n `13`; crypto_alt avg `0.0077` n `237`; crypto_major avg `-0.334` n `8`; equity avg `-1.7859` n `151`; fx avg `-0.0604` n `6`; index avg `-0.2483` n `26`; metal avg `-0.4651` n `20`; unknown avg `121.5214` n `945`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1659`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1446`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1247`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1206`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1044`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.102`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.094`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
