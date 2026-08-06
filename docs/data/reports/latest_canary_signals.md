# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-06T08:37:37.543320+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1017` n `12`; crypto_alt avg `0.0042` n `230`; crypto_major avg `0.1029` n `8`; equity avg `0.2604` n `108`; fx avg `-0.0097` n `6`; index avg `0.0497` n `25`; metal avg `0.0708` n `20`; unknown avg `0.0121` n `782`
- 1h: commodity avg `-0.07` n `12`; crypto_alt avg `-0.1012` n `230`; crypto_major avg `-0.0526` n `8`; equity avg `-0.0253` n `108`; fx avg `-0.0306` n `6`; index avg `-0.0022` n `25`; metal avg `0.0889` n `20`; unknown avg `-0.0816` n `782`
- 4h: commodity avg `0.1292` n `12`; crypto_alt avg `0.1409` n `230`; crypto_major avg `-0.0034` n `8`; equity avg `-0.1823` n `108`; fx avg `0.0759` n `6`; index avg `-0.027` n `25`; metal avg `0.064` n `20`; unknown avg `-0.0654` n `750`
- 24h: commodity avg `-0.2429` n `12`; crypto_alt avg `0.1019` n `230`; crypto_major avg `-0.2955` n `8`; equity avg `-1.3298` n `108`; fx avg `-0.003` n `6`; index avg `-0.2836` n `25`; metal avg `0.371` n `20`; unknown avg `0.7538` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.185`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1425`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0709`, n `668`, weak_sample_signal
