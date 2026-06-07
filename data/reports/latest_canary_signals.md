# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T08:37:24.315710+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.1956` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.5431` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0442` n `12`; crypto_alt avg `0.3631` n `228`; crypto_major avg `0.4728` n `8`; equity avg `0.0305` n `74`; fx avg `-0.0054` n `6`; index avg `0.0045` n `23`; metal avg `0.0268` n `18`; unknown avg `0.0052` n `516`
- 1h: commodity avg `-0.2366` n `12`; crypto_alt avg `0.1717` n `228`; crypto_major avg `0.4302` n `8`; equity avg `-0.0705` n `74`; fx avg `-0.0033` n `6`; index avg `0.0999` n `23`; metal avg `0.0572` n `18`; unknown avg `-1.8082` n `516`
- 4h: commodity avg `-0.3996` n `12`; crypto_alt avg `1.0676` n `228`; crypto_major avg `1.796` n `8`; equity avg `0.5332` n `74`; fx avg `0.0002` n `6`; index avg `0.1845` n `23`; metal avg `0.2529` n `18`; unknown avg `-1.9934` n `506`
- 24h: commodity avg `0.0779` n `12`; crypto_alt avg `2.1458` n `228`; crypto_major avg `1.9845` n `8`; equity avg `2.3709` n `74`; fx avg `0.0588` n `6`; index avg `1.214` n `23`; metal avg `0.6268` n `18`; unknown avg `0.5155` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1377`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0762`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0717`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0603`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0564`, n `668`, weak_sample_signal
