# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T20:52:38.785296+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `2.2065` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_commodity_crypto_divergence: score `2.1596` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.1152` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_crypto_metal_divergence: score `1.7865` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0073` n `12`; crypto_alt avg `0.2309` n `228`; crypto_major avg `0.34` n `8`; equity avg `0.3697` n `86`; fx avg `-0.0007` n `6`; index avg `0.0833` n `23`; metal avg `-0.0001` n `20`; unknown avg `-0.4252` n `764`
- 1h: commodity avg `-0.0434` n `12`; crypto_alt avg `1.786` n `228`; crypto_major avg `2.0718` n `8`; equity avg `2.4454` n `86`; fx avg `0.0` n `6`; index avg `0.5328` n `23`; metal avg `0.2853` n `20`; unknown avg `5.2363` n `764`
- 4h: commodity avg `-0.1532` n `12`; crypto_alt avg `2.1006` n `228`; crypto_major avg `2.0064` n `8`; equity avg `1.7798` n `86`; fx avg `0.0004` n `6`; index avg `0.4778` n `23`; metal avg `-0.2001` n `20`; unknown avg `4.4123` n `764`
- 24h: commodity avg `-0.5466` n `12`; crypto_alt avg `-2.4015` n `228`; crypto_major avg `-1.6644` n `8`; equity avg `4.3961` n `86`; fx avg `0.0482` n `6`; index avg `0.6062` n `23`; metal avg `-1.6163` n `20`; unknown avg `-0.689` n `724`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1214`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0811`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
