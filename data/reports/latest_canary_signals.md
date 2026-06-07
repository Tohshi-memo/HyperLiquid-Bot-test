# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T06:37:23.147159+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0624` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7192` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0119` n `12`; crypto_alt avg `0.483` n `228`; crypto_major avg `0.567` n `8`; equity avg `0.1616` n `74`; fx avg `0.0014` n `6`; index avg `0.0103` n `23`; metal avg `0.0075` n `18`; unknown avg `0.0454` n `516`
- 1h: commodity avg `-0.002` n `12`; crypto_alt avg `0.4959` n `228`; crypto_major avg `0.6092` n `8`; equity avg `0.2726` n `74`; fx avg `-0.0093` n `6`; index avg `0.0697` n `23`; metal avg `0.054` n `18`; unknown avg `-0.139` n `506`
- 4h: commodity avg `-0.04` n `12`; crypto_alt avg `1.3973` n `228`; crypto_major avg `2.0224` n `8`; equity avg `0.8949` n `74`; fx avg `-0.0004` n `6`; index avg `0.3699` n `23`; metal avg `0.3032` n `18`; unknown avg `0.1183` n `506`
- 24h: commodity avg `0.4026` n `12`; crypto_alt avg `2.8514` n `228`; crypto_major avg `1.9894` n `8`; equity avg `1.8621` n `74`; fx avg `0.0444` n `6`; index avg `0.9944` n `23`; metal avg `0.6175` n `18`; unknown avg `1.6472` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1334`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1325`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0712`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0679`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0579`, n `668`, weak_sample_signal
