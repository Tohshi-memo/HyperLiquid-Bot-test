# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T02:06:32.762265+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2698` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8873` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0749` n `12`; crypto_alt avg `0.1041` n `228`; crypto_major avg `0.2198` n `8`; equity avg `0.1683` n `74`; fx avg `0.0076` n `6`; index avg `-0.1322` n `23`; metal avg `0.0558` n `18`; unknown avg `-0.1608` n `517`
- 1h: commodity avg `0.4344` n `12`; crypto_alt avg `-0.3657` n `228`; crypto_major avg `-0.1631` n `8`; equity avg `-0.1641` n `74`; fx avg `0.0008` n `6`; index avg `-0.2871` n `23`; metal avg `-0.0833` n `18`; unknown avg `-0.3675` n `517`
- 4h: commodity avg `-0.1598` n `12`; crypto_alt avg `1.3672` n `228`; crypto_major avg `2.11` n `8`; equity avg `1.0506` n `74`; fx avg `-0.0357` n `6`; index avg `0.2301` n `23`; metal avg `0.2227` n `18`; unknown avg `0.2134` n `516`
- 24h: commodity avg `0.2707` n `12`; crypto_alt avg `0.7516` n `228`; crypto_major avg `3.4199` n `8`; equity avg `1.3895` n `74`; fx avg `-0.0957` n `6`; index avg `0.1959` n `23`; metal avg `0.0876` n `18`; unknown avg `-5.4659` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0999`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0733`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0635`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0633`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0598`, n `668`, weak_sample_signal
