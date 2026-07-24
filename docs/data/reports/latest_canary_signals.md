# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-24T02:52:24.410147+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0308` n `12`; crypto_alt avg `0.0114` n `230`; crypto_major avg `-0.0192` n `8`; equity avg `-0.0836` n `100`; fx avg `0.0038` n `6`; index avg `-0.055` n `25`; metal avg `-0.1162` n `20`; unknown avg `0.1846` n `772`
- 1h: commodity avg `0.0737` n `12`; crypto_alt avg `-0.236` n `230`; crypto_major avg `-0.301` n `8`; equity avg `-0.493` n `100`; fx avg `-0.0094` n `6`; index avg `-0.1565` n `25`; metal avg `-0.2281` n `20`; unknown avg `0.0462` n `772`
- 4h: commodity avg `-0.0086` n `12`; crypto_alt avg `-0.1248` n `230`; crypto_major avg `-0.3374` n `8`; equity avg `-0.8228` n `100`; fx avg `-0.1195` n `6`; index avg `-0.3047` n `25`; metal avg `-0.2884` n `20`; unknown avg `-0.391` n `772`
- 24h: commodity avg `0.5002` n `12`; crypto_alt avg `-1.4359` n `230`; crypto_major avg `-2.229` n `8`; equity avg `-2.0064` n `99`; fx avg `-0.1132` n `6`; index avg `-0.5462` n `25`; metal avg `-1.0978` n `20`; unknown avg `-0.3527` n `740`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1732`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1622`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1047`, n `666`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0956`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0952`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0916`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0856`, n `666`, weak_sample_signal
