# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-06T22:22:25.279381+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0455` n `12`; crypto_alt avg `0.148` n `228`; crypto_major avg `0.0797` n `8`; equity avg `-0.0173` n `74`; fx avg `0.0006` n `6`; index avg `0.0036` n `23`; metal avg `0.0` n `18`; unknown avg `0.0433` n `515`
- 1h: commodity avg `0.0255` n `12`; crypto_alt avg `-0.0477` n `228`; crypto_major avg `-0.4508` n `8`; equity avg `-0.1766` n `74`; fx avg `-0.0094` n `6`; index avg `-0.052` n `23`; metal avg `0.0043` n `18`; unknown avg `0.1983` n `515`
- 4h: commodity avg `0.14` n `12`; crypto_alt avg `0.3323` n `228`; crypto_major avg `-0.092` n `8`; equity avg `0.2198` n `74`; fx avg `-0.1688` n `6`; index avg `0.046` n `23`; metal avg `0.0276` n `18`; unknown avg `-0.1443` n `515`
- 24h: commodity avg `0.7992` n `12`; crypto_alt avg `-2.3598` n `228`; crypto_major avg `-2.2843` n `8`; equity avg `-1.1679` n `74`; fx avg `0.0215` n `6`; index avg `-0.0468` n `23`; metal avg `-0.5782` n `18`; unknown avg `-0.6237` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0699`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0574`, n `668`, weak_sample_signal
