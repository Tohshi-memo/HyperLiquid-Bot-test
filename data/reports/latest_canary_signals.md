# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-19T09:52:27.121040+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0446` n `13`; crypto_alt avg `-0.1106` n `237`; crypto_major avg `-0.0811` n `8`; equity avg `0.0849` n `151`; fx avg `-0.0084` n `6`; index avg `0.0066` n `26`; metal avg `0.0086` n `20`; unknown avg `0.4707` n `1195`
- 1h: commodity avg `0.2147` n `13`; crypto_alt avg `0.0008` n `237`; crypto_major avg `0.139` n `8`; equity avg `0.0899` n `151`; fx avg `-0.0117` n `6`; index avg `0.0071` n `26`; metal avg `0.0483` n `20`; unknown avg `0.4578` n `1193`
- 4h: commodity avg `0.2654` n `13`; crypto_alt avg `0.0346` n `237`; crypto_major avg `0.2299` n `8`; equity avg `0.0582` n `151`; fx avg `-0.0006` n `6`; index avg `-0.0116` n `26`; metal avg `-0.104` n `20`; unknown avg `0.9585` n `1126`
- 24h: commodity avg `-0.2486` n `13`; crypto_alt avg `-0.1284` n `237`; crypto_major avg `0.7883` n `8`; equity avg `2.4126` n `151`; fx avg `-0.0592` n `6`; index avg `0.4222` n `26`; metal avg `0.2301` n `20`; unknown avg `1.9155` n `971`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1984`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1446`, n `666`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1285`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1148`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1072`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0617`, n `666`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
