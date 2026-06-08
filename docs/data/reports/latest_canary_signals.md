# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T01:52:25.554590+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6333` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.1744` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.5102` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.2099` n `12`; crypto_alt avg `0.3092` n `228`; crypto_major avg `0.2279` n `8`; equity avg `0.328` n `74`; fx avg `0.0134` n `6`; index avg `0.106` n `23`; metal avg `0.2363` n `18`; unknown avg `-0.1266` n `517`
- 1h: commodity avg `0.1545` n `12`; crypto_alt avg `-1.2378` n `228`; crypto_major avg `-1.2019` n `8`; equity avg `-0.6421` n `74`; fx avg `-0.0089` n `6`; index avg `-0.2304` n `23`; metal avg `-0.4732` n `18`; unknown avg `0.0324` n `517`
- 4h: commodity avg `-0.441` n `12`; crypto_alt avg `1.8114` n `228`; crypto_major avg `2.1923` n `8`; equity avg `0.6821` n `74`; fx avg `-0.0591` n `6`; index avg `0.1087` n `23`; metal avg `0.0179` n `18`; unknown avg `0.2259` n `516`
- 24h: commodity avg `0.1549` n `12`; crypto_alt avg `0.743` n `228`; crypto_major avg `3.3039` n `8`; equity avg `1.2255` n `74`; fx avg `-0.1034` n `6`; index avg `0.3116` n `23`; metal avg `0.0403` n `18`; unknown avg `-5.2688` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0991`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0828`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0641`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0602`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.06`, n `668`, weak_sample_signal
