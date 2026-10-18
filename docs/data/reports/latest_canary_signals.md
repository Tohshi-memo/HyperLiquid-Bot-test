# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T11:37:26.176097+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0523` n `13`; crypto_alt avg `-0.1984` n `237`; crypto_major avg `-0.1131` n `8`; equity avg `-0.0021` n `151`; fx avg `0.0009` n `6`; index avg `0.006` n `26`; metal avg `0.0068` n `20`; unknown avg `0.1367` n `1193`
- 1h: commodity avg `0.0582` n `13`; crypto_alt avg `-0.2702` n `237`; crypto_major avg `-0.1579` n `8`; equity avg `-0.0654` n `151`; fx avg `0.0072` n `6`; index avg `-0.0143` n `26`; metal avg `0.0017` n `20`; unknown avg `0.1106` n `1191`
- 4h: commodity avg `0.0309` n `13`; crypto_alt avg `0.1267` n `237`; crypto_major avg `0.4154` n `8`; equity avg `0.2035` n `151`; fx avg `0.0074` n `6`; index avg `0.036` n `26`; metal avg `0.0254` n `20`; unknown avg `5.0775` n `1079`
- 24h: commodity avg `0.0827` n `13`; crypto_alt avg `-2.3838` n `236`; crypto_major avg `-0.3653` n `8`; equity avg `-0.6605` n `151`; fx avg `-0.0398` n `6`; index avg `-0.0904` n `26`; metal avg `-0.0437` n `20`; unknown avg `4.7399` n `1033`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.2043`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1341`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1301`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1097`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0735`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0638`, n `666`, weak_sample_signal
