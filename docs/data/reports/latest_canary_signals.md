# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T22:22:31.505575+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.5645` n `234`; crypto_major avg `0.2651` n `8`; equity avg `0.1165` n `142`; fx avg `-0.003` n `6`; index avg `0.0268` n `26`; metal avg `-0.0068` n `20`; unknown avg `3.7969` n `975`
- 1h: commodity avg `-0.0238` n `12`; crypto_alt avg `0.1684` n `234`; crypto_major avg `0.0816` n `8`; equity avg `0.1467` n `142`; fx avg `-0.0158` n `6`; index avg `0.0408` n `26`; metal avg `-0.0195` n `20`; unknown avg `0.5091` n `973`
- 4h: commodity avg `-0.1531` n `12`; crypto_alt avg `-0.3839` n `234`; crypto_major avg `0.1052` n `8`; equity avg `-0.0282` n `142`; fx avg `0.0164` n `6`; index avg `-0.0372` n `26`; metal avg `0.0786` n `20`; unknown avg `3.8514` n `887`
- 24h: commodity avg `0.3116` n `12`; crypto_alt avg `0.187` n `234`; crypto_major avg `0.7687` n `8`; equity avg `-0.4584` n `142`; fx avg `0.0798` n `6`; index avg `-0.075` n `26`; metal avg `-0.2582` n `20`; unknown avg `764.9357` n `812`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1341`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1009`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0896`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0874`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
