# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T08:52:19.423876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1853` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5391` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0388` n `12`; crypto_alt avg `0.6491` n `228`; crypto_major avg `0.3408` n `8`; equity avg `0.0708` n `74`; fx avg `-0.0169` n `6`; index avg `0.0138` n `23`; metal avg `0.0856` n `18`; unknown avg `-0.619` n `516`
- 1h: commodity avg `-0.0633` n `12`; crypto_alt avg `0.8027` n `228`; crypto_major avg `0.8101` n `8`; equity avg `0.0632` n `74`; fx avg `-0.0077` n `6`; index avg `0.1326` n `23`; metal avg `0.1393` n `18`; unknown avg `-2.4223` n `516`
- 4h: commodity avg `-0.3354` n `12`; crypto_alt avg `1.6475` n `228`; crypto_major avg `1.8499` n `8`; equity avg `0.5042` n `74`; fx avg `-0.0174` n `6`; index avg `0.0959` n `23`; metal avg `0.3108` n `18`; unknown avg `-2.6034` n `506`
- 24h: commodity avg `0.0716` n `12`; crypto_alt avg `2.6644` n `228`; crypto_major avg `2.2029` n `8`; equity avg `2.2912` n `74`; fx avg `0.0419` n `6`; index avg `1.0502` n `23`; metal avg `0.685` n `18`; unknown avg `0.2843` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1389`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1388`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1284`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1105`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0659`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0563`, n `668`, weak_sample_signal
