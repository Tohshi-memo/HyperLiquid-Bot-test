# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-13T18:22:27.729889+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0035` n `12`; crypto_alt avg `0.0432` n `233`; crypto_major avg `0.0813` n `8`; equity avg `0.0197` n `136`; fx avg `0.0008` n `6`; index avg `0.0032` n `27`; metal avg `0.0004` n `20`; unknown avg `0.2243` n `840`
- 1h: commodity avg `0.0253` n `12`; crypto_alt avg `0.015` n `233`; crypto_major avg `0.0075` n `8`; equity avg `0.0534` n `136`; fx avg `0.001` n `6`; index avg `-0.0011` n `27`; metal avg `-0.0101` n `20`; unknown avg `1.2211` n `822`
- 4h: commodity avg `0.1021` n `12`; crypto_alt avg `-0.0092` n `233`; crypto_major avg `0.4747` n `8`; equity avg `0.2221` n `136`; fx avg `-0.0038` n `6`; index avg `-0.0139` n `27`; metal avg `0.0046` n `20`; unknown avg `1.53` n `774`
- 24h: commodity avg `0.2308` n `12`; crypto_alt avg `0.128` n `233`; crypto_major avg `-0.6673` n `8`; equity avg `-1.3749` n `136`; fx avg `0.0092` n `6`; index avg `-0.2603` n `26`; metal avg `-0.0807` n `20`; unknown avg `1.4681` n `688`

## Correlations

- market_context_score -> index_forward_1h_return_pct: corr `-0.0891`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0886`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0655`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0597`, n `668`, weak_sample_signal
