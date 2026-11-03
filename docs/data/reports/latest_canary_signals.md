# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T12:37:43.558362+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.106` n `13`; crypto_alt avg `0.2405` n `239`; crypto_major avg `0.0083` n `8`; equity avg `0.1994` n `157`; fx avg `-0.0168` n `6`; index avg `0.0284` n `27`; metal avg `0.0642` n `20`; unknown avg `5.3297` n `1264`
- 1h: commodity avg `-0.3088` n `13`; crypto_alt avg `0.9254` n `239`; crypto_major avg `0.8414` n `8`; equity avg `0.3889` n `157`; fx avg `-0.0031` n `6`; index avg `0.0511` n `27`; metal avg `0.1501` n `20`; unknown avg `3.7552` n `1252`
- 4h: commodity avg `-0.2061` n `13`; crypto_alt avg `2.1445` n `239`; crypto_major avg `1.5443` n `8`; equity avg `1.1939` n `157`; fx avg `0.018` n `6`; index avg `0.125` n `27`; metal avg `0.1571` n `20`; unknown avg `1.5944` n `1212`
- 24h: commodity avg `-0.539` n `13`; crypto_alt avg `-0.3423` n `238`; crypto_major avg `-0.0763` n `8`; equity avg `-2.8186` n `157`; fx avg `0.0031` n `6`; index avg `-0.1676` n `27`; metal avg `-0.2328` n `20`; unknown avg `3.878` n `1020`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.1642`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1604`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1576`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
