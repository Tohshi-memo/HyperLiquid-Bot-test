# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T09:22:28.747482+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `13`; crypto_alt avg `0.1779` n `239`; crypto_major avg `0.0208` n `8`; equity avg `0.1196` n `157`; fx avg `-0.0036` n `6`; index avg `0.0095` n `27`; metal avg `0.0385` n `20`; unknown avg `0.0037` n `1264`
- 1h: commodity avg `0.1121` n `13`; crypto_alt avg `0.5444` n `239`; crypto_major avg `0.3892` n `8`; equity avg `0.5823` n `157`; fx avg `0.0258` n `6`; index avg `0.0503` n `27`; metal avg `-0.1177` n `20`; unknown avg `0.5065` n `1248`
- 4h: commodity avg `0.3753` n `13`; crypto_alt avg `0.0925` n `239`; crypto_major avg `0.1491` n `8`; equity avg `0.6265` n `157`; fx avg `0.0678` n `6`; index avg `0.0704` n `27`; metal avg `-0.3105` n `20`; unknown avg `0.8437` n `1206`
- 24h: commodity avg `-0.2418` n `13`; crypto_alt avg `-2.0206` n `238`; crypto_major avg `-1.4752` n `8`; equity avg `-3.7729` n `157`; fx avg `-0.0211` n `6`; index avg `-0.2677` n `27`; metal avg `-0.5285` n `20`; unknown avg `4.0367` n `1021`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1658`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1608`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1581`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1498`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.127`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1108`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1014`, n `668`, weak_sample_signal
