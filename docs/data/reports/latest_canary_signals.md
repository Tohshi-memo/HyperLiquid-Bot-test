# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-09T19:07:26.813982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0282` n `12`; crypto_alt avg `0.0701` n `230`; crypto_major avg `0.0268` n `8`; equity avg `0.0127` n `112`; fx avg `0.0041` n `6`; index avg `0.0` n `25`; metal avg `0.011` n `20`; unknown avg `-0.0451` n `785`
- 1h: commodity avg `0.1261` n `12`; crypto_alt avg `-0.0462` n `230`; crypto_major avg `-0.0638` n `8`; equity avg `0.0074` n `112`; fx avg `0.0063` n `6`; index avg `0.0151` n `25`; metal avg `0.0154` n `20`; unknown avg `-0.2954` n `785`
- 4h: commodity avg `0.0965` n `12`; crypto_alt avg `0.549` n `230`; crypto_major avg `-0.043` n `8`; equity avg `0.0587` n `112`; fx avg `0.0091` n `6`; index avg `0.0302` n `25`; metal avg `0.0212` n `20`; unknown avg `-0.3705` n `785`
- 24h: commodity avg `0.1439` n `12`; crypto_alt avg `1.3299` n `230`; crypto_major avg `0.2357` n `8`; equity avg `0.3008` n `112`; fx avg `0.0076` n `6`; index avg `0.0538` n `25`; metal avg `0.0807` n `20`; unknown avg `-0.2566` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1535`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1049`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0821`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0633`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
