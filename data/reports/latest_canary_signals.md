# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T09:22:22.513557+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.2896` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.726` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0679` n `12`; crypto_alt avg `-0.0742` n `228`; crypto_major avg `-0.0953` n `8`; equity avg `0.0227` n `74`; fx avg `-0.0106` n `6`; index avg `-0.0302` n `23`; metal avg `-0.0176` n `18`; unknown avg `0.0406` n `516`
- 1h: commodity avg `0.0801` n `12`; crypto_alt avg `1.2404` n `228`; crypto_major avg `1.2044` n `8`; equity avg `0.2894` n `74`; fx avg `-0.0353` n `6`; index avg `-0.0464` n `23`; metal avg `0.1285` n `18`; unknown avg `-0.8282` n `516`
- 4h: commodity avg `-0.3414` n `12`; crypto_alt avg `1.7531` n `228`; crypto_major avg `1.9482` n `8`; equity avg `0.5076` n `74`; fx avg `-0.0348` n `6`; index avg `0.0491` n `23`; metal avg `0.2222` n `18`; unknown avg `-2.8774` n `506`
- 24h: commodity avg `-0.0418` n `12`; crypto_alt avg `3.0664` n `228`; crypto_major avg `3.0775` n `8`; equity avg `0.744` n `74`; fx avg `0.0351` n `6`; index avg `0.6534` n `23`; metal avg `0.6797` n `18`; unknown avg `1.4878` n `401`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1412`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.14`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1269`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0621`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0599`, n `668`, weak_sample_signal
