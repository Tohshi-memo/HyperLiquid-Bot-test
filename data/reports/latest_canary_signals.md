# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T09:07:24.671332+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.5699` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.9906` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.6884` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0652` n `12`; crypto_alt avg `0.2963` n `228`; crypto_major avg `0.4813` n `8`; equity avg `0.1652` n `74`; fx avg `-0.0025` n `6`; index avg `-0.0344` n `23`; metal avg `0.0337` n `18`; unknown avg `-0.2359` n `516`
- 1h: commodity avg `0.0687` n `12`; crypto_alt avg `1.3087` n `228`; crypto_major avg `1.3779` n `8`; equity avg `0.2632` n `74`; fx avg `-0.0247` n `6`; index avg `0.0922` n `23`; metal avg `0.1719` n `18`; unknown avg `-2.535` n `516`
- 4h: commodity avg `-0.2718` n `12`; crypto_alt avg `2.0598` n `228`; crypto_major avg `2.2981` n `8`; equity avg `0.6097` n `74`; fx avg `-0.0214` n `6`; index avg `0.0856` n `23`; metal avg `0.3075` n `18`; unknown avg `-2.8456` n `506`
- 24h: commodity avg `-0.0297` n `12`; crypto_alt avg `3.1923` n `228`; crypto_major avg `3.1491` n `8`; equity avg `2.4133` n `74`; fx avg `0.0392` n `6`; index avg `0.5708` n `23`; metal avg `0.6704` n `18`; unknown avg `1.3105` n `401`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.128`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.064`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
