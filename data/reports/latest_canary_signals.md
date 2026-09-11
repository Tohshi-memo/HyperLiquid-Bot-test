# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-11T00:52:30.338767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0479` n `12`; crypto_alt avg `-0.0793` n `233`; crypto_major avg `0.0462` n `8`; equity avg `-0.0363` n `136`; fx avg `-0.0003` n `6`; index avg `-0.0132` n `26`; metal avg `0.0676` n `20`; unknown avg `-0.2375` n `796`
- 1h: commodity avg `-0.2002` n `12`; crypto_alt avg `0.3723` n `233`; crypto_major avg `0.1474` n `8`; equity avg `0.2587` n `136`; fx avg `-0.0292` n `6`; index avg `0.0681` n `26`; metal avg `0.1171` n `20`; unknown avg `0.4095` n `784`
- 4h: commodity avg `-0.102` n `12`; crypto_alt avg `-0.8312` n `233`; crypto_major avg `-0.8376` n `8`; equity avg `-0.0857` n `136`; fx avg `0.0127` n `6`; index avg `0.0121` n `26`; metal avg `0.0679` n `20`; unknown avg `0.1746` n `750`
- 24h: commodity avg `1.1551` n `12`; crypto_alt avg `-1.9199` n `233`; crypto_major avg `-2.2006` n `8`; equity avg `-1.7913` n `136`; fx avg `0.1345` n `6`; index avg `-0.3019` n `26`; metal avg `-1.1837` n `20`; unknown avg `-0.5004` n `683`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1432`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1378`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
