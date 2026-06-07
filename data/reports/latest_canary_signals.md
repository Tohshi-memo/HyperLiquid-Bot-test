# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T10:52:24.066616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0159` n `12`; crypto_alt avg `-0.2384` n `228`; crypto_major avg `-0.0978` n `8`; equity avg `-0.0231` n `74`; fx avg `-0.042` n `6`; index avg `0.0743` n `23`; metal avg `-0.0153` n `18`; unknown avg `-0.0291` n `516`
- 1h: commodity avg `0.0631` n `12`; crypto_alt avg `-0.8092` n `228`; crypto_major avg `-0.601` n `8`; equity avg `-0.3667` n `74`; fx avg `-0.0136` n `6`; index avg `-0.0631` n `23`; metal avg `-0.1577` n `18`; unknown avg `-3.3077` n `516`
- 4h: commodity avg `-0.2056` n `12`; crypto_alt avg `-0.457` n `228`; crypto_major avg `-0.0481` n `8`; equity avg `-0.3329` n `74`; fx avg `-0.0402` n `6`; index avg `-0.2297` n `23`; metal avg `-0.0456` n `18`; unknown avg `-4.9103` n `516`
- 24h: commodity avg `0.1729` n `12`; crypto_alt avg `3.527` n `228`; crypto_major avg `3.5163` n `8`; equity avg `2.1911` n `74`; fx avg `0.0135` n `6`; index avg `0.7654` n `23`; metal avg `0.6638` n `18`; unknown avg `0.3207` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1397`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1263`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0614`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.061`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0583`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
