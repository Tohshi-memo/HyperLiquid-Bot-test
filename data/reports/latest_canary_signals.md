# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T05:07:29.484579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0057` n `12`; crypto_alt avg `0.3784` n `231`; crypto_major avg `0.2986` n `8`; equity avg `0.0246` n `128`; fx avg `-0.0006` n `6`; index avg `0.0117` n `26`; metal avg `0.0066` n `20`; unknown avg `-0.3186` n `793`
- 1h: commodity avg `0.0158` n `12`; crypto_alt avg `0.1132` n `231`; crypto_major avg `0.0521` n `8`; equity avg `0.0034` n `128`; fx avg `0.0` n `6`; index avg `-0.0004` n `26`; metal avg `-0.002` n `20`; unknown avg `-0.4543` n `793`
- 4h: commodity avg `0.0052` n `12`; crypto_alt avg `0.1472` n `231`; crypto_major avg `0.0493` n `8`; equity avg `0.0567` n `128`; fx avg `0.0042` n `6`; index avg `0.0093` n `26`; metal avg `0.0014` n `20`; unknown avg `-0.674` n `793`
- 24h: commodity avg `0.0078` n `12`; crypto_alt avg `0.243` n `231`; crypto_major avg `0.5699` n `8`; equity avg `0.2938` n `128`; fx avg `-0.0154` n `6`; index avg `0.0561` n `26`; metal avg `0.0784` n `20`; unknown avg `0.116` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1845`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1363`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.096`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0952`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0863`, n `668`, weak_sample_signal
