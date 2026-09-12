# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T10:37:26.218925+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.53` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0269` n `12`; crypto_alt avg `0.0309` n `233`; crypto_major avg `0.0082` n `8`; equity avg `-0.0052` n `136`; fx avg `0.0027` n `6`; index avg `0.0004` n `26`; metal avg `0.0032` n `20`; unknown avg `0.1462` n `838`
- 1h: commodity avg `0.006` n `12`; crypto_alt avg `0.2194` n `233`; crypto_major avg `0.1777` n `8`; equity avg `0.0262` n `136`; fx avg `-0.0062` n `6`; index avg `0.0039` n `26`; metal avg `0.0102` n `20`; unknown avg `0.0914` n `836`
- 4h: commodity avg `0.0468` n `12`; crypto_alt avg `0.4761` n `233`; crypto_major avg `0.5293` n `8`; equity avg `0.0207` n `136`; fx avg `0.0015` n `6`; index avg `0.0035` n `26`; metal avg `0.0094` n `20`; unknown avg `0.685` n `830`
- 24h: commodity avg `-0.0042` n `12`; crypto_alt avg `2.4614` n `233`; crypto_major avg `1.7212` n `8`; equity avg `0.086` n `136`; fx avg `-0.0522` n `6`; index avg `0.1114` n `26`; metal avg `-0.0429` n `20`; unknown avg `1.2654` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.085`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0788`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0778`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0579`, n `668`, weak_sample_signal
