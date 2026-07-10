# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-10T05:52:27.584485+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0613` n `12`; crypto_alt avg `-0.0306` n `229`; crypto_major avg `0.0493` n `8`; equity avg `-0.083` n `91`; fx avg `-0.0221` n `6`; index avg `-0.004` n `25`; metal avg `0.0443` n `20`; unknown avg `0.2933` n `765`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.0009` n `229`; crypto_major avg `0.054` n `8`; equity avg `-0.3143` n `91`; fx avg `-0.0466` n `6`; index avg `-0.0329` n `25`; metal avg `-0.0327` n `20`; unknown avg `-0.2045` n `765`
- 4h: commodity avg `-0.0456` n `12`; crypto_alt avg `-0.169` n `229`; crypto_major avg `0.1336` n `8`; equity avg `-0.3737` n `91`; fx avg `-0.0564` n `6`; index avg `-0.0462` n `25`; metal avg `0.0892` n `20`; unknown avg `0.1273` n `763`
- 24h: commodity avg `-0.8878` n `12`; crypto_alt avg `1.0092` n `229`; crypto_major avg `1.2198` n `8`; equity avg `1.2937` n `91`; fx avg `0.0043` n `6`; index avg `0.3634` n `25`; metal avg `0.6689` n `20`; unknown avg `0.0815` n `746`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0924`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0785`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.078`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0723`, n `668`, weak_sample_signal
