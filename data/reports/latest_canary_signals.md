# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-03T20:10:27.591411+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0748` n `13`; crypto_alt avg `-0.0218` n `239`; crypto_major avg `0.0607` n `8`; equity avg `0.0159` n `158`; fx avg `-0.0026` n `6`; index avg `0.0021` n `27`; metal avg `-0.0379` n `20`; unknown avg `71.4014` n `1233`
- 1h: commodity avg `0.1956` n `13`; crypto_alt avg `-0.1593` n `239`; crypto_major avg `-0.0026` n `8`; equity avg `-0.0342` n `158`; fx avg `-0.0077` n `6`; index avg `-0.0284` n `27`; metal avg `-0.0775` n `20`; unknown avg `20.9097` n `1233`
- 4h: commodity avg `0.3302` n `13`; crypto_alt avg `-0.4286` n `239`; crypto_major avg `-0.3458` n `8`; equity avg `-0.6075` n `158`; fx avg `0.0341` n `6`; index avg `-0.1058` n `27`; metal avg `-0.1846` n `20`; unknown avg `0.1139` n `1201`
- 24h: commodity avg `0.3965` n `13`; crypto_alt avg `0.9778` n `239`; crypto_major avg `1.2509` n `8`; equity avg `0.9491` n `158`; fx avg `0.0757` n `6`; index avg `0.0461` n `27`; metal avg `-0.5858` n `20`; unknown avg `370.7492` n `1059`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1505`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1405`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.138`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
