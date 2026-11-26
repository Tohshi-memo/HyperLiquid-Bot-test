# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-26T16:37:35.434400+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0306` n `13`; crypto_alt avg `-0.2176` n `239`; crypto_major avg `-0.1851` n `8`; equity avg `-0.1072` n `168`; fx avg `-0.0006` n `6`; index avg `-0.0095` n `27`; metal avg `-0.021` n `20`; unknown avg `0.1422` n `1267`
- 1h: commodity avg `-0.0118` n `13`; crypto_alt avg `0.2056` n `239`; crypto_major avg `0.0094` n `8`; equity avg `-0.0664` n `168`; fx avg `0.0045` n `6`; index avg `-0.0064` n `27`; metal avg `-0.0609` n `20`; unknown avg `-0.0807` n `1243`
- 4h: commodity avg `0.1476` n `13`; crypto_alt avg `-0.5394` n `239`; crypto_major avg `-0.6309` n `8`; equity avg `-0.3473` n `168`; fx avg `-0.0052` n `6`; index avg `-0.043` n `27`; metal avg `-0.0817` n `20`; unknown avg `-0.0597` n `1243`
- 24h: commodity avg `0.2947` n `13`; crypto_alt avg `4.6474` n `239`; crypto_major avg `3.6341` n `8`; equity avg `6.6467` n `168`; fx avg `0.0485` n `6`; index avg `0.6227` n `27`; metal avg `1.4221` n `20`; unknown avg `10.932` n `1054`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1124`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1025`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.086`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
