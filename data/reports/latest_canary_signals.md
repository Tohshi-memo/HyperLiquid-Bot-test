# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T00:07:36.946225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `4.6588` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `4.24` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.0498` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `1.6396` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.1453` n `12`; crypto_alt avg `0.1118` n `228`; crypto_major avg `0.0133` n `8`; equity avg `0.2066` n `74`; fx avg `-0.0668` n `6`; index avg `0.1862` n `23`; metal avg `0.0032` n `18`; unknown avg `0.0155` n `645`
- 1h: commodity avg `-0.2213` n `12`; crypto_alt avg `0.6147` n `228`; crypto_major avg `0.6338` n `8`; equity avg `0.2822` n `74`; fx avg `-0.1395` n `6`; index avg `0.1616` n `23`; metal avg `0.1734` n `18`; unknown avg `-0.2961` n `637`
- 4h: commodity avg `-1.1635` n `12`; crypto_alt avg `3.4209` n `228`; crypto_major avg `3.4953` n `8`; equity avg `1.4455` n `74`; fx avg `-0.0203` n `6`; index avg `0.3875` n `23`; metal avg `1.8557` n `18`; unknown avg `2.8818` n `637`
- 24h: commodity avg `-0.8604` n `12`; crypto_alt avg `2.061` n `228`; crypto_major avg `2.4382` n `8`; equity avg `1.5866` n `74`; fx avg `-0.0464` n `6`; index avg `0.5433` n `23`; metal avg `1.7` n `18`; unknown avg `1.59` n `585`

## Correlations

- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0852`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0737`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0604`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0479`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0476`, n `668`, weak_sample_signal
