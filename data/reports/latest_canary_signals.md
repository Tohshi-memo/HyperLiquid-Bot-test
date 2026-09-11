# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T11:37:26.190835+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0413` n `12`; crypto_alt avg `0.1901` n `233`; crypto_major avg `0.1133` n `8`; equity avg `0.0451` n `136`; fx avg `0.0018` n `6`; index avg `0.0144` n `26`; metal avg `-0.0155` n `20`; unknown avg `0.0715` n `796`
- 1h: commodity avg `0.0709` n `12`; crypto_alt avg `-0.4647` n `233`; crypto_major avg `-0.389` n `8`; equity avg `-0.1662` n `136`; fx avg `-0.0106` n `6`; index avg `-0.012` n `26`; metal avg `-0.0922` n `20`; unknown avg `0.0414` n `794`
- 4h: commodity avg `-0.3054` n `12`; crypto_alt avg `-1.4357` n `233`; crypto_major avg `-0.8503` n `8`; equity avg `0.0163` n `136`; fx avg `-0.0809` n `6`; index avg `0.0545` n `26`; metal avg `-0.0547` n `20`; unknown avg `-0.1718` n `788`
- 24h: commodity avg `0.3405` n `12`; crypto_alt avg `-2.4883` n `233`; crypto_major avg `-2.0854` n `8`; equity avg `-0.9631` n `136`; fx avg `-0.0998` n `6`; index avg `-0.1009` n `26`; metal avg `-0.5047` n `20`; unknown avg `1.0914` n `683`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1228`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0985`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0953`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0929`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.076`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0559`, n `668`, weak_sample_signal
