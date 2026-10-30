# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-30T02:52:33.652667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0812` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.02` n `13`; crypto_alt avg `-0.5571` n `238`; crypto_major avg `-0.4102` n `8`; equity avg `-0.0771` n `156`; fx avg `-0.0084` n `6`; index avg `-0.0227` n `27`; metal avg `-0.0752` n `20`; unknown avg `0.1809` n `1258`
- 1h: commodity avg `-0.263` n `13`; crypto_alt avg `0.6711` n `238`; crypto_major avg `1.0611` n `8`; equity avg `0.5609` n `156`; fx avg `0.0155` n `6`; index avg `0.0431` n `27`; metal avg `0.0055` n `20`; unknown avg `4.2496` n `1252`
- 4h: commodity avg `0.1472` n `13`; crypto_alt avg `-2.309` n `238`; crypto_major avg `-1.2311` n `8`; equity avg `-0.4127` n `156`; fx avg `-0.0056` n `6`; index avg `-0.1499` n `27`; metal avg `-0.3366` n `20`; unknown avg `11.1241` n `1238`
- 24h: commodity avg `-0.0627` n `13`; crypto_alt avg `-5.3343` n `238`; crypto_major avg `-1.3963` n `8`; equity avg `-2.9504` n `155`; fx avg `0.1843` n `6`; index avg `-0.3221` n `27`; metal avg `-0.7755` n `20`; unknown avg `29.578` n `986`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1023`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0784`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0736`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0677`, n `668`, weak_sample_signal
