# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-07T02:07:20.128712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.054` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.7982` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0398` n `12`; crypto_alt avg `0.0969` n `228`; crypto_major avg `0.1067` n `8`; equity avg `0.0066` n `74`; fx avg `-0.0001` n `6`; index avg `-0.0142` n `23`; metal avg `0.0084` n `18`; unknown avg `0.0602` n `516`
- 1h: commodity avg `-0.0563` n `12`; crypto_alt avg `1.1933` n `228`; crypto_major avg `0.9274` n `8`; equity avg `0.3485` n `74`; fx avg `0.0005` n `6`; index avg `0.1177` n `23`; metal avg `0.2234` n `18`; unknown avg `1.0759` n `516`
- 4h: commodity avg `0.0336` n `12`; crypto_alt avg `2.6777` n `228`; crypto_major avg `2.0876` n `8`; equity avg `0.7758` n `74`; fx avg `-0.0159` n `6`; index avg `0.0864` n `23`; metal avg `0.2894` n `18`; unknown avg `0.9057` n `515`
- 24h: commodity avg `0.1173` n `12`; crypto_alt avg `1.4171` n `228`; crypto_major avg `0.5089` n `8`; equity avg `1.0589` n `74`; fx avg `0.0454` n `6`; index avg `0.4725` n `23`; metal avg `-0.0157` n `18`; unknown avg `0.245` n `401`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1146`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.062`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0611`, n `668`, weak_sample_signal
