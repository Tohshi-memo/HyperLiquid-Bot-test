# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T04:39:13.996039+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0061` n `12`; crypto_alt avg `-0.0465` n `230`; crypto_major avg `-0.0306` n `8`; equity avg `-0.069` n `98`; fx avg `-0.0133` n `6`; index avg `-0.0328` n `25`; metal avg `-0.0162` n `20`; unknown avg `-0.0935` n `771`
- 1h: commodity avg `0.0142` n `12`; crypto_alt avg `0.0123` n `230`; crypto_major avg `0.1656` n `8`; equity avg `-0.0322` n `98`; fx avg `-0.0035` n `6`; index avg `-0.0215` n `25`; metal avg `-0.0776` n `20`; unknown avg `-0.1953` n `771`
- 4h: commodity avg `0.1127` n `12`; crypto_alt avg `-0.3469` n `230`; crypto_major avg `-0.4016` n `8`; equity avg `-0.7725` n `98`; fx avg `0.0444` n `6`; index avg `-0.103` n `25`; metal avg `0.2874` n `20`; unknown avg `-0.4468` n `771`
- 24h: commodity avg `0.6133` n `12`; crypto_alt avg `0.0527` n `230`; crypto_major avg `0.0089` n `8`; equity avg `2.297` n `98`; fx avg `0.082` n `6`; index avg `0.2653` n `25`; metal avg `0.7589` n `20`; unknown avg `0.2741` n `755`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0958`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0804`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0613`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0591`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0527`, n `666`, weak_sample_signal
