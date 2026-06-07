# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T07:22:23.148214+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0549` n `12`; crypto_alt avg `-0.17` n `228`; crypto_major avg `-0.1531` n `8`; equity avg `-0.0344` n `74`; fx avg `-0.0039` n `6`; index avg `0.007` n `23`; metal avg `0.002` n `18`; unknown avg `-0.1086` n `516`
- 1h: commodity avg `-0.1872` n `12`; crypto_alt avg `0.2203` n `228`; crypto_major avg `0.3499` n `8`; equity avg `0.0881` n `74`; fx avg `-0.0054` n `6`; index avg `-0.0228` n `23`; metal avg `0.0259` n `18`; unknown avg `-0.0854` n `516`
- 4h: commodity avg `-0.2038` n `12`; crypto_alt avg `0.5768` n `228`; crypto_major avg `0.9937` n `8`; equity avg `0.5994` n `74`; fx avg `-0.0067` n `6`; index avg `0.1707` n `23`; metal avg `0.1706` n `18`; unknown avg `-0.1608` n `506`
- 24h: commodity avg `0.2537` n `12`; crypto_alt avg `2.8268` n `228`; crypto_major avg `2.1597` n `8`; equity avg `2.2334` n `74`; fx avg `0.0485` n `6`; index avg `1.0142` n `23`; metal avg `0.5736` n `18`; unknown avg `0.5565` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1366`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1357`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0773`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0635`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0619`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
