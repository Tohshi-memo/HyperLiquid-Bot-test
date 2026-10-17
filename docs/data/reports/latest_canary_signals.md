# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T20:55:58.621860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0213` n `13`; crypto_alt avg `0.0949` n `236`; crypto_major avg `0.0932` n `8`; equity avg `-0.004` n `151`; fx avg `0.0006` n `6`; index avg `-0.0082` n `26`; metal avg `-0.0036` n `20`; unknown avg `-0.0157` n `1193`
- 1h: commodity avg `0.0082` n `13`; crypto_alt avg `-0.0829` n `236`; crypto_major avg `0.1117` n `8`; equity avg `-0.0521` n `151`; fx avg `0.0013` n `6`; index avg `-0.0117` n `26`; metal avg `-0.0081` n `20`; unknown avg `-0.0826` n `1177`
- 4h: commodity avg `-0.0052` n `13`; crypto_alt avg `1.0118` n `236`; crypto_major avg `0.7269` n `8`; equity avg `0.1144` n `151`; fx avg `-0.0073` n `6`; index avg `0.0009` n `26`; metal avg `0.0114` n `20`; unknown avg `3.0334` n `1113`
- 24h: commodity avg `0.0449` n `13`; crypto_alt avg `-1.006` n `236`; crypto_major avg `-0.1288` n `8`; equity avg `-0.2768` n `151`; fx avg `-0.0286` n `6`; index avg `-0.0293` n `26`; metal avg `-0.0258` n `20`; unknown avg `4.4976` n `1049`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1711`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1482`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1139`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1128`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0993`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0735`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0723`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0689`, n `668`, weak_sample_signal
