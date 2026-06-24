# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T23:22:29.196857+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.7925` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `2.3738` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0123` n `12`; crypto_alt avg `0.0438` n `228`; crypto_major avg `0.2074` n `8`; equity avg `0.2528` n `86`; fx avg `-0.0052` n `6`; index avg `-0.0324` n `23`; metal avg `0.0736` n `20`; unknown avg `-0.0661` n `764`
- 1h: commodity avg `0.0362` n `12`; crypto_alt avg `-0.2268` n `228`; crypto_major avg `0.1228` n `8`; equity avg `0.2311` n `86`; fx avg `-0.0074` n `6`; index avg `0.0264` n `23`; metal avg `-0.0063` n `20`; unknown avg `-0.5976` n `748`
- 4h: commodity avg `-0.0116` n `12`; crypto_alt avg `2.4956` n `228`; crypto_major avg `2.7809` n `8`; equity avg `3.4204` n `86`; fx avg `-0.0502` n `6`; index avg `0.7789` n `23`; metal avg `0.4071` n `20`; unknown avg `5.4791` n `748`
- 24h: commodity avg `-0.4685` n `12`; crypto_alt avg `-2.128` n `228`; crypto_major avg `-1.642` n `8`; equity avg `5.4887` n `86`; fx avg `0.0352` n `6`; index avg `0.6637` n `23`; metal avg `-1.5227` n `20`; unknown avg `-0.4735` n `716`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0859`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.071`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0632`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0607`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0585`, n `668`, weak_sample_signal
