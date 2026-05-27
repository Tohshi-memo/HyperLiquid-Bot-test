# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T21:37:17.290187+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0139` n `12`; crypto_alt avg `-0.6597` n `228`; crypto_major avg `-0.4373` n `8`; equity avg `-0.0252` n `67`; fx avg `0.0196` n `6`; index avg `0.0029` n `23`; metal avg `-0.0465` n `18`; unknown avg `-0.3143` n `419`
- 1h: commodity avg `0.0102` n `12`; crypto_alt avg `-0.52` n `228`; crypto_major avg `-0.4656` n `8`; equity avg `-0.1395` n `67`; fx avg `0.0014` n `6`; index avg `0.0228` n `23`; metal avg `-0.0079` n `18`; unknown avg `-0.2733` n `419`
- 4h: commodity avg `-0.1695` n `12`; crypto_alt avg `-0.345` n `228`; crypto_major avg `-0.0401` n `8`; equity avg `0.2824` n `67`; fx avg `0.0144` n `6`; index avg `0.2159` n `23`; metal avg `0.041` n `18`; unknown avg `-0.1675` n `418`
- 24h: commodity avg `-1.4111` n `12`; crypto_alt avg `-1.0959` n `228`; crypto_major avg `-0.4695` n `8`; equity avg `-0.1941` n `67`; fx avg `-0.0596` n `6`; index avg `-0.4195` n `23`; metal avg `-1.3097` n `18`; unknown avg `-0.3152` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1747`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1737`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1633`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1561`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1452`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1387`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.133`, n `668`, weak_sample_signal
