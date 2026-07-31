# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-31T04:07:27.973519+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0344` n `12`; crypto_alt avg `0.0115` n `230`; crypto_major avg `-0.1002` n `8`; equity avg `0.0663` n `102`; fx avg `0.0141` n `6`; index avg `0.0136` n `25`; metal avg `-0.0068` n `20`; unknown avg `0.0637` n `779`
- 1h: commodity avg `0.0035` n `12`; crypto_alt avg `0.2301` n `230`; crypto_major avg `0.1463` n `8`; equity avg `0.1641` n `102`; fx avg `-0.0013` n `6`; index avg `0.0075` n `25`; metal avg `0.027` n `20`; unknown avg `0.1005` n `779`
- 4h: commodity avg `-0.262` n `12`; crypto_alt avg `-0.2868` n `230`; crypto_major avg `-0.6407` n `8`; equity avg `0.1919` n `102`; fx avg `0.1117` n `6`; index avg `0.0797` n `25`; metal avg `-0.2514` n `20`; unknown avg `0.1538` n `779`
- 24h: commodity avg `-0.197` n `12`; crypto_alt avg `-0.0012` n `230`; crypto_major avg `0.7416` n `8`; equity avg `8.1621` n `102`; fx avg `-0.1262` n `6`; index avg `1.0776` n `25`; metal avg `0.4935` n `20`; unknown avg `0.0592` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1402`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1315`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0962`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0813`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
