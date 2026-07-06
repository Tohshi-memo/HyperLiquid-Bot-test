# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-06T21:07:26.490051+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.001` n `12`; crypto_alt avg `0.0788` n `229`; crypto_major avg `0.1178` n `8`; equity avg `0.0405` n `91`; fx avg `0.0003` n `6`; index avg `0.032` n `25`; metal avg `0.0141` n `20`; unknown avg `-0.179` n `763`
- 1h: commodity avg `-0.0015` n `12`; crypto_alt avg `0.1653` n `229`; crypto_major avg `0.2531` n `8`; equity avg `0.0046` n `91`; fx avg `-0.0055` n `6`; index avg `0.0201` n `25`; metal avg `0.0218` n `20`; unknown avg `-0.311` n `763`
- 4h: commodity avg `0.1773` n `12`; crypto_alt avg `-0.1555` n `229`; crypto_major avg `-0.1185` n `8`; equity avg `-0.43` n `91`; fx avg `-0.0198` n `6`; index avg `-0.0241` n `25`; metal avg `0.0457` n `20`; unknown avg `-0.5274` n `763`
- 24h: commodity avg `0.0608` n `12`; crypto_alt avg `1.0611` n `229`; crypto_major avg `0.7778` n `8`; equity avg `-0.6113` n `90`; fx avg `0.1763` n `6`; index avg `0.0411` n `25`; metal avg `-0.2055` n `20`; unknown avg `0.0083` n `729`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0889`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0734`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0731`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0608`, n `668`, weak_sample_signal
