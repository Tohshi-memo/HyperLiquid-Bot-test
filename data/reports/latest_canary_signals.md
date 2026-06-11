# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-11T17:52:38.272610+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_commodity_crypto_divergence: score `3.3305` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_commodity_crypto_divergence: score `2.2107` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.3188` n `12`; crypto_alt avg `0.4598` n `228`; crypto_major avg `0.709` n `8`; equity avg `0.221` n `74`; fx avg `-0.0529` n `6`; index avg `0.1038` n `23`; metal avg `0.1612` n `18`; unknown avg `0.1043` n `556`
- 1h: commodity avg `-1.1812` n `12`; crypto_alt avg `1.8553` n `228`; crypto_major avg `2.1493` n `8`; equity avg `1.5181` n `74`; fx avg `0.0468` n `6`; index avg `0.8127` n `23`; metal avg `2.0435` n `18`; unknown avg `0.8906` n `556`
- 4h: commodity avg `-0.8508` n `12`; crypto_alt avg `1.3539` n `228`; crypto_major avg `1.3599` n `8`; equity avg `0.8501` n `74`; fx avg `-0.0336` n `6`; index avg `0.5777` n `23`; metal avg `1.6211` n `18`; unknown avg `-0.1707` n `556`
- 24h: commodity avg `-2.0251` n `12`; crypto_alt avg `3.2602` n `228`; crypto_major avg `3.2693` n `8`; equity avg `1.3824` n `74`; fx avg `0.006` n `6`; index avg `1.0126` n `23`; metal avg `1.5683` n `18`; unknown avg `2.2391` n `530`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1375`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1016`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0805`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
