# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T09:52:14.813807+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.2591` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.3488` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.013` n `12`; crypto_alt avg `0.1133` n `228`; crypto_major avg `0.1299` n `8`; equity avg `0.0165` n `65`; fx avg `-0.0006` n `5`; index avg `0.0188` n `23`; metal avg `0.0188` n `18`; unknown avg `-0.0904` n `383`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `0.1416` n `228`; crypto_major avg `0.1674` n `8`; equity avg `0.0865` n `65`; fx avg `0.0009` n `5`; index avg `0.0541` n `23`; metal avg `-0.0182` n `18`; unknown avg `-0.0146` n `383`
- 4h: commodity avg `1.7721` n `12`; crypto_alt avg `-8.86` n `228`; crypto_major avg `-2.487` n `8`; equity avg `-2.7664` n `65`; fx avg `-0.1691` n `5`; index avg `-1.7383` n `23`; metal avg `-5.8358` n `18`; unknown avg `550.1667` n `367`
- 24h: commodity avg `1.7721` n `12`; crypto_alt avg `-8.86` n `228`; crypto_major avg `-2.487` n `8`; equity avg `-2.7664` n `65`; fx avg `-0.1691` n `5`; index avg `-1.7383` n `23`; metal avg `-5.8358` n `18`; unknown avg `550.1667` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1408`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1192`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0744`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0726`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0613`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0597`, n `668`, weak_sample_signal
