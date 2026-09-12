# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T01:22:31.994620+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.0` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `0.1127` n `233`; crypto_major avg `0.0634` n `8`; equity avg `0.0112` n `136`; fx avg `-0.0006` n `6`; index avg `-0.0006` n `26`; metal avg `-0.01` n `20`; unknown avg `-0.1865` n `836`
- 1h: commodity avg `-0.021` n `12`; crypto_alt avg `0.406` n `233`; crypto_major avg `0.057` n `8`; equity avg `0.0286` n `136`; fx avg `0.0108` n `6`; index avg `0.0102` n `26`; metal avg `-0.0114` n `20`; unknown avg `0.3974` n `828`
- 4h: commodity avg `-0.0385` n `12`; crypto_alt avg `0.1008` n `233`; crypto_major avg `-0.5522` n `8`; equity avg `0.0848` n `136`; fx avg `-0.0129` n `6`; index avg `0.0327` n `26`; metal avg `-0.0387` n `20`; unknown avg `3.6107` n `814`
- 24h: commodity avg `-0.5804` n `12`; crypto_alt avg `1.337` n `233`; crypto_major avg `1.4075` n `8`; equity avg `0.871` n `136`; fx avg `-0.1699` n `6`; index avg `0.3203` n `26`; metal avg `0.2325` n `20`; unknown avg `1.3094` n `702`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1062`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0933`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0698`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
