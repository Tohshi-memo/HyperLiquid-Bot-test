# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T06:52:31.535825+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0028` n `12`; crypto_alt avg `-0.1091` n `233`; crypto_major avg `-0.1241` n `8`; equity avg `-0.0273` n `136`; fx avg `0.0006` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0008` n `20`; unknown avg `2.9821` n `840`
- 1h: commodity avg `-0.0199` n `12`; crypto_alt avg `-0.2378` n `233`; crypto_major avg `-0.4145` n `8`; equity avg `-0.2058` n `136`; fx avg `-0.003` n `6`; index avg `-0.0361` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.1446` n `812`
- 4h: commodity avg `0.0787` n `12`; crypto_alt avg `-0.0795` n `233`; crypto_major avg `-0.5309` n `8`; equity avg `-0.4048` n `136`; fx avg `-0.0068` n `6`; index avg `-0.0676` n `26`; metal avg `0.0041` n `20`; unknown avg `-0.006` n `804`
- 24h: commodity avg `0.1778` n `12`; crypto_alt avg `0.7088` n `233`; crypto_major avg `-0.2489` n `8`; equity avg `-0.7656` n `136`; fx avg `-0.0194` n `6`; index avg `-0.1271` n `26`; metal avg `0.0323` n `20`; unknown avg `0.5834` n `708`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0857`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0581`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0527`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0519`, n `668`, weak_sample_signal
