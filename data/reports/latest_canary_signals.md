# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-12T11:37:26.222912+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.44` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0179` n `12`; crypto_alt avg `0.0215` n `233`; crypto_major avg `0.0981` n `8`; equity avg `0.0355` n `136`; fx avg `-0.0019` n `6`; index avg `-0.0002` n `26`; metal avg `0.0054` n `20`; unknown avg `0.0089` n `838`
- 1h: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.0824` n `233`; crypto_major avg `0.0649` n `8`; equity avg `0.04` n `136`; fx avg `-0.0078` n `6`; index avg `-0.0035` n `26`; metal avg `-0.0015` n `20`; unknown avg `0.853` n `836`
- 4h: commodity avg `0.0475` n `12`; crypto_alt avg `0.0672` n `233`; crypto_major avg `0.4488` n `8`; equity avg `0.0656` n `136`; fx avg `-0.0066` n `6`; index avg `-0.0028` n `26`; metal avg `0.0094` n `20`; unknown avg `0.9724` n `830`
- 24h: commodity avg `-0.0865` n `12`; crypto_alt avg `2.8641` n `233`; crypto_major avg `2.186` n `8`; equity avg `0.2927` n `136`; fx avg `-0.0494` n `6`; index avg `0.12` n `26`; metal avg `0.0479` n `20`; unknown avg `1.1876` n `692`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0861`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0759`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0757`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.058`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0572`, n `668`, weak_sample_signal
