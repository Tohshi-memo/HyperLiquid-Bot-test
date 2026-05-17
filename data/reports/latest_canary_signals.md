# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T08:07:16.140512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-4.2923` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-4.2923` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.2325` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `3.2325` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0023` n `12`; crypto_alt avg `-0.0307` n `228`; crypto_major avg `0.0062` n `8`; equity avg `0.0107` n `65`; fx avg `0.0006` n `5`; index avg `-0.0086` n `23`; metal avg `-0.0032` n `18`; unknown avg `0.0614` n `383`
- 1h: commodity avg `1.7265` n `12`; crypto_alt avg `-8.841` n `228`; crypto_major avg `-2.5658` n `8`; equity avg `-2.8755` n `65`; fx avg `-0.1723` n `5`; index avg `-1.8092` n `23`; metal avg `-5.7983` n `18`; unknown avg `550.1402` n `367`
- 4h: commodity avg `1.7265` n `12`; crypto_alt avg `-8.841` n `228`; crypto_major avg `-2.5658` n `8`; equity avg `-2.8755` n `65`; fx avg `-0.1723` n `5`; index avg `-1.8092` n `23`; metal avg `-5.7983` n `18`; unknown avg `550.1402` n `367`
- 24h: commodity avg `1.7265` n `12`; crypto_alt avg `-8.841` n `228`; crypto_major avg `-2.5658` n `8`; equity avg `-2.8755` n `65`; fx avg `-0.1723` n `5`; index avg `-1.8092` n `23`; metal avg `-5.7983` n `18`; unknown avg `550.1402` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1404`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1191`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0748`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0731`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0609`, n `668`, weak_sample_signal
