# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-18T06:22:28.660842+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `13`; crypto_alt avg `-0.1315` n `237`; crypto_major avg `-0.0529` n `8`; equity avg `-0.0445` n `151`; fx avg `-0.0022` n `6`; index avg `-0.0059` n `26`; metal avg `-0.0038` n `20`; unknown avg `0.0148` n `1193`
- 1h: commodity avg `0.0059` n `13`; crypto_alt avg `-0.27` n `237`; crypto_major avg `-0.2109` n `8`; equity avg `-0.0464` n `151`; fx avg `-0.0026` n `6`; index avg `-0.0057` n `26`; metal avg `-0.0115` n `20`; unknown avg `0.0821` n `1175`
- 4h: commodity avg `-0.0335` n `13`; crypto_alt avg `-0.6021` n `237`; crypto_major avg `-0.154` n `8`; equity avg `0.049` n `151`; fx avg `-0.0167` n `6`; index avg `0.0254` n `26`; metal avg `0.0083` n `20`; unknown avg `0.0835` n `1169`
- 24h: commodity avg `-0.0964` n `13`; crypto_alt avg `-3.0164` n `236`; crypto_major avg `-0.9361` n `8`; equity avg `-0.9708` n `151`; fx avg `-0.0496` n `6`; index avg `-0.1196` n `26`; metal avg `-0.0702` n `20`; unknown avg `3.8953` n `1051`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1675`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1329`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0802`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0755`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0575`, n `668`, weak_sample_signal
