# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-04T06:07:25.113786+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0332` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8577` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0651` n `12`; crypto_alt avg `0.2454` n `228`; crypto_major avg `0.1696` n `8`; equity avg `0.166` n `73`; fx avg `0.0054` n `6`; index avg `0.0071` n `23`; metal avg `0.1313` n `18`; unknown avg `-0.171` n `404`
- 1h: commodity avg `-0.0984` n `12`; crypto_alt avg `0.4321` n `228`; crypto_major avg `0.1416` n `8`; equity avg `0.1238` n `73`; fx avg `0.0039` n `6`; index avg `-0.0331` n `23`; metal avg `-0.1473` n `18`; unknown avg `-0.2361` n `404`
- 4h: commodity avg `0.002` n `12`; crypto_alt avg `1.8376` n `228`; crypto_major avg `2.0352` n `8`; equity avg `0.8829` n `73`; fx avg `-0.0025` n `6`; index avg `0.1856` n `23`; metal avg `0.1775` n `18`; unknown avg `1.6195` n `404`
- 24h: commodity avg `-0.2045` n `12`; crypto_alt avg `-4.194` n `228`; crypto_major avg `-3.475` n `8`; equity avg `-3.617` n `73`; fx avg `-0.0203` n `6`; index avg `-1.0889` n `23`; metal avg `-1.2532` n `18`; unknown avg `0.6216` n `403`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1674`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.147`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1442`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1035`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0875`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0688`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
