# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T03:07:26.093565+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0843` n `12`; crypto_alt avg `-0.2094` n `233`; crypto_major avg `-0.2493` n `8`; equity avg `-0.0953` n `136`; fx avg `0.0035` n `6`; index avg `-0.0133` n `26`; metal avg `-0.0452` n `20`; unknown avg `-0.1541` n `794`
- 1h: commodity avg `0.0241` n `12`; crypto_alt avg `-0.3468` n `233`; crypto_major avg `-0.3126` n `8`; equity avg `-0.295` n `136`; fx avg `-0.0248` n `6`; index avg `-0.0358` n `26`; metal avg `-0.0438` n `20`; unknown avg `-0.1108` n `788`
- 4h: commodity avg `-0.1198` n `12`; crypto_alt avg `-0.3191` n `233`; crypto_major avg `-0.1527` n `8`; equity avg `-0.1591` n `136`; fx avg `-0.0569` n `6`; index avg `0.0039` n `26`; metal avg `-0.0362` n `20`; unknown avg `-0.6833` n `778`
- 24h: commodity avg `1.2126` n `12`; crypto_alt avg `-2.6335` n `233`; crypto_major avg `-2.8183` n `8`; equity avg `-2.0913` n `136`; fx avg `0.0836` n `6`; index avg `-0.3582` n `26`; metal avg `-1.3477` n `20`; unknown avg `-1.0161` n `677`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1447`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.118`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
