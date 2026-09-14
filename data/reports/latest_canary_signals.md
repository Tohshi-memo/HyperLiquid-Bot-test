# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-14T01:52:30.328544+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0541` n `12`; crypto_alt avg `0.2977` n `233`; crypto_major avg `0.2191` n `8`; equity avg `0.2039` n `136`; fx avg `-0.0002` n `6`; index avg `0.0316` n `27`; metal avg `0.0342` n `20`; unknown avg `0.5605` n `894`
- 1h: commodity avg `-0.057` n `12`; crypto_alt avg `0.151` n `233`; crypto_major avg `0.0198` n `8`; equity avg `0.0018` n `136`; fx avg `0.011` n `6`; index avg `0.012` n `27`; metal avg `-0.0097` n `20`; unknown avg `0.1055` n `774`
- 4h: commodity avg `0.4627` n `12`; crypto_alt avg `-1.197` n `233`; crypto_major avg `-0.8749` n `8`; equity avg `-0.7535` n `136`; fx avg `0.0045` n `6`; index avg `-0.1704` n `27`; metal avg `-0.032` n `20`; unknown avg `12.0967` n `768`
- 24h: commodity avg `0.6775` n `12`; crypto_alt avg `-1.7221` n `233`; crypto_major avg `-1.5474` n `8`; equity avg `-1.6972` n `136`; fx avg `0.057` n `6`; index avg `-0.3593` n `26`; metal avg `-0.0774` n `20`; unknown avg `1.5428` n `682`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1321`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.129`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1223`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.116`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.0812`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
