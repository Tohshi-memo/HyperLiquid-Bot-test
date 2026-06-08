# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T07:07:26.058610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1396` n `12`; crypto_alt avg `-0.2637` n `228`; crypto_major avg `-0.2094` n `8`; equity avg `0.1277` n `74`; fx avg `-0.0465` n `6`; index avg `-0.0106` n `23`; metal avg `-0.2527` n `18`; unknown avg `-0.0146` n `517`
- 1h: commodity avg `-0.0248` n `12`; crypto_alt avg `0.0464` n `228`; crypto_major avg `0.0873` n `8`; equity avg `0.2012` n `74`; fx avg `-0.0991` n `6`; index avg `0.188` n `23`; metal avg `-0.0134` n `18`; unknown avg `-0.0096` n `517`
- 4h: commodity avg `0.2772` n `12`; crypto_alt avg `-0.3819` n `228`; crypto_major avg `-0.506` n `8`; equity avg `-0.9563` n `74`; fx avg `-0.2354` n `6`; index avg `-0.3543` n `23`; metal avg `-0.3693` n `18`; unknown avg `-0.1997` n `507`
- 24h: commodity avg `0.9144` n `12`; crypto_alt avg `-0.2537` n `228`; crypto_major avg `1.58` n `8`; equity avg `0.1953` n `74`; fx avg `-0.3232` n `6`; index avg `-0.0355` n `23`; metal avg `-0.8925` n `18`; unknown avg `-5.5191` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1255`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.124`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1104`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0775`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0764`, n `668`, weak_sample_signal
