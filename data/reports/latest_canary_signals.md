# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-30T20:37:27.221966+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `-0.0847` n `230`; crypto_major avg `-0.1865` n `8`; equity avg `-0.0342` n `102`; fx avg `0.0115` n `6`; index avg `-0.0243` n `25`; metal avg `-0.0465` n `20`; unknown avg `0.1282` n `779`
- 1h: commodity avg `0.114` n `12`; crypto_alt avg `0.0467` n `230`; crypto_major avg `-0.2232` n `8`; equity avg `0.4846` n `102`; fx avg `0.0094` n `6`; index avg `0.059` n `25`; metal avg `-0.0344` n `20`; unknown avg `0.0913` n `779`
- 4h: commodity avg `-0.0112` n `12`; crypto_alt avg `0.1032` n `230`; crypto_major avg `-0.0014` n `8`; equity avg `1.0485` n `102`; fx avg `0.0082` n `6`; index avg `0.1552` n `25`; metal avg `0.1008` n `20`; unknown avg `-0.1181` n `779`
- 24h: commodity avg `-0.0904` n `12`; crypto_alt avg `1.5431` n `230`; crypto_major avg `1.8422` n `8`; equity avg `7.2301` n `102`; fx avg `-0.3744` n `6`; index avg `0.9394` n `25`; metal avg `0.6791` n `20`; unknown avg `0.156` n `738`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1392`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1138`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0827`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
