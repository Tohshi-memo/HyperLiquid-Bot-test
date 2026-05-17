# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T07:52:13.018858+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `-4.3094` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `-4.3094` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `3.2468` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_metal_divergence: score `3.2468` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0192` n `12`; crypto_alt avg `0.0364` n `228`; crypto_major avg `-0.0429` n `8`; equity avg `-0.0284` n `65`; fx avg `-0.0038` n `5`; index avg `0.0031` n `23`; metal avg `0.0033` n `18`; unknown avg `-0.0721` n `383`
- 1h: commodity avg `1.7576` n `12`; crypto_alt avg `-8.7935` n `228`; crypto_major avg `-2.5518` n `8`; equity avg `-2.8927` n `65`; fx avg `-0.1704` n `5`; index avg `-1.8003` n `23`; metal avg `-5.7986` n `18`; unknown avg `550.0511` n `367`
- 4h: commodity avg `1.7576` n `12`; crypto_alt avg `-8.7935` n `228`; crypto_major avg `-2.5518` n `8`; equity avg `-2.8927` n `65`; fx avg `-0.1704` n `5`; index avg `-1.8003` n `23`; metal avg `-5.7986` n `18`; unknown avg `550.0511` n `367`
- 24h: commodity avg `1.7576` n `12`; crypto_alt avg `-8.7935` n `228`; crypto_major avg `-2.5518` n `8`; equity avg `-2.8927` n `65`; fx avg `-0.1704` n `5`; index avg `-1.8003` n `23`; metal avg `-5.7986` n `18`; unknown avg `550.0511` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1403`, n `669`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.119`, n `669`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0949`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `669`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0813`, n `669`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0741`, n `669`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0739`, n `669`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0696`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0622`, n `669`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0618`, n `669`, weak_sample_signal
