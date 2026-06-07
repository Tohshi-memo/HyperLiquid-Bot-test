# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T06:40:51.231536+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5653` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `0.4832` n `228`; crypto_major avg `0.4315` n `8`; equity avg `0.1571` n `74`; fx avg `0.0014` n `6`; index avg `0.0017` n `23`; metal avg `0.0232` n `18`; unknown avg `0.077` n `516`
- 1h: commodity avg `-0.0041` n `12`; crypto_alt avg `0.4961` n `228`; crypto_major avg `0.4736` n `8`; equity avg `0.268` n `74`; fx avg `-0.0093` n `6`; index avg `0.0611` n `23`; metal avg `0.0696` n `18`; unknown avg `-0.1385` n `506`
- 4h: commodity avg `-0.042` n `12`; crypto_alt avg `1.3973` n `228`; crypto_major avg `1.8842` n `8`; equity avg `0.8903` n `74`; fx avg `-0.0004` n `6`; index avg `0.3613` n `23`; metal avg `0.3189` n `18`; unknown avg `0.1188` n `506`
- 24h: commodity avg `0.4005` n `12`; crypto_alt avg `2.8511` n `228`; crypto_major avg `1.8524` n `8`; equity avg `1.857` n `74`; fx avg `0.0444` n `6`; index avg `0.9857` n `23`; metal avg `0.6334` n `18`; unknown avg `1.6469` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1336`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1327`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1195`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0677`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
