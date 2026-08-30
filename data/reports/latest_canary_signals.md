# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-30T04:07:23.014571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.003` n `12`; crypto_alt avg `-0.0926` n `231`; crypto_major avg `-0.0084` n `8`; equity avg `0.0052` n `128`; fx avg `-0.0012` n `6`; index avg `0.015` n `26`; metal avg `-0.0001` n `20`; unknown avg `-0.1294` n `793`
- 1h: commodity avg `-0.0218` n `12`; crypto_alt avg `-0.0024` n `231`; crypto_major avg `0.0004` n `8`; equity avg `0.0161` n `128`; fx avg `0.0006` n `6`; index avg `-0.0048` n `26`; metal avg `0.0068` n `20`; unknown avg `-0.2511` n `793`
- 4h: commodity avg `-0.0032` n `12`; crypto_alt avg `-0.0914` n `231`; crypto_major avg `-0.0981` n `8`; equity avg `0.0416` n `128`; fx avg `0.0036` n `6`; index avg `0.019` n `26`; metal avg `-0.0044` n `20`; unknown avg `-0.3437` n `793`
- 24h: commodity avg `-0.0272` n `12`; crypto_alt avg `0.5076` n `231`; crypto_major avg `0.8273` n `8`; equity avg `0.3327` n `128`; fx avg `-0.0032` n `6`; index avg `0.0658` n `26`; metal avg `0.097` n `20`; unknown avg `0.1395` n `728`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1787`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1276`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0938`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0918`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0895`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0882`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0867`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
