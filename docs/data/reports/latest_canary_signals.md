# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T10:52:30.996368+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.5` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0048` n `12`; crypto_alt avg `-0.058` n `233`; crypto_major avg `-0.0153` n `8`; equity avg `-0.018` n `136`; fx avg `-0.0018` n `6`; index avg `-0.0026` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.8465` n `838`
- 1h: commodity avg `-0.0384` n `12`; crypto_alt avg `0.1351` n `233`; crypto_major avg `0.1761` n `8`; equity avg `0.0119` n `136`; fx avg `-0.0019` n `6`; index avg `0.0016` n `26`; metal avg `0.0049` n `20`; unknown avg `0.5518` n `836`
- 4h: commodity avg `0.0546` n `12`; crypto_alt avg `0.4055` n `233`; crypto_major avg `0.4936` n `8`; equity avg `0.0115` n `136`; fx avg `-0.0084` n `6`; index avg `0.0004` n `26`; metal avg `0.0068` n `20`; unknown avg `1.0886` n `830`
- 24h: commodity avg `0.0367` n `12`; crypto_alt avg `2.5226` n `233`; crypto_major avg `1.7556` n `8`; equity avg `0.1203` n `136`; fx avg `-0.0515` n `6`; index avg `0.1133` n `26`; metal avg `-0.0159` n `20`; unknown avg `1.1793` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0608`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
