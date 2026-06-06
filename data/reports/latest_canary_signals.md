# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T07:52:24.970236+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `0.203` n `228`; crypto_major avg `0.1991` n `8`; equity avg `-0.2292` n `74`; fx avg `0.0043` n `6`; index avg `-0.1662` n `23`; metal avg `-0.0416` n `18`; unknown avg `0.0986` n `425`
- 1h: commodity avg `0.0162` n `12`; crypto_alt avg `0.8777` n `228`; crypto_major avg `0.7329` n `8`; equity avg `-0.3552` n `74`; fx avg `0.0033` n `6`; index avg `-0.1508` n `23`; metal avg `0.0178` n `18`; unknown avg `0.1822` n `425`
- 4h: commodity avg `-0.6422` n `12`; crypto_alt avg `0.4861` n `228`; crypto_major avg `0.7528` n `8`; equity avg `-0.4465` n `74`; fx avg `0.0034` n `6`; index avg `-0.2043` n `23`; metal avg `0.0663` n `18`; unknown avg `0.1127` n `415`
- 24h: commodity avg `-1.2593` n `12`; crypto_alt avg `-3.9321` n `228`; crypto_major avg `-3.3367` n `8`; equity avg `-6.685` n `74`; fx avg `-0.2267` n `6`; index avg `-4.2344` n `23`; metal avg `-4.2433` n `18`; unknown avg `0.3786` n `414`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1136`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0834`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0829`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0638`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0626`, n `668`, weak_sample_signal
