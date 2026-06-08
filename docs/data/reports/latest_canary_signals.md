# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T00:07:28.167025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.9931` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.14` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7493` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0596` n `12`; crypto_alt avg `0.1214` n `228`; crypto_major avg `0.08` n `8`; equity avg `0.2864` n `74`; fx avg `-0.0022` n `6`; index avg `0.0605` n `23`; metal avg `0.0326` n `18`; unknown avg `-0.0228` n `517`
- 1h: commodity avg `-0.143` n `12`; crypto_alt avg `0.1661` n `228`; crypto_major avg `0.4336` n `8`; equity avg `0.3203` n `74`; fx avg `-0.0056` n `6`; index avg `0.2187` n `23`; metal avg `0.4329` n `18`; unknown avg `0.0801` n `516`
- 4h: commodity avg `-0.3945` n `12`; crypto_alt avg `2.1711` n `228`; crypto_major avg `2.5986` n `8`; equity avg `0.8493` n `74`; fx avg `-0.0504` n `6`; index avg `0.2714` n `23`; metal avg `0.4586` n `18`; unknown avg `1.0576` n `516`
- 24h: commodity avg `0.1125` n `12`; crypto_alt avg `2.9295` n `228`; crypto_major avg `4.9224` n `8`; equity avg `1.5004` n `74`; fx avg `-0.0636` n `6`; index avg `0.3637` n `23`; metal avg `0.6796` n `18`; unknown avg `-4.4429` n `506`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1219`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0594`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
