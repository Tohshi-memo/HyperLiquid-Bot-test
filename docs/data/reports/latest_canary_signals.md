# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T13:22:34.960548+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.22` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.9866` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_commodity_crypto_divergence: score `2.7003` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.4719` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0815` n `12`; crypto_alt avg `0.6199` n `228`; crypto_major avg `0.6999` n `8`; equity avg `0.1387` n `74`; fx avg `0.0034` n `6`; index avg `0.0741` n `23`; metal avg `0.2658` n `18`; unknown avg `-0.0728` n `689`
- 1h: commodity avg `0.0498` n `12`; crypto_alt avg `1.163` n `228`; crypto_major avg `1.3244` n `8`; equity avg `0.1919` n `74`; fx avg `0.0013` n `6`; index avg `0.1546` n `23`; metal avg `0.5749` n `18`; unknown avg `-0.1569` n `689`
- 4h: commodity avg `0.3033` n `12`; crypto_alt avg `2.3006` n `228`; crypto_major avg `3.0036` n `8`; equity avg `0.017` n `74`; fx avg `-0.0042` n `6`; index avg `0.1837` n `23`; metal avg `0.5317` n `18`; unknown avg `0.2165` n `689`
- 24h: commodity avg `-1.0792` n `12`; crypto_alt avg `6.1497` n `228`; crypto_major avg `6.5308` n `8`; equity avg `1.6897` n `74`; fx avg `0.0363` n `6`; index avg `0.9915` n `23`; metal avg `3.0302` n `18`; unknown avg `1.1591` n `529`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1172`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0831`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0695`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0632`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
