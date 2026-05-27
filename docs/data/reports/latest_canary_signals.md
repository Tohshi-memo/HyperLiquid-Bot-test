# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T20:54:43.426777+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0232` n `12`; crypto_alt avg `0.1562` n `228`; crypto_major avg `0.0977` n `8`; equity avg `-0.0101` n `67`; fx avg `-0.0008` n `6`; index avg `0.0171` n `23`; metal avg `0.0026` n `18`; unknown avg `0.0488` n `419`
- 1h: commodity avg `-0.0606` n `12`; crypto_alt avg `0.0154` n `228`; crypto_major avg `0.1523` n `8`; equity avg `0.1338` n `67`; fx avg `0.0019` n `6`; index avg `0.1109` n `23`; metal avg `0.0142` n `18`; unknown avg `0.4316` n `419`
- 4h: commodity avg `-0.3562` n `12`; crypto_alt avg `-0.3578` n `228`; crypto_major avg `-0.1563` n `8`; equity avg `0.2962` n `67`; fx avg `0.0235` n `6`; index avg `0.1348` n `23`; metal avg `-0.057` n `18`; unknown avg `0.0175` n `418`
- 24h: commodity avg `-1.1712` n `12`; crypto_alt avg `-0.3542` n `228`; crypto_major avg `0.0153` n `8`; equity avg `0.0544` n `67`; fx avg `-0.0775` n `6`; index avg `-0.3617` n `23`; metal avg `-1.2949` n `18`; unknown avg `-0.0886` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1704`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1608`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1545`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1398`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1331`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.129`, n `668`, weak_sample_signal
