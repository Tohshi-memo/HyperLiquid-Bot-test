# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-08T16:22:28.532318+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0027` n `12`; crypto_alt avg `0.0358` n `230`; crypto_major avg `-0.0403` n `8`; equity avg `0.0347` n `112`; fx avg `-0.0069` n `6`; index avg `-0.0096` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.0784` n `784`
- 1h: commodity avg `0.0001` n `12`; crypto_alt avg `0.3307` n `230`; crypto_major avg `0.1036` n `8`; equity avg `-0.0402` n `112`; fx avg `-0.011` n `6`; index avg `-0.0049` n `25`; metal avg `0.0058` n `20`; unknown avg `-0.0157` n `784`
- 4h: commodity avg `-0.0478` n `12`; crypto_alt avg `0.8202` n `230`; crypto_major avg `0.7188` n `8`; equity avg `0.1993` n `112`; fx avg `-0.0139` n `6`; index avg `0.0338` n `25`; metal avg `-0.0075` n `20`; unknown avg `-0.24` n `784`
- 24h: commodity avg `-0.302` n `12`; crypto_alt avg `1.2261` n `230`; crypto_major avg `1.0026` n `8`; equity avg `0.5315` n `112`; fx avg `-0.0025` n `6`; index avg `0.0417` n `25`; metal avg `0.0891` n `20`; unknown avg `-0.1041` n `750`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0707`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0686`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.063`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0596`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0555`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0509`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0508`, n `668`, weak_sample_signal
