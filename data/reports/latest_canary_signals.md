# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T08:52:18.529930+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-4.4284` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `3.1688` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0092` n `12`; crypto_alt avg `-0.0971` n `228`; crypto_major avg `0.0357` n `8`; equity avg `0.0412` n `65`; fx avg `0.0009` n `5`; index avg `-0.0059` n `23`; metal avg `-0.0077` n `18`; unknown avg `0.0007` n `383`
- 1h: commodity avg `0.0472` n `12`; crypto_alt avg `-0.1901` n `228`; crypto_major avg `-0.0811` n `8`; equity avg `0.0376` n `65`; fx avg `0.003` n `5`; index avg `0.0117` n `23`; metal avg `-0.0246` n `18`; unknown avg `0.0259` n `383`
- 4h: commodity avg `1.7781` n `12`; crypto_alt avg `-8.9794` n `228`; crypto_major avg `-2.6503` n `8`; equity avg `-2.8476` n `65`; fx avg `-0.17` n `5`; index avg `-1.7897` n `23`; metal avg `-5.8191` n `18`; unknown avg `550.1288` n `367`
- 24h: commodity avg `1.7781` n `12`; crypto_alt avg `-8.9794` n `228`; crypto_major avg `-2.6503` n `8`; equity avg `-2.8476` n `65`; fx avg `-0.17` n `5`; index avg `-1.7897` n `23`; metal avg `-5.8191` n `18`; unknown avg `550.1288` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0823`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0606`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0601`, n `668`, weak_sample_signal
