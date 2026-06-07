# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T04:52:26.931553+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0454` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5181` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0262` n `12`; crypto_alt avg `0.0777` n `228`; crypto_major avg `0.2858` n `8`; equity avg `0.0996` n `74`; fx avg `0.0007` n `6`; index avg `0.1014` n `23`; metal avg `0.0279` n `18`; unknown avg `-0.2003` n `516`
- 1h: commodity avg `-0.0217` n `12`; crypto_alt avg `0.1933` n `228`; crypto_major avg `0.494` n `8`; equity avg `0.1737` n `74`; fx avg `0.004` n `6`; index avg `0.0006` n `23`; metal avg `0.0098` n `18`; unknown avg `-0.0969` n `516`
- 4h: commodity avg `-0.1159` n `12`; crypto_alt avg `1.3433` n `228`; crypto_major avg `1.9295` n `8`; equity avg `0.6603` n `74`; fx avg `0.0065` n `6`; index avg `0.4574` n `23`; metal avg `0.4114` n `18`; unknown avg `2.0333` n `516`
- 24h: commodity avg `0.4078` n `12`; crypto_alt avg `4.7656` n `228`; crypto_major avg `3.2702` n `8`; equity avg `2.3209` n `74`; fx avg `0.0462` n `6`; index avg `1.3553` n `23`; metal avg `0.7768` n `18`; unknown avg `0.8185` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1265`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1252`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1025`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0651`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0596`, n `668`, weak_sample_signal
