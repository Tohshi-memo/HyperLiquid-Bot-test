# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T10:22:32.743887+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0111` n `12`; crypto_alt avg `0.161` n `229`; crypto_major avg `-0.0603` n `8`; equity avg `0.0521` n `91`; fx avg `-0.0145` n `6`; index avg `-0.002` n `25`; metal avg `0.0226` n `20`; unknown avg `-0.0514` n `763`
- 1h: commodity avg `-0.1094` n `12`; crypto_alt avg `0.3917` n `229`; crypto_major avg `0.2088` n `8`; equity avg `0.0145` n `91`; fx avg `-0.0535` n `6`; index avg `0.0044` n `25`; metal avg `0.1353` n `20`; unknown avg `-0.0324` n `761`
- 4h: commodity avg `-0.0262` n `12`; crypto_alt avg `0.454` n `229`; crypto_major avg `0.4659` n `8`; equity avg `-0.007` n `91`; fx avg `-0.1184` n `6`; index avg `-0.011` n `25`; metal avg `0.2862` n `20`; unknown avg `-0.4145` n `757`
- 24h: commodity avg `0.338` n `12`; crypto_alt avg `0.7606` n `229`; crypto_major avg `0.0901` n `8`; equity avg `-1.4709` n `90`; fx avg `-0.1248` n `6`; index avg `-0.3462` n `25`; metal avg `-0.164` n `20`; unknown avg `-0.4559` n `739`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1116`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0805`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0747`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0636`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0629`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0537`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0496`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
