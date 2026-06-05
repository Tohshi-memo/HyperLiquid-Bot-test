# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T19:52:23.630846+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_crypto_metal_divergence: score `1.5291` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0435` n `12`; crypto_alt avg `1.5371` n `228`; crypto_major avg `1.2778` n `8`; equity avg `0.1734` n `74`; fx avg `0.0075` n `6`; index avg `0.0047` n `23`; metal avg `-0.0512` n `18`; unknown avg `1.7769` n `425`
- 1h: commodity avg `-0.19` n `12`; crypto_alt avg `1.5524` n `228`; crypto_major avg `1.5468` n `8`; equity avg `0.7454` n `74`; fx avg `-0.004` n `6`; index avg `0.0545` n `23`; metal avg `0.0177` n `18`; unknown avg `1.214` n `424`
- 4h: commodity avg `-0.2496` n `12`; crypto_alt avg `-0.2054` n `228`; crypto_major avg `-0.4741` n `8`; equity avg `-1.6913` n `74`; fx avg `-0.0495` n `6`; index avg `-1.7116` n `23`; metal avg `-0.6852` n `18`; unknown avg `0.8857` n `424`
- 24h: commodity avg `-1.6508` n `12`; crypto_alt avg `-8.812` n `228`; crypto_major avg `-7.14` n `8`; equity avg `-6.3549` n `74`; fx avg `-0.0404` n `6`; index avg `-4.2628` n `23`; metal avg `-4.5798` n `18`; unknown avg `-1.1432` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1286`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1242`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0637`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0627`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
