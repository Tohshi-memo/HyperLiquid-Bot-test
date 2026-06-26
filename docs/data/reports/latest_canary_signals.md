# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-26T14:07:26.333440+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0111` n `12`; crypto_alt avg `0.512` n `228`; crypto_major avg `0.7043` n `8`; equity avg `0.9662` n `86`; fx avg `0.0047` n `6`; index avg `0.2014` n `23`; metal avg `0.2389` n `20`; unknown avg `0.1048` n `765`
- 1h: commodity avg `-0.1388` n `12`; crypto_alt avg `1.3455` n `228`; crypto_major avg `1.7675` n `8`; equity avg `1.6398` n `86`; fx avg `-0.0174` n `6`; index avg `0.2164` n `23`; metal avg `0.3247` n `20`; unknown avg `0.4711` n `765`
- 4h: commodity avg `-0.0231` n `12`; crypto_alt avg `0.4806` n `228`; crypto_major avg `0.6053` n `8`; equity avg `1.0282` n `86`; fx avg `0.0193` n `6`; index avg `0.1326` n `23`; metal avg `0.3744` n `20`; unknown avg `-0.0438` n `765`
- 24h: commodity avg `-0.2548` n `12`; crypto_alt avg `1.8071` n `228`; crypto_major avg `2.2468` n `8`; equity avg `-0.5858` n `86`; fx avg `0.0497` n `6`; index avg `-0.2226` n `23`; metal avg `0.7914` n `20`; unknown avg `0.7955` n `701`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.3466`, n `668`, moderate_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.2262`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.2152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1739`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.166`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1188`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1041`, n `668`, weak_sample_signal
