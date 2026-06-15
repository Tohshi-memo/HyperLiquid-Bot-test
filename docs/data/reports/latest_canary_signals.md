# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T00:21:42.719508+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.7176` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `4.62` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.8476` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0936` n `12`; crypto_alt avg `0.0442` n `228`; crypto_major avg `0.1163` n `8`; equity avg `0.1842` n `74`; fx avg `0.0071` n `6`; index avg `0.1581` n `23`; metal avg `0.1965` n `18`; unknown avg `-0.0222` n `645`
- 1h: commodity avg `-0.3014` n `12`; crypto_alt avg `0.527` n `228`; crypto_major avg `0.6274` n `8`; equity avg `0.5012` n `74`; fx avg `-0.1377` n `6`; index avg `0.342` n `23`; metal avg `0.5359` n `18`; unknown avg `-0.2028` n `637`
- 4h: commodity avg `-1.2189` n `12`; crypto_alt avg `3.333` n `228`; crypto_major avg `3.4987` n `8`; equity avg `1.6511` n `74`; fx avg `-0.0496` n `6`; index avg `0.5404` n `23`; metal avg `2.0877` n `18`; unknown avg `3.9513` n `637`
- 24h: commodity avg `-0.9642` n `12`; crypto_alt avg `2.0235` n `228`; crypto_major avg `2.5921` n `8`; equity avg `1.7928` n `74`; fx avg `-0.0392` n `6`; index avg `0.7026` n `23`; metal avg `1.908` n `18`; unknown avg `1.6428` n `585`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0647`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.064`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0562`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
